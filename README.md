# 👋 안녕하세요, AI-Chemist97입니다.

화학/재료 공학 석사에서 공부한 내용과 SSAFY에서 경험한 웹/백엔드 개발을 바탕으로,  
데이터 분석과 머신러닝을 차근차근 공부하고 있습니다.

- 석사 과정에서 화학물질 독성 예측 관련 연구를 진행했고,  
  ScienceDirect에 등재된 논문  
  “Efficiency of pharmaceutical toxicity prediction in computational models and in-vitro models”의 제1저자로 참여했습니다.

* **Email:** `nyh1142@gmail.com`  
* **Blog:** https://ai-chemist97.github.io/

---

### 🧪 AI-Chemist97 이름에 담긴 의미

- **AI-Chemist**  
  - 전공은 화학·재료 공학이고, 화학물질 독성 예측(Tox21)과 유전자 데이터(췌장암 GSE16515) 같은 주제를 다뤄 본 경험이 있습니다.  
  - 이런 배경을 바탕으로 데이터를 분석하고, AI/머신러닝을 적용하는 일을 더 깊게 해 보고 싶어 AI와 Chemist를 함께 쓰고 있습니다.  
  - 영어로 보면 alchemist(연금술사)와 비슷하게 보여서, 실험·모델·코드들을 섞어 보면서 조금씩 배워 간다는 의미도 담았습니다.

---

## 💬 Interactive Portfolio Chatbot - Jobby

> 나에 대해 궁금한 건, 이제 조비에게 물어보세요.

- 바로 써보기: https://jobby-henna.vercel.app/  
- Stack: React, Node.js(Express), Dialogflow  
- 자기소개, 전공/경력, SSAFY/프로젝트, 데이터/ML 공부 방향 등을 대화형으로 볼 수 있도록 만든 포트폴리오용 챗봇입니다.

---

[![AI-Chemist97's GitHub stats](https://github-readme-stats.vercel.app/api?username=AI-chemist97&theme=radical&show_icons=true&count_private=true&hide=stars)](https://github.com/anuraghazra/github-readme-stats)  
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=nyh1142)](https://solved.ac/nyh1142/)

---

## 🛠️ 보유 기술 (Tech Stack)

### 1. 데이터 분석 & 머신러닝 (Data Analysis & ML)

* **Language:** Python  
* **Data Handling:** pandas, numpy  
* **ML & Analysis:** scikit-learn  
  - 분류/회귀 (LogisticRegression, RandomForest 등)  
  - 전처리/스케일링, 클래스 불균형(class_weight) 처리, PCA  
* **Domain-Specific:** RDKit (Cheminformatics), 유전자/오믹스 데이터 처리  
* **Visualization:** matplotlib, seaborn  

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

## 🚀 대표 프로젝트 (Featured Projects)

### 1. 췌장암 예측 모델 (GSE16515)

* **[Data Analysis] [Bioinformatics]**  
* GEO 췌장암 유전자 발현 데이터 GSE16515(종양 36건, 정상 16건, 총 52샘플)를 사용했습니다.  
* Affymetrix U133 Plus 2.0 칩 기반 데이터로, 약 5만 개 유전자 프로브 중 중요한 특징들을 중심으로 분류 모델을 구성했습니다.  
* 초기 모델에서 암 환자를 놓치는 사례(FN=1)가 나오는 문제를 확인했고,  
  암 환자를 놓치지 않는 방향으로 class_weight를 조정해 재현율(Recall)을 올리는 실험을 진행했습니다.  
* feature_importance_를 활용해 모델이 주목한 유전자를 확인하고,  
  어떤 특징 조합에서 고위험군으로 분류되는지 해석하는 데 집중했습니다.  
* ➡️ GitHub Repository: https://github.com/AI-chemist97/003_Genomics_Omics_Project  

---

### 2. 화학물질 독성 예측 (Tox21)

* **[Data Analysis] [Cheminformatics]**  
* Tox21 독성 예측 데이터에서 약 1만 2천 개 수준의 화합물 데이터를 사용해,  
  각 화합물의 독성(여러 타깃에 대한 활성 여부)을 예측하는 이진 분류 문제로 다뤘습니다.  
* RDKit으로 분자 특성을 추출해 수백 개 규모의 분자 기술자치(피처)를 만들고,  
  데이터 불균형 문제는 언더샘플링을 통해 어느 정도 완화했습니다.  
* 로지스틱 회귀에서 성능이 충분하지 않아 결정트리 모델로 바꿔 보면서,  
  성능과 해석 가능성을 함께 비교했습니다.  
* export_graphviz로 의사결정 트리를 시각화해,  
  어떤 규칙이 독성 판단에 영향을 주는지 살펴보는 과정을 포함했습니다.  
* ➡️ GitHub Repository: https://github.com/AI-chemist97/001_TOX21_Chemical_Toxicity_Prediction  

---

### 3. 학과방 (Gwabang) - 학과 기반 커뮤니티

* **[Post-SSAFY Project] [Full-Stack]**  
* SSAFY 수료 후, 최신 기술 스택을 계속 써 보기 위해 오픈카톡으로 팀원을 모집해서 진행한 프로젝트입니다.  
* Spring Boot 3.4, React 19, JPA/JWT를 사용해 학과별 커뮤니티 서비스를 구현했습니다.  
* ➡️ GitHub Repository: https://github.com/AI-chemist97/gwabang  

---

### 4. 일희무비 / 링고랜드 (SSAFY Projects)

* **[SSAFY Foundation] [Backend]**  
* SSAFY 교육 과정 중 Django/Spring, Vue/Three.js를 사용한 팀 프로젝트를 경험했습니다.  
* 백엔드 API 설계와 프론트 개발을 함께 맡으면서, 웹 서비스 전체 플로우를 익혔습니다.  
* ➡️ GitHub Repository: https://github.com/AI-chemist97/SSAFY_projects  
* ➡️ GitHub Repository: https://github.com/AI-chemist97/lingoland  

---

## 🔭 앞으로 해볼 계획

- 반도체 공정 로그, 센서 데이터, 주식 시계열을 활용한  
  시계열 예측·이상탐지 프로젝트를 Python/ML 기반으로 진행해 볼 예정입니다.  
- Python → EDA → SQL → ML 순서로 공부 내용을 정리하면서,  
  여기에서 나온 결과들을 포트폴리오 프로젝트로 계속 확장해 볼 생각입니다.
