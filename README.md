<div align='center'>
    <img src='./readme/image1.png'/>  

    💻삼성 청년 SW 아카데미 관통 프로젝트💻
    금융 상품 통합 비교 및 추천 서비스
</div>

## 메인 기능
**1. 금융 상품 비교**   
    예금, 적금, 대출 상품을 한 눈에 확인하고 비교할 수 있습니다.  
    <img src='./readme/image2.png' height='350px'/>   
    <img src='./readme/image3.png' height='350px'/> 

**2. 환율 계산**  
    환율 API가져와서 환율 계산 가능  
    <img src='./readme/image4.png' height='350px'/> 

**3. 지도 보기**  
   지도에서 가장 가까운 은행을 검색할 수 있습니다.  
   <img src='./readme/image5.png' height='350px'/>   
   지도를 옮겨가며 현 지도에서 검색하고, 상세정보를 확인할 수 있습니다.  

**4. 상품 추천**  
    사용자에게 자산과 연소득 정보를 입력받아, 금융 상품을 추천합니다.  
    <img src='./readme/image6.png' height='350px'/>  


## 기술 스택
#### BackEnd
<div display='flex'>
    <img src="https://img.shields.io/badge/django-174435?style=for-the-badge&logo=Django&logoColor=white">
    <img src="https://img.shields.io/badge/Python-black?style=for-the-badge&logo=Python&logoColor=white">
</div>


#### FrontEnd
<div display='flex'>
    <img src="https://img.shields.io/badge/Vue.js-6fb486?style=for-the-badge&logo=Vue.js&logoColor=3a4f63">
    <img src="https://img.shields.io/badge/Vite-white?style=for-the-badge&logo=vite&logoColor=9e77f5">
    <img src="https://img.shields.io/badge/JavaScript-f7e025?style=for-the-badge&logo=JavaScript&logoColor=black">
    <img src="https://img.shields.io/badge/bootstrap-white?style=for-the-badge&logo=bootstrap&logoColor=6514dd">
</div>

#### 협업
<img src="https://img.shields.io/badge/git.js-black?style=for-the-badge&logo=Git">

## 팀원

|[![](https://github.com/gimezi.png?width=5px)](https://github.com/gimezi) |[![](https://github.com/alpapago.png?width=5px)](https://github.com/alpapago)|
|:---:|:---:|
| 예지 | 신애 |


## 프로젝트 돌리기
### BackEnd 
(env파일 추가)
`python -m venv venv`
`source venv/Scripts/activate`
`pip install -r requirements.txt`
`python manage.py migrate`
`python manage.py runserver`

### FrontEnd
`npm install`
`npm run dev`