<template>
    <div class="detail-page">
        <div v-if="article">
            <h1 class="article-title">{{ article.title }}</h1>
            <div class="article-dates">
                <p class="article-date">작성일: {{ dayjs(article.created_at).format('YY.MM.DD HH.mm') }}</p>
                <p>수정일: {{ dayjs(article.updated_at).format('YY.MM.DD HH.mm') }}</p>
            </div>
            <hr>
            <p class="article-content">{{ article.content }}</p>
            <div class="article-user">
                <div>
                    <button class="article-button-element" v-if="checkMine(article)" @click="deleteArticle">글 삭제하기</button>
                    <RouterLink class="article-button-element" v-if="checkMine(article)" :to="{ name : 'UpdateArticleView', params: {id: article.id} }">글 수정하기</RouterLink>
                </div>
                <p>작성자: {{ article.user.nickname }}</p>
            </div>
        </div>
        <div v-else><p>해당 글이 없습니다.</p></div>
        <hr style="margin-top: 20px;">
        <div class="comments">
            <p style="font-size: 20px;">Comments</p>
            <form class="comment-form" @submit.prevent="createNewComment">
                <textarea class="comment-input" type="text" v-model="newComment"></textarea>
                <input class="comment-submit" type="submit" value="댓글 작성하기">
            </form>
            <div v-if="comments">
                <div v-for="comment in comments" :key="comment.id" class="comment-container">
                    <div class="comment-content">
                        <p style="font-size: 19px; color: darkblue;">{{ comment.user.nickname }}</p>
                        <p>{{ comment.content }}</p>
                    </div>
                    <button v-if="checkMine(comment)" @click="deleteComment(comment.id)" class="comment-delete-btn">삭제</button>

                </div>
            </div>
            <div v-else>
                <p>작성된 댓글이 없습니다.</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import dayjs from 'dayjs'

const store = useCounterStore()
const router = useRouter()
const route = useRoute()
const article = ref(null)
const comments = ref(null)
const newComment = ref(null)


// 내껀지 확인하는 함수
const checkMine = function(docu) {
    if (store.isLogin === true) {
        if (docu.user.id === store.nowUserId) {
            return true
        } else {
            return false
        }
    } else {
        return false
    }
    
}

// 새로운 댓글 생성
const createNewComment = function() {
    if (store.isLogin === true) {
        axios({
            method: 'post',
            url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
            data: {
                'content': newComment.value
            },
            headers: {
                Authorization: `Token ${store.token}`   
            }
        }) .then((res) => {
            router.go(0)
            console.log(res)
        }) .catch((error) => {console.log(error)})
    } else {
        window.alert('로그인하세요')
        router.push({name: 'LogInView'})
    }
    
}

// 글 삭제
const deleteArticle = function() {
    const isConfirmed = window.confirm('삭제하시겠습니까?')
    if (isConfirmed) {
        axios({
            method: 'delete',
            url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
            headers: {
                Authorization: `Token ${store.token}`   
            }
        }) .then((res) => {
            router.push({name: 'ArticleView'})
        }) .catch((error) => {
            console.log(error)
        })
    } else {
        window.alert('취소되었습니다')
    }   
}



// 댓글 삭제
const deleteComment = function (commentid) {
    const isConfirmed = window.confirm('댓글을 삭제하시겠습니까?')
    if (isConfirmed) {
        axios({
                method: 'delete',
                url: `${store.API_URL}/api/v1/articles/${route.params.id}/comment/${commentid}/`,
                headers: {
                    Authorization: `Token ${store.token}`   
                }
            }). then((res) => {
                console.log(res)
                router.go(0)
            }) .catch((err) => {
                console.log(err)
            })
        } else {
            window.alert('취소되었습니다')
        }
    }
     


// 처음에 글, 댓글 가져오기
onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
        // headers: {
        //     Authorization: `Token ${store.token}`   
        // }
    }) .then((response) => {
        article.value = response.data.article
        comments.value = response.data.comments
    }) .catch((error) => {console.log(error)})
})

</script>

<style scoped>
.detail-page{
    padding: 50px 20px;
}
@media screen and (min-width: 1000px) {
    .detail-page{
        padding: 50px 300px;
    }
}
.article-title {
    font-size: 40px;
}
.article-dates {
    display: flex;
    justify-content: flex-start;
    font-size: 14px;
}
.article-date{
    margin-right: 20px;
}
hr {
    margin: 0px;
}
.article-content {
    margin: 10px 0px;
    padding: 50px 0px;
    font-size: 20px;
}
.article-user {
    margin-top: 15px;
    display: flex;
    justify-content: space-between;
}
.article-button-element {
    margin: 0px 5px;
    border: none;
    border-radius: 10px;
    background-color: white;
    padding: 3px;
    text-decoration: none;
    color: gray;
    height: 35px; /* 고정 높이 */
    line-height: 40px; /* 텍스트 세로 중앙 정렬 */
    display: inline-flex; /* Flexbox를 사용한 중앙 정렬 */
    align-items: center; /* 수직 중앙 정렬 */
    justify-content: center; /* 수평 중앙 정렬 */
}
.article-button-element:hover {
    background-color: rgba(160, 159, 159, 0.685);
    color: white;
}
.comments {
    margin-top: 15px;
    padding: 10px 10px;
    display: flex;
    justify-content: center;
    flex-direction: column;
}
.comment-form {
    width: 100%;
    padding: 10px;
    display: flex;
    justify-content: space-between;
}
.comment-input {
    border: 2px solid grey;
    border-radius: 10px;
    height: 80px;
    resize: none;
    padding: 10px;
    flex: 1;
}
.comment-submit {
    /* border: 2px solid rgba(234, 238, 17, 0.479); */
    border-radius: 10px;
    background-color: rgb(179, 179, 179);
    color: black;
    width: 100px;
    margin-left: 5px;
}
.comment-submit:hover {
    background-color: rgba(160, 159, 159, 0.685);
    color: white;
}
.comment-container {
    border-bottom: 1px solid silver;
    margin-top: 20px;
    width: 100%;
    height: 120px;
    padding: 10px;
    display: flex;
    justify-content: space-between;
}
.comment-delete-btn {
    background-color: silver;
    border: 1px solid silver;
    color: white;
    width: 50px;
    height: 30%;
    margin-left: 5px;
    margin-bottom: 10px;
    align-self: flex-end;
}
.comment-delete-btn:hover{
    background-color: rgba(160, 159, 159, 0.685);
    color: black;
}
</style>