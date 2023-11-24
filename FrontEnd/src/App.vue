<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <RouterLink :to="{ name : 'MainView' }">
          <img src="@/assets/mainlogo.PNG" alt="Main" class="mainlogo">
        </RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="true" aria-label="Toggle navigation">
          <i class="fa-solid fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li  class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">금융 상품</a>
              <ul class="dropdown-menu">
                <li><RouterLink :to="{ name: 'BankingView', params: {content: 'deposit'}}" class="dropdown-item">예금</RouterLink></li>
                <li><RouterLink :to="{ name: 'BankingView', params: {content: 'saving'}}" class="dropdown-item">적금</RouterLink></li>
                <li><RouterLink :to="{ name: 'BankingView', params: {content: 'rentalloan'}}" class="dropdown-item">대출</RouterLink></li>
              </ul>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'ExchangeView' }" class="nav-link">환율 계산</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'MapView' }" class="nav-link">지도 보기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name : 'ArticleView' }" class="nav-link">게시판</RouterLink>
            </li> 
          </ul>
          <form class="d-flex">
            <div v-if="!store.isLogin">
              <RouterLink :to="{ name : 'LogInView' }" class="btn btn-outline-success login-button">Log In</RouterLink>
              <RouterLink :to="{ name : 'SignUpView' }" class="btn btn-outline-primary login-button">SIGN UP</RouterLink>
            </div>
            <div v-else>
              <RouterLink :to="{ name : 'MyPageView', params: {username: store.nowUserName}}" class="mypage-link login-button">마이페이지</RouterLink>
              <button @click="logOut" class="btn btn-outline-danger login-button">LOGOUT</button>
            </div>
          </form>
        </div>
      </div>
    </nav>
    <RouterView class="main-content"/>
    <footer class="bg-body-tertiary p-3">
      <p>&copy; 2023 SSAFY, Final Project. All rights reserved.</p>
    </footer>
  </div>
</template>
<script setup>
import { RouterView, RouterLink, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import { onMounted } from 'vue';

const store = useCounterStore()
const router = useRouter()

const logOut = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/accounts/logout/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((res) =>{
    store.token = null
    // store.isLogin = false
    window.alert('로그아웃 완료!')
    router.push({ name: 'MainView' })
    // console.log(res)
  }).catch((err) => {
    console.log(err)
  })
}


</script>

<style scoped>
.navbar {
  width: 100%;
  padding-top: 20px !important;
  background-color: #ffffffde !important;
  font-size: 23px;
  padding: 0px;
}
@media screen and (min-width: 1000px) {
    .navbar{
        padding: 0 80px;
    }
}
.navbar-toggler {
  border: none;
}
.main-content {
  min-height: 900px;
  width: 100%;
  padding-top: 50px;
}
.mainlogo {
  margin-right: 20px;
  width: 150px;
}
.nav-item {
  margin: 0 5px !important;
}
.nav-link {
  color: black;
}
.nav-link:hover{
  color: #86c5c7;
}
.mypage-link {
  text-decoration-line: none;
  color: black;
  font-size: 20px;
  margin-right: 10px;
}
.mypage-link:hover{
  color: #86c5c7;
}
 .login-button {
  margin: 0 10px;
 }

.dropdown-menu {
  background-color: rgb(245, 245, 245) !important;
  box-shadow: 0px 4px 8px rgba(201, 201, 201, 0.9);
}

.footer {
  padding: 10px; /* 위아래 여백 지정 */
}
</style>
