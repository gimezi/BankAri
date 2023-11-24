<template>
    <div class="login-page">
      <div class="login-box">
        <h1>로그인</h1>
        <form @submit.prevent="logIn" class="login-form">
          <div class="form-group">
            <label for="username">아이디</label>
            <input type="text" id="username" v-model.trim="username" class="form-control" placeholder="Enter your username">
          </div>

          <div class="form-group">
            <label for="password">비밀번호</label>
            <input type="password" id="password" v-model.trim="password" class="form-control" placeholder="Enter your password">
          </div>

          <button type="submit" class="btn btn-primary">Login</button>
        </form>
      </div>
    
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter' 
  
  const store = useCounterStore()
  const username = ref(null)
  const password = ref(null)
  
  
  const logIn = function() {
    if (username.value == null) {
      window.alert('아이디를 입력해주세요!')
    } else if (password.value == null) {
      window.alert('비밀번호를 입력해주세요!')
    } else {
      const payload = {
        username: username.value,
        password: password.value
      }
      store.logIn(payload)
    }
    
  }
  </script>
  
  <style scoped>

  /* 반응형 조절 */
  .login-page {
    padding: 50px 20px;
}
@media screen and (min-width: 1400px) {
    .login-page {
        padding: 50px 200px;
    }
}
    .login-box {
    max-width: 600px;
    padding: 30px;
    margin: auto;
    background-color: #f4f4f4;
    border-radius: 8px;
    box-shadow: 15px 15px 10px rgba(0, 0, 0, 0.1);
  }

  h1 {
    text-align: center;
    color: #333;
    font-size: 2.5em;
  }

  .login-form {
    margin-top: 50px;
  }

  .form-group {
    margin-bottom: 25px;
  }

  label {
    font-size: 1.3em;
    display: block;
    margin-bottom: 8px;
}

  .form-control {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button {
    display: block;
    width: 100%;
    padding: 10px;
    color: black;
    background-color: #86c5c7;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: grey;
  }
  </style>
  