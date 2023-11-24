<template>
    <div class="article-page">
        <div class="article row">
            <h1 class="article-title">자유게시판</h1>
            <p class="article-title">모두가 자유롭게 이용하는 게시판입니다.</p>
            <ArticleList class="col-10 offset-1"/>
        </div>
    </div>
    
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue'

const store = useCounterStore()

onMounted(() => {
    store.getArticles()
})


</script>

<style scoped>
.article-page {
    padding: 50px 20px;
}
@media screen and (min-width: 1400px) {
    .article-page {
        padding: 50px 200px;
    }
}

.article-title {
    margin: 20px auto;
    text-align: center;
}
</style>