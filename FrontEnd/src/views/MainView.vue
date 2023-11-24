<template>
    <div class="mainpage">
        <!-- 메인이미지 -->
        <div id="carouselExampleIndicators" class="carousel slide container" style="margin: 0;"> 
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            </div>
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src='@/assets/images/image1.PNG' class="carousel-img" alt="image1">
                </div>
                <div class="carousel-item col-12">
                    <img src='@/assets/images/main_image.gif' class="carousel-img" alt="main">
                </div>
                
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
        <div class="sub-contents">
            <div class="main-article">
                <div style="display: flex; justify-content: space-between;">
                    <h3>자유게시판</h3>
                    <RouterLink :to="{ name : 'ArticleView' }" class="go-article">바로가기  <i class="fa-solid fa-arrow-right-to-bracket"></i></RouterLink>
                </div>
                <table class="col-2">
                    <thead>
                        <tr>
                            <th class="article-table-title">글 제목</th>
                            <th>작성자</th>
                            <th>작성일</th>
                        </tr>
                    </thead>
                    <tbody >
                        <tr v-if="store.articles" v-for="article of store.articles.slice(0,3)" :key="article.id">
                            <td class="article-table-title"><RouterLink :to="{ name:'DetailView', params: { id: article.id } }" style="color: black;">{{ article.title }}</RouterLink></td>
                            <td>{{ article.user.nickname }}</td>
                            <td>{{ dayjs(article.created_at).format('YY.MM.DD HH.mm') }}</td>
                        </tr>
                        <tr v-else>아직 작성된 글이 없습니다.</tr>
                    </tbody>
                </table>
                
            </div>
            <div class="banners">
                <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img @click="gobanking()" src="@/assets/images/banner1.png" class="banner-image d-block w-100" alt="금융상품 이미지" style="border-radius: 10px;">
                        </div>
                        <div class="carousel-item">
                            <img @click="gorecommend()" src="@/assets/images/banner2.png" class="banner-image d-block w-100" alt="추천 알고리즘 이미지" style="border-radius: 10px;">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import dayjs from 'dayjs'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()

const gobanking = function() {
    router.push({name: 'BankingView', params: {content : 'deposit'}})
}
const gorecommend = function() {
    router.push({name: 'RecommendationView'})
}

</script>

<style scoped>
.mainpage {
    width: 100%;
}
.carousel{
    margin: 0 auto !important;
}
.carousel-item {
    width: 100%;
}
.carousel-img{
    width: 100%;
}
.sub-contents {
    margin: 50px auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
}
.main-article {
    width: 45%;
}
.go-article {
    padding-top: 20px;
    margin-right: 70px;
    color: black;
    text-decoration: none;
}
.go-article:hover {
    color: #ddd;
}
.article-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 50px;
    /* padding: 20px; */
}
.article-list-title {
    text-align: center;
    color: grey;
    margin-bottom: 30px;
}
table {
    min-height: 150px;
    width: 90%;
    border-collapse: collapse;
    margin: 10px;
    border-radius: 10px;
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1) !important;
}

th, td {
  text-align: center;
  padding: 5px;
  border-bottom: 1px solid #ddd;
}

table thead {
  background-color: #f9e9a9; /* 배경색 */
  font-size: 15px;
}

table thead th {
  padding: 10px; /* 패딩 */
}

tbody tr:hover {
  background-color: #f4f4f4;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

td a {
  text-decoration: none;
}

td a:hover {
  text-decoration: underline;
}
.article-table-title {
    width: 60%;
}
.banners {
    width: 20%;
    margin-right: 10px;
    border-radius: 10px;
    height: fit-content;
    box-shadow: 10px 10px 5px rgba(0, 0, 0, 0.1) !important;
}

.banner-image:hover {
    cursor: pointer;
}
</style>

