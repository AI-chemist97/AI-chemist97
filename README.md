# Portfolio

backend 개발자 (희망)

새로운 것을 공부하거나 깊게 파는 것을 좋아하는 개발자입니다.

[![AI-Chemist97's GitHub stats](https://github-readme-stats.vercel.app/api?username=AI-chemist97&theme=radical&show_icons=true&count_private=true&hide=stars)](https://github.com/anuraghazra/github-readme-stats)

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=nyh1142)](https://solved.ac/nyh1142/)



# Project

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white), ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray), ![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D), ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white),
![Vuetify](https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=AEDDFF), ![Spring](https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)

## 영화 추천 알고리즘 사이트 만들기
* 일희무비
    * ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white), 	![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray), ![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D), ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)을 사용하였습니다.
    * 영화 api를 TMDB에서 받아와서 제작
        * axios를 이용하여 데이터를 받아오고 받아온 데이터에서 description을 기반으로 현재 선택한 영화와 유사한 영화를 추천해주는 알고리즘을 텍스트 유사도 함수를 이용하여 구현
```py
function termFreq(text) {
  const terms = text.split(/\s+/);
  const freq = {};
  terms.forEach(term => {
    if (freq[term]) {
      freq[term]++;
    } else {
      freq[term] = 1;
    }
  });
  return freq;
}

const dotProduct = (vec1, vec2) => {
  const terms = Object.keys(vec1);
  return terms.reduce((sum, term) => {
    if (vec2[term]) {
      return sum + vec1[term] * vec2[term];
    }
    return sum;
  }, 0);
};

const magnitude = (vec) => {
  return Math.sqrt(Object.values(vec).reduce((sum, val) => sum + val * val, 0));
};

function cosineSimilarity(text1, text2) {
  const freq1 = termFreq(text1);
  const freq2 = termFreq(text2);

  const numerator = dotProduct(freq1, freq2);
  const denominator = magnitude(freq1) * magnitude(freq2);

  return denominator ? numerator / denominator : 0;
}

export { cosineSimilarity };

```
* 계획: gpt api를 이용하여 gpt가 db를 돌면서 유사도를 평가해주는 기능
* 한계: gpt api를 이용하여 db에 접근하거나 prompt에 넣으려고 할 때 db의 사이즈가 커 들어가지 않고 빈 json 파일만 들어가는 경우가 많았음
* 해결: 오류를 줄이고자 글자에서 단어별로 유사한 정도를 추정하여 가장 유사한 영화부터 내림차순으로 정렬
    
<img alt="프로젝트 메인" src="/assets/01_movie/01_01_프로젝트메인01.png" width="500"/>

* 당시 프로젝트 이름은 일희movie
* 팀원분과 이름 한 글자씩 합친 것

<img alt="프로젝트 메인" src="/assets/01_movie/01_02_프로젝트메인02.png" width="500"/>

* 메인페이지로 bootstrap을 이용한 carousel을 통해 인기 영화 리스트에서 5개 뽑아와서 3초가 지나면 다음 목록을 보여주게 구현
* 영화를 클릭시 해당 영화의 상세페이지로 이동
* 아래 작은 크기의 리스트는 5개씩 자동으로 시간이 지날때마다 움직임, 당시 carousel을 중첩해서 사용
  
<img alt="인기있는 영화" src="/assets/01_movie/01_03_인기있는영화.png" width="500"/>


<img alt="프로젝트 메인" src="/assets/01_movie/01_02_프로젝트메인02.png" width="500"/>
<img alt="검색창" src="/assets/01_movie/01_04_검색창.png" width="500"/>
<img alt="영화 상세창" src="/assets/01_movie/01_05_영화상세창.png" width="500"/>
<img alt="유튜브 미리보기창" src="/assets/01_movie/01_06_유튜브미리보기창.png" width="500"/>
<img alt="ai키워드ai요약" src="/assets/01_movie/01_07_ai키워드ai요약.png" width="500"/>
<img alt="유사한 영화추천" src="/assets/01_movie/01_08_유사한영화추천.png" width="500"/>
<img alt="자동 carousel" src="/assets/01_movie/01_09_자동carousel.png" width="500"/>
<img alt="회원가입" src="/assets/01_movie/01_10_회원가입.png" width="500"/>
<img alt="로그인" src="/assets/01_movie/01_11_로그인.png" width="500"/>

![유튜브검색](image-11.png)
![회원가입 체크박스](image-12.png)
![게시글 목록](image-13.png)
![게시글 생성](image-14.png)
![댓글 달기](image-15.png)
![댓글 수정](image-16.png)
![마이페이지](image-17.png)
![게시글 수정](image-18.png)

최근 완료 후 ui가 너무 기능 중심인 것 같아 수정 중이다.
* 백, 프론트 구분없이 협업.
* AI 연결 진행



1. 학생들의 문해력 향상을 위한 학습 게임 만들기
    * ![Vuetify](https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=AEDDFF), ![Spring](https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)
    * 프론트 담당
    * 초기 다들 게임 개발은 처음이라 시도하던 중, three.js를 너무 잘 해서 게임 개발 담당으로 정해졌습니다.
        * 담당이 된 후 sketchfab에서 표기할 경우 상업적으로도 사용이 가능한 캐릭터들 중 애니메이션을 가진 캐릭터들을 선별하였고, 그 중 하나를 임포트 하여 개발을 시작하였습니다.
병아리
고양이
쥐
....
링크



