<template>
    <div class="article-list">
        <!-- <h3 class="article-list-title">Article List</h3> -->
        <div class="create-btn">
            <RouterLink :to="{ name:'CreateView' }" type="button" class="btn btn-outline-secondary">새로운 글 작성하기</RouterLink>
        </div>
        <table v-if="store.articles" class="col-2">
            <thead>
                <tr>
                    <th class="article-table-title">글 제목</th>
                    <th>작성자</th>
                    <th>작성일</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="article in store.articles" :key="article.id">
                    <td class="article-table-title"><RouterLink :to="{ name:'DetailView', params: { id: article.id } }" style="color: black;">{{ article.title }}</RouterLink></td>
                    <td>{{ article.user.nickname }}</td>
                    <td>{{ dayjs(article.created_at).format('YY.MM.DD HH.mm') }}</td>
                </tr>
            </tbody>
        </table>
        <div v-else>
            <p>작성된 글이 없습니다!</p>
        </div>
    </div>
</template>

<script setup> 
import { useCounterStore } from '@/stores/counter'
import dayjs from 'dayjs'

const store = useCounterStore()

</script>

<style scoped>


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

.create-btn {
    align-self: flex-end;
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
    margin-left: auto;
    margin-right: auto;
}

th, td {
  text-align: center;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

table thead {
  background-color: #f9e9a9; /* 배경색 */
  font-size: 19px;
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
  color: #0366d6;
  text-decoration: none;
}

td a:hover {
  text-decoration: underline;
}
.article-table-title {
    width: 65%;
}

</style>