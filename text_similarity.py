from sentence_transformers import SentenceTransformer, util
from bert_score import BERTScorer
from fastapi import FastAPI, HTTPException
from comet import download_model, load_from_checkpoint
from pydantic import BaseModel
import time

# 모델 로딩
# HuggingFace의 SentenceTransFormer 라이브러리(e5, LaBSE 모델 사용)
model_e5 = SentenceTransformer('intfloat/multilingual-e5-large', device='cpu')
model_labse = SentenceTransformer('sentence-transformers/LaBSE', device='cpu')
# HuggingFace의 bert-score 패키지
model_bert = BERTScorer(
    model_type="xlm-roberta-base",
    lang="ko",                      # 토크나이저 설정을 위한 임시 값 
    # lang=target_lang,             # 사용자 번역 언어 입력 시 주석 제거 
    rescale_with_baseline=False,    # 언어별 가중치 설정 X
    idf=False                       # 언어별 가중치 설정 X
)
# Unbabel의 COMET 모델 사용
model_comet_path = download_model("wmt20-comet-qe-da")
model_comet = load_from_checkpoint(model_comet_path)

# FastAPI 앱 초기화
app = FastAPI(
    title="Text Similarity API",
    description="원문과 번역문간의 유사도 평가 API",
    version="1.0.0"
)

# 입력 데이터 모델 정의
class TextPair(BaseModel):
    source_text: str    # 원본 텍스트
    target_text: str    # 번역 텍스트

# E5, LaBSE Score
def get_similarity(model, sentence1, sentence2):
    embeddings = model.encode([sentence1, sentence2], convert_to_tensor=True)
    return util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()

# BERTScore
def get_bertscore(source_text, target_text):
    P, R, F1 = model_bert.score([target_text], [source_text])
    return P.item(), R.item(), F1.item()

# Comet Score
def get_comet_score(source_text, target_text):
    # COMET 스코어 계산 (최신 API 방식)
    data = [
        {
            "src": source_text,
            "mt": target_text,
        }
    ]
    model_output = model_comet.predict(data, batch_size=8, gpus=0)
    return model_output.system_score

# Score 임계값 설정
threshold_e5=0.8
threshold_labse=0.7
threshold_bert=0.8
threshold_comet=0.5

def evaluate_text_similarity(
        source_text, 
        target_text, 
        
    ):
    start = time.time()

    similarity_e5 = get_similarity(
        model_e5, 
        f"query: {source_text}", 
        f"passage: {target_text}"
        )

    similarity_labse = get_similarity(model_labse, source_text, target_text)
    P, R, F1 = get_bertscore(source_text, target_text)
    comet_score = get_comet_score(source_text, target_text)
    
    # description을 리스트로 초기화
    descriptions = [
        "Score Explanation:",
        " • E5: 문장 단위, 구절 등을 임베딩해 cosine similarity 측정",
        " • LaBSE: 문장 전체를 임베딩해 cosine similarity 측정",
        " • BERTScore: 각 단어들을 임베딩해 cosine similarity 측정",
        " • COMET: 사람 평가 기반 번역 품질 점수 측정"
    ]

    # e5, LaBSE 평가
    if similarity_e5 >= threshold_e5 and similarity_labse >= threshold_labse:
        descriptions.append(
            f"✅ 직역 가능성 높음 (E5: {similarity_e5:.2f} ≥ {threshold_e5}, "
            f"LaBSE: {similarity_labse:.2f} ≥ {threshold_labse})"
        )
    elif similarity_e5 >= threshold_e5:
        descriptions.append(
            f"✏️ 의역 가능성 있음 (E5: {similarity_e5:.2f} ≥ {threshold_e5}, "
            f"LaBSE: {similarity_labse:.2f} < {threshold_labse})"
        )
    elif similarity_labse >= threshold_labse:
        descriptions.append(
            f"📖 직역 유사성만 높음 (E5: {similarity_e5:.2f} < {threshold_e5}, "
            f"LaBSE: {similarity_labse:.2f} ≥ {threshold_labse})"
        )
    else:
        descriptions.append(
            f"⚠️ 의미 차이 큼 (E5: {similarity_e5:.2f}, LaBSE: {similarity_labse:.2f}); "
            "COMET score 확인 요망"
        )

    # BERTScore 평가
    if F1 >= threshold_bert:
        descriptions.append(
            f"👍 단어 단위 의미 유사도 우수 (BERTScore F1: {F1:.2f} ≥ {threshold_bert})"
        )
    else:
        descriptions.append(
            f"👎 단어 단위 의미 유사도 부족 (BERTScore F1: {F1:.2f} < {threshold_bert})"
        )

    # COMET 평가 추가
    if comet_score >= threshold_comet:
        descriptions.append(
            f"🎯 번역 품질 우수 (COMET: {comet_score:.2f} ≥ {threshold_comet})"
        )
    else:
        descriptions.append(
            f"❗️ 번역 품질 미흡 (COMET: {comet_score:.2f} < {threshold_comet})"
        )

    end = time.time()
    # 유사도 평가 소요시간
    execution_time = end - start

    # JSON 형식으로 결과 반환
    return {
        "source_text": source_text,
        "target_text": target_text,
        "e5_cosine_similarity": round(similarity_e5, 4),
        "labse_cosine_similarity": round(similarity_labse, 4),
        "bertscore": {
            "precision": round(P, 4),
            "recall": round(R, 4),
            "f1": round(F1, 4)
        },
        "comet_score": comet_score,
        "description" : descriptions,
        "execution_time_seconds": round(execution_time, 2)
    }

# Agent Controller
@app.post("/agent-text")
async def agent_controller(text_pair: TextPair):
    """
    원문과 번역문의 유사도를 평가합니다.
    
    - **source_text**: 원본 텍스트
    - **target_text**: 번역된 텍스트
    
    Returns:
        유사도 평가 결과 (JSON 형식)
    """
    try:
        result = evaluate_text_similarity(
            text_pair.source_text,
            text_pair.target_text
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

