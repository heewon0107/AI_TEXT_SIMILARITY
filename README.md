#  AI 더빙 평가 에이전트 - SyncMonster

## 📂 프로젝트 소개
다국어 음성 더빙 유사도를 정밀하게 분석하고 평가하는 AI 더빙 평가 시스템 <br>

## 📅 프로젝트 수행 기간
- 2025-04-14 ~ 2025-05-22

## 🧑‍🚀 팀원 소개

|                             [황치운](https://github.com/HwangCU)                            |                           [이수정](https://github.com/SooJ2)                           |                             [조윤장](https://github.com/dbswkd76)                            |                            [신희원](https://github.com/heewon0107)                            |                             [정재현](https://github.com/hyeonjaez)                             |                             [정찬환](https://github.com/chanhoan)                             |
| :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: |
| <img src="https://avatars.githubusercontent.com/u/118156229?v=4" width="100" height="100"> | <img src="https://avatars.githubusercontent.com/u/64190044?v=4" width="100" height="100"> | <img src="https://avatars.githubusercontent.com/u/77269556?v=4" width="100" height="100"> | <img src="https://avatars.githubusercontent.com/u/175683567?&v=4" width="100" height="100"> | <img src="https://avatars.githubusercontent.com/u/50399586?v=4" width="100" height="100"> | <img src="https://avatars.githubusercontent.com/u/44390830?v=4" width="100" height="100"> |
|                                     팀장 & AI                                     |                                        Frontend                                       |                                          AI                                          |                                       AI                                      |                                          Backend                                          |                                          Backend                                          |


<br><br>
## 🔧 사용 스택

### **FrontEnd** <br>
<span>
<img src="https://img.shields.io/badge/React-02569B?style=for-the-badge&logo=react&logoColor=white">
<img src="https://img.shields.io/badge/Node.js-3DDC84?style=for-the-badge&logo=node.js&logoColor=white"/>
</span>
    
### **BackEnd** <br>
<span>
<img src="https://img.shields.io/badge/Java 17-007396.svg?&style=for-the-badge&logo=Java&logoColor=white">
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/JPA-F3702A?style=for-the-badge&logo=jpa&logoColor=white"/>
<img src="https://img.shields.io/badge/gradle-02303A?style=for-the-badge&logo=gradle&logoColor=white"/>
<img src="https://img.shields.io/badge/springboot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white"/>
<img src="https://img.shields.io/badge/fastapi-F7931E?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
</span>

### **AI** <br>
<span>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/pytorch-F7931E?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/cuda-4479A1?style=for-the-badge&logo=cuda&logoColor=white"/>
<img src="https://img.shields.io/badge/huggingface-3DDC84?style=for-the-badge&logo=huggingface&logoColor=white"/>
<img src="https://img.shields.io/badge/transformers-02303A?style=for-the-badge&logo=transformers&logoColor=white"/>
</span>

### **Infra** <br>
<span>
<img src="https://img.shields.io/badge/amazon EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white"/>
<img src="https://img.shields.io/badge/amazon s3-569A31?style=for-the-badge&logo=amazons3&logoColor=white"/>
<img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white"/>
<img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
</span>

<br>

## 📢 기능 요약

#### [AI 더빙 평가 에이전트 시스템]

**1. 음성 합성 및 음질 평가**
- Multi-lingual TTS 모델 기반 음성 합성
- MOS (Mean Opinion Score) 평가: UTMOS 등 모델을 활용한 음질 정량 평가
- Speaker Consistency 평가: 원본 음성과 합성 음성 간 화자 일관성 점수 (SC Score) 산출

**2. 합성 음성과 원본 음성 간 유사도 평가**
- 음성-텍스트 정렬(Alignment) 수행
- Vowel, Pause, Silence 기반 Isochrone Score 산출: 시간 정렬 기준 발음 간 동기화 유사도 평가
- 원본 및 번역 음성 간 정합성 측정

**3. 텍스트 번역 및 유사도 평가**
- 다국어 신경망 기계번역(NMT) 기반 약 Multi-lingual 번역
- 원문과 번역문 텍스트 유사도 평가 및 Similarity Score 산출(E5, LaBSE, BERT, COMET)
- 입력/번역 텍스트 간 직역/의역 평가 후 Score 기반 피드백 
- 관용어, 초월번역을 위한 재번역 피드백 루프 제공

**4. 통합 에이전트 시스템**
- 위 3가지 에이전트를 통합한 시스템 구축
- 각 에이전트를 모듈화하여 분산처리 및 병렬처리 가능
- 사용자 친화적 UI


<br>

## 🧙 평가 에이전트 

**[텍스트 번역 및 유사도 평가 에이전트]**
- 영화 대사 데이터셋을 학습해 구어체 및 숙어 등 자연스러운 번역
- Transformer 기반 Multi-lingual 임베딩 모델을 활용한 다국어 텍스트 의미 유사도 분석
- 의역/직역 평가 및 텍스트 Similarity Score를 제공해 번역 품질 평가 및 사용자의 재번역 여부 결정에 도움 
- 번역 정확성 및 의미 보존 여부를 정밀하게 평가할 수 있어, 콘텐츠 현지화 품질을 향상시킴

**[음성 합성 및 음질 평가 에이전트]**
- UTMOS 기반의 객관적 MOS 점수 산출로 음성 합성 품질을 자동 평가
- 화자 일관성(Speaker Consistency)까지 측정하여, 더빙 품질의 핵심 요소까지 정량적으로 분석 가능

**[원본/합성 음성 유사도 평가 에이전트]**
- 원본 및 번역 음성 간의 Vowel, Pause, Silence 정렬을 기반으로 한 Isochrone Score 제공
- 단순 청취 평가를 넘어 발화 구조의 유사성을 수치로 표현

**[통합 에이전트 시스템]**
- 음질, 음성 정렬, 번역 유사도 에이전트를 모듈화하여 독립 실행 및 병렬 처리 가능
- 향후 추가 평가 지표나 언어 확장도 유연하게 대응 가능
- 사용자 친화적 평가 시스템 UI
- 평가 결과를 시각적으로 확인할 수 있는 UI 제공
- 누구나 손쉽게 평가 지표를 해석하고 더빙 퀄리티를 비교 가능

<br>

## 🎁 프로젝트 구성

### 1. 아키텍쳐
![architecture](./img/architecture.png)

### 2. ERD
![erd](./img/erd.png)
자세한 내용은 [테이블 정의서](https://www.erdcloud.com/d/RuqyFnsygFEjrCraC)에 정리해두었습니다

<br>

## 🌈 AI 기능

 **Multi-lingual TTS(Text-to-Speech) 모델**
 - 다양한 언어로 텍스트를 자연스러운 음성으로 변환하는 딥러닝 기반 음성 합성 기술

 **UTMOS(Universal Text-to-speech Mean Opinion Score)**
 - 합성된 음성의 품질을 자동으로 평가하는 딥러닝 모델

 **화자 임베딩(Speaker Embedding) 기술**
 - 화자의 음성 특성을 추출하여 벡터 공간에 표현하는 기술

 **음성-텍스트 강제 정렬(Forced Alignment) 알고리즘**
 - 음성과 텍스트의 시간적 대응 관계를 자동으로 맵핑하는 기술

 **Google Trasnlator API**
 - 의역 및 장문 번역해주는 AI 기술

 **M2M100_418M(Transformer 기반 Multi-lingual 기계번역 딥러닝 NMT)**
 - 영어-비영어, 비영어-비영어 번역을 위해 파인튜닝 

 **OpenAI GPT-4.1-nano (Chat Completions API)**
 - 시네마틱 프롬프트 기반 대화형 언어모델 관용 표현 및 초월 번역에 활용

 **E5, LaBSE(Transformer 기반 Multi-lingual 문장 임베딩 모델)**
 - 문장 단위나 구조, 전체 문장의 의미 유사도를 평가 기술

 **BERTScore (Transformer 기반 토큰 임베딩 평가 메트릭)**
 - 원문, 번역문의 각 토큰 간 cosine similarity 점수를 평가하는 기술

 **COMET (Transformer 기반 MT 품질 예측 메트릭)**
 - 원문과 번역문을 사람이 매긴 DA/MQM 점수를 통해 번역 품질을 평가하는 기술

 **멀티모달 데이터 통합 처리**
 - 음성, 텍스트 등 다양한 형태의 데이터를 통합적으로 처리하는 AI 기술

<br>

## 🤖 기본 요구사항

**텍스트 번역/재번역 및 유사도 평가 에이전트**
- 원문 스크립트를 번역하고, 원문과 번역문의 의미 유사도를 평가(BERTScore)

**음성 합성 에이전트**
- 번역 텍스트 기반 TTS 합성 (예: XTTS v2, Google TTS, CLOVA 등 활용)

**정렬(Alignment) 에이전트**
-원본 음성과 번역 음성 간 발화 타이밍 정렬 (prosodic alignment 방식 적용)

**음질 평가 에이전트**
- MOS(UTMOSv2), SC(ECAPA-TDNN) 기반 평가

**음성 유사도 평가 에이전트**
- pause/vowel 기준의 음성 타이밍 유사도 평가

**에이전트 통합 자동화 시스템**
- 평가를 자동화 구성

<br>

## 👽 추가 개발 사항
 
**UI/UX 시스템**
- 위 기능들을 시각적으로 활용 가능한 사용자 인터페이스 제공

**OpenAPI를 활용한 재번역**
- 구어체, 인용구, 은어 등을 포함한 재번역

**영상 음성 추출**
- 대상화자기반 영상에서 화자 음성 추출

**STT기능 추가**
- 화자 음성을 기반으로 Text 생성

**다국어 모델 추가**
- Multi-lingual 번역 모델을 사용해 다국어 번역

**유사도 평가 에이전트 개선**
- E5, LaBSE, Comet Score를 추가해 직역/의역/사람평가 Score를 피드백 루프에 추가

**관용 표현 및 초월 재번역 추가**
- Open AI의 시네마틱 Prompting으로 감정, 뉘앙스, 문화적 맥락 보존 번역

<br>

## 👻 UI/UX
![시연 이미지](./img/example.gif)
