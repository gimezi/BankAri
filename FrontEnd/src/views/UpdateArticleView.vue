<template>
    <div class="create-page">
        <div class="back-btn">
            <button @mouseenter="invi = false" @mouseleave="invi = true" @click="goback" class="back-button"><i class="fa-solid fa-left-long fa-xl" style="color: darkslategray;"></i></button>
            <p :class="{'invisible' : invi, 'button-p': true}">뒤로가기</p>
        </div>
        <h1>게시글 수정</h1>
        <form v-if="article" @submit.prevent="updateArticle" class="create-form">
            <input class="title-input" type="text" v-model="article.title" >
            <hr>
            <textarea class="content-input" type="text" v-model="article.content"></textarea>
            <button type="submit" class="fixed-bottom-button">수정하기</button>
        </form>
        <p v-else>로딩중</p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const invi = ref(true)
const goback = function() {
    router.go(-1)
}
const updateArticle = function() {
    axios({
        method: 'put',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
        data: {
            'title': article.value.title,
            'content': article.value.content
        }
    }) .then((res) => {
        router.push({name: 'DetailView' , params: { id: article.value.id}})
    }) .catch((err) => {
        console.log(err)
    })
}

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    }) .then((response) => {
        article.value = response.data.article
    }) .catch((error) => {console.log(error)})
})
</script>

<style scoped>
.back-button {
    width: 50px;
    height: 50px;
    background: none;
    border: none;
}
.back-btn {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin: 0px;
}
.button-p {
    margin: 0;
    color: darkslategray;
}

.create-page {
    padding: 50px 20px;
}
@media screen and (min-width: 1400px) {
    .create-page {
        padding: 50px 200px;
    }
}

.create-page{
    padding: 10px 60px;
    display: flex;
    flex-direction: column;
    align-content: center;
}
@media screen and (min-width: 1100px) {
    .create-page{
        padding: 10px 300px;
    }
}
.create-page h1 {
    margin: 20px 0px;
}
.create-form {
    display: flex;
    flex-direction: column;
}
.invisible {
    display: none;
}
.title-input {
    border: 1px solid white;
    font-size: 1.7em;
    padding: 10px;
    box-sizing: border-box;
}

.content-input {
    border: none;
    padding: 10px;
    height: 800px;
}

.fixed-bottom-button {
    width: 300px;
    height: 100;
    position: fixed; /* 요소를 고정 위치에 두기 */
    bottom: 10px;    /* 페이지 하단에서 10픽셀 위에 위치 */
    left: 80%;       /* 요소를 가로축의 중앙에 위치 */
    transform: translateX(-50%); /* 요소를 가로축 중앙 정렬 */
    padding: 10px 20px; /* 버튼의 패딩 */
    background-color: darkslategray; /* 버튼의 배경 색상 */
    color: white; /* 버튼의 글자 색상 */
    border: none; /* 버튼의 테두리 없애기 */
    border-radius: 5px; /* 버튼의 모서리 둥글게 */
    cursor: pointer; /* 마우스 오버 시 커서 변경 */
}

</style>