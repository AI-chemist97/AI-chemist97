# 👋 안녕하세요, AI-Chemist97 남윤희입니다. (Hi, I'm Yunhee Nam, AI-Chemist97)
### AI/Data Engineer | Industrial Big Data Specialist

- **[KR]** 화학/재료공학 석사의 도메인 지식과 SSAFY에서 다진 SW 엔지니어링 역량을 바탕으로, 제조 현장의 대규모 공정 데이터를 분석하고 확장 가능한 ML 파이프라인을 설계합니다.
- **[EN]** A Data Engineer with a **Master's in Materials Chemistry & Engineering**, bridging deep chemical domain knowledge and high-throughput **Industrial Data Engineering (6B+ rows)**.

- **[KR]** 석사 과정 중 화학물질 검출·나노복합체 연구로 ScienceDirect 등재 저널 **JIEC**에 제1저자 논문을 게재했습니다.
- **[EN]** First-authored a paper in **JIEC** (Journal of Industrial and Engineering Chemistry, ScienceDirect) on chemical detection with nanocomposites during my master's.
  - *"Effective hydroquinone detection using a manganese stannate/functionalized carbon black nanocomposite"*

- **[KR]** AI 스타트업에서 60억 건 이상의 산업 데이터를 다루며, 데이터 신뢰성을 검증하고 분석 효율을 높이는 일을 했습니다.
- **[EN]** At an AI startup, handled 6B+ rows of industrial data, validating data reliability and maximizing analysis efficiency.

* **Email:** `nyh1142@gmail.com`
* **Blog:** https://ai-chemist97.github.io/

---

## 🧪 AI-Chemist97 이름에 담긴 의미 (Identity)

- **[KR]** 전공인 화학(Chemist)과 지금의 전문 분야인 AI를 결합한 이름입니다. 화학물질 독성 예측(Tox21)과 유전자 데이터 분석 프로젝트로 데이터 커리어를 시작했습니다.
- **[EN]** Combines my major, **Chemistry**, with my current field, **AI**. I started my data career with projects like Tox21 and genomic data analysis.
- **[KR]** 영어 **alchemist(연금술사)**와 발음이 비슷해, 로우 데이터를 정제해 비즈니스 가치로 바꾸는 전문가가 되겠다는 포부도 담았습니다.
- **[EN]** It also sounds like **'alchemist'**, reflecting my goal to turn raw data into valuable business insights.

---

## 🛠️ 주요 성과 (Core Professional Impact) — @ Domain-Specific AI Startup

### **1. 설비-센서 종속성 규명을 통한 6.1B Rows 파이프라인 최적화 (6.1B-Row Pipeline Optimization)**
- **[KR]** 동료 엔지니어들이 파악하지 못했던 장비-센서 간 종속성과 중복 구조를 도메인 지식으로 규명했습니다. 불필요한 센서 데이터를 제거하고 61억 건의 공정 로그 처리 로직을 재구성해 **전처리 시간을 24시간에서 2시간으로 91% 단축**했습니다.
- **[EN]** Identified undocumented sensor-equipment dependencies and redundancies. By removing unnecessary sensor data and restructuring the logic for 6.1 billion rows, **cut preprocessing time by 91% (24h → 2h)**.

### **2. 데이터 무결성 검증 및 대외 리스크 차단 (Data Integrity)**
- **[KR]** 실무 데이터와 기존 답안 간의 불일치를 포착하고 정밀 재검증해 **대기업 거래처 오보고 리스크를 선제적으로 차단**했습니다. (기존 신뢰도 90% → 실제 정합성 20% 확인)
- **[EN]** Caught critical discrepancies between operational data and reference sets and re-validated them, **preventing misreporting risks to Tier-1 clients** (assumed 90% reliability → 20% actual consistency).

---

## 🤖 AI 기반 개인 프로젝트 (AI-Powered Side Projects, 2026)

> **[KR]** Claude Code를 페어 엔지니어로 두고 설계부터 실운영까지 직접 만들고 있습니다. AI로 빠르게 만들고, 결과가 좋아 보일수록 먼저 의심합니다.
>
> **[EN]** I build from design to live operation with Claude Code as a pair engineer. Build fast with AI; the better a result looks, the harder I question it.

### **1. 주식 자동매매 봇 (Automated Trading Bots) — 국내 / ISA / 스윙 / 미국 (KR / ISA / Swing / US)**

[![Trading Scoreboard](https://raw.githubusercontent.com/AI-chemist97/trading-scoreboard/main/card.svg)](https://ai-chemist97.github.io/scoreboard/)

- **[KR]** 증권사 API로 시세를 받고 **LightGBM**으로 종목별 수익률을 예측, **Optuna**로 튜닝하고 **SHAP**으로 근거를 해석합니다. Docker 컨테이너로 24시간 운영하며 매일 텔레그램으로 리포트를 받습니다.
- **[EN]** Pulls market data via brokerage APIs, predicts per-stock returns with **LightGBM**, tunes with **Optuna**, and explains predictions with **SHAP**. Runs 24/7 in Docker with daily Telegram reports.
- **[KR]** 백테스트 수익률이 비정상적으로 높은 것을 의심해 추적한 결과, **$0.5 미만 초저가 종목의 체결 불가능한 거래**가 평균 거래 수익률을 **3.33% → 43.61%**로 부풀리고 있음을 찾아 교정했습니다.
- **[EN]** Suspicious of an unusually high backtest, traced it to **untradeable sub-$0.5 stocks** inflating the average trade return from **3.33% to 43.61%**, and corrected it.
- **[KR]** 운영 중 크래시 4건과 API 레이트리밋(시간당 100건+ → 거의 0건)을 해결했고, KRX 호가단위(매수 올림 / 매도 내림)를 반영했습니다.
- **[EN]** Fixed 4 production crashes, cut API rate-limit hits from 100+/hour to near zero, and applied KRX tick-size rounding (round up on buys, down on sells).

### **2. yt-factory — 쇼츠 영상 자동 생성 파이프라인 (Automated Shorts Pipeline)**
- **[KR]** **Gemini**로 매일 새 주제의 대본을 만들고 **edge-tts**로 음성을 입혀 배경·자막을 합성한 뒤 텔레그램으로 받아봅니다.
- **[EN]** Generates a fresh script daily with **Gemini**, narrates it with **edge-tts**, composes background and subtitles, and delivers the video via Telegram.
- **[KR]** 유료 TTS와 로컬 TTS를 비교해, 매일 자동 생성 구조에 맞는 무료 TTS로 **운영비 0원** 구조를 설계했습니다. 현재 유튜브에 비공개로 업로드하며 영상 품질을 개선하고 있고, 공개 자동 업로드를 준비하는 단계입니다.
- **[EN]** Compared paid and local TTS options and chose free TTS that fits daily automation, designing for **zero running cost**. Now uploading privately to YouTube while improving video quality, preparing for public auto-upload.

---

## 🚀 주요 프로젝트 (Featured Projects)

### **1. 췌장암 예측 모델 (Pancreatic Cancer Prediction, GSE16515)**
- **[KR]** Affymetrix U133 Plus 2.0 칩 기반 고차원 유전자 데이터에서 미탐(FN)을 최소화하기 위해 `class_weight` 튜닝과 재현율 최적화 실험을 진행하고, `feature_importances_`로 고위험군 분류 기준을 해석했습니다.
- **[EN]** Minimized **false negatives (FN)** on high-dimensional Affymetrix U133 Plus 2.0 genomic data through `class_weight` tuning and recall optimization, interpreting high-risk classification with RF feature importance.
- [🔗 GitHub Repository](https://github.com/AI-chemist97/003_Genomics_Omics_Project)

### **2. 화학물질 독성 예측 (Chemical Toxicity Prediction, Tox21)**
- **[KR]** **RDKit**으로 분자 특성을 추출해 수백 개 규모의 피처를 만들고, 결정트리 시각화로 독성 판단 규칙을 해석했습니다.
- **[EN]** Engineered hundreds of molecular descriptors with **RDKit** and interpreted toxicity rules through decision tree visualization.
- [🔗 GitHub Repository](https://github.com/AI-chemist97/001_TOX21_Chemical_Toxicity_Prediction)

### **3. 학과방 (Gwabang) — 학과 기반 커뮤니티 (Department-Based Community)**
- **[KR]** SSAFY 수료 후 최신 기술 스택을 유지하려고 오픈카톡으로 팀원을 모아 진행한 프로젝트입니다. Spring Boot 3.4, React 19, JPA/JWT로 학과별 커뮤니티 서비스를 구현했습니다.
- **[EN]** A team project recruited via open chat after SSAFY to keep my stack current; built a department-based community with Spring Boot 3.4, React 19, and JPA/JWT.
- [🔗 GitHub Repository](https://github.com/AI-chemist97/gwabang)

### **4. 일희무비 / 링고랜드 (Ilhee Movie / Lingoland, SSAFY Projects)**
- **[KR]** Django/Spring, Vue/Three.js로 백엔드 API 설계부터 프론트엔드 개발까지 전체 흐름을 구현하며 웹 서비스 구조를 익혔습니다.
- **[EN]** Built full-stack web services end to end, from backend API design to frontend, with Django/Spring and Vue/Three.js during SSAFY.
- [🔗 SSAFY Projects Repo](https://github.com/AI-chemist97/SSAFY_projects) | [🔗 Lingoland Repo](https://github.com/AI-chemist97/lingoland)

### **5. Jobby — 자기소개 챗봇 (Portfolio Chatbot)** · ⏸️ 서비스 일시 중단 (Temporarily Unavailable)
- **[KR]** 자기소개, 전공/경력, SSAFY/프로젝트를 대화형으로 확인할 수 있는 챗봇입니다. 현재 서비스를 잠시 중단했습니다.
- **[EN]** A conversational chatbot for exploring my background, major, career, and projects. The service is temporarily offline.
- **Stack:** React, Node.js (Express), Dialogflow

---

## 🛠️ 보유 기술 (Tech Stack)

### 1. 데이터 분석 & 머신러닝 (Data Analysis & ML)

* **Language:** Python (Advanced), SQL
* **Data Handling:** pandas, numpy, Parquet optimization
* **ML & Analysis:** scikit-learn (LogisticRegression, RandomForest, etc.), preprocessing/scaling, class imbalance (`class_weight`), PCA
* **ML Ops & Automation:** LightGBM, Optuna, SHAP, Docker, Telegram Bot API
* **Domain-Specific:** RDKit (Cheminformatics), genomics/omics data
* **Visualization:** matplotlib, seaborn
* **AI Tools:** Claude Code, Claude, GPT, Gemini

### 2. 백엔드 & 웹 (Backend & Web)

* **Frameworks:**
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
  ![Spring](https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)

* **Frontend:**
  ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
  ![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
  ![Vuetify](https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=AEDDFF)

* **Game/Interactive:** Three.js

---

## 🔭 앞으로 해볼 계획 (What's Next)

- **[KR]** 반도체 공정 로그·센서 데이터를 활용한 시계열 예측·이상탐지 프로젝트를 이어갈 예정입니다.
- **[EN]** Continue time-series forecasting and anomaly detection on semiconductor process logs and sensor data.

---

## 📈 Stats & Connect

[![AI-Chemist97's GitHub stats](https://github-readme-stats-two-pearl-36.vercel.app/api?username=AI-chemist97&theme=radical&show_icons=true&count_private=true&hide=stars)](https://github.com/anuraghazra/github-readme-stats)
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=nyh1142)](https://solved.ac/nyh1142/)

* **Email:** nyh1142@gmail.com
* **Blog:** https://ai-chemist97.github.io/
