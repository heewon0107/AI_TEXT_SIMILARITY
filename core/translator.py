# GOOGLE CLOUD TRANSLATOR
# 439,991 remain
import requests
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# .env 파일에서 API_KEY 로드
load_dotenv(dotenv_path = "../config/.env")
API_KEY = os.getenv("GOOGLE_TRANSLATOR_API_KEY")

# Fast API
app = FastAPI(title = "Google Cloud Translator API Wrapper")

# 요청 스키마 정의
class TranslateRequest(BaseModel):
    source_lang: str    # 원본 언어
    target_lang: str    # 번역 언어
    source_text: str    # 원본 텍스트

# 에이전트 설정
AGENT_URL = os.getenv("AGENT_URL")

# 엔드포인트 설정
@app.post("/translate-google")
def translate(request: TranslateRequest):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": request.source_text,
        "target": request.target_lang,
        "key": API_KEY
    }
    google_response = requests.post(url, params=params)

    # 에러 응답 예외처리
    if not google_response.ok:
        raise HTTPException(
                status_code=google_response.status_code, 
                detail=google_response.text
                )
    
    # 번역 텍스트 에이전트 요청
    google_data = google_response.json()
    translated_text = google_data["data"]["translations"][0]["translatedText"]
    agent_payload = {
        "source_lang": request.source_lang, # 원본 언어
        "target_lang": request.target_lang, # 번역 언어
        "source_text": request.source_text, # 원본 텍스트
        "target_text": translated_text      # 번역 텍스트
    }
    # 에이전트 API 호출
    agent_response = requests.post(AGENT_URL, json=agent_payload)
    if not agent_response.ok:
        raise HTTPException(status_code=agent_response.status_code, detail=agent_response.text)
    return agent_response.json()

    
