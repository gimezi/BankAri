<template>
  <div class="signup-page">
    <div class="signup-container">
        <h1>회원가입</h1>
        <form @submit.prevent="signUp" class="signup-form">
          <div class="form-group">
            <label for="userName">아이디</label>
            <div class="nickname-input">
              <input type="text" v-model.trim="userName" id="userName" class="form-control" :class="{error : errorStyle.id}" placeholder="Enter your username">
              <div @click="dupId" class="recommend-link">중복확인</div>
            </div>
            <p>{{ dupMessage }}</p>
          </div>

          <div class="form-group">
            <label for="password1">비밀번호</label>
            <input type="password" v-model.trim="password1" class="form-control" :class="{'error' : errorStyle.password1}" placeholder="Enter your password">
          </div>

          <div class="form-group">
            <label for="password2">비밀번호 확인</label>
            <input type="password" v-model.trim="password2" class="form-control" :class="{'error' : errorStyle.password2}" placeholder="Confirm your password">
            <p>{{ passwordmessage }}</p>
          </div>

          <div class="form-group">
            <label for="nickname">닉네임</label>
            <div class="nickname-input">
              <input type="text" v-model.trim="nickName" id="nickname" class="form-control" :class="{'error' : errorStyle.nickName}" placeholder="Enter your nickname">
              <div @click="recommendNickName" class="recommend-link">추천받기</div>
            </div>
            <p style="color: grey;">닉네임을 정하기 어렵다면 추천받기를 선택해보세요!</p>
          </div>
          <button type="submit" class="btn btn-primary">가입하기</button>
        </form>
      </div>
  </div>
  
</template>

<script setup>
import { ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter' 
import axios from 'axios';
  
  const store = useCounterStore()
  const userName = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const nickName = ref(null)
  const adjectives = [
    '유쾌한', '신나는', '환상적인', '유머러스한', '신비로운',
    '흥겨운', '아름다운', '노래하는', '춤추는', '귀여운'
  ]
  const nouns = [
    '강아지', '고양이', '카피바라', '사자', '코끼리', 
    '햄스터', '토끼', '고슴도치', '원숭이', '기린',' 다람쥐'
  ]
  const passwordmessage = ref(null)
  const errorStyle = ref({
    id : false,
    password1: false,
    password2: false,
    nickName: false
  })
  const dupMessage = ref(null)
  const isvalidid = ref(false)
  const passwordWatch = function() {
    if (password1.value && password2.value) {
      passwordmessage.value = password1.value === password2.value ? '일치합니다' : '일치하지 않습니다'
    } else {
      passwordmessage.value = null
    }
  }

  const inputWatch = function() {
    if (userName.value) {
      errorStyle.value.id = false
    }
    if (password1.value) {
      errorStyle.value.password1 = false
    }
    if (password2.value) {
      errorStyle.value.password2 = false
    }
    if (nickName.value) {
      errorStyle.value.nickName = false
    }
  }

  // 비밀번호 일치 확인
  watch([password1, password2], passwordWatch)

  // 쓰고 있으면 색깔 원복
  watch([userName, password1, password2, nickName], inputWatch)

  // 닉네임 중복 확인
  const dupId = function() {
    if (userName.value) {
      axios({
        method: 'get',
        url: `${store.API_URL}/accountsapps/check-username/${userName.value}/`,
      }) .then((res) => {
        console.log(res.data.message)
        dupMessage.value = res.data.message
        if (dupMessage.value == '존재하는 아이디입니다.') {
          errorStyle.value.id = true
        } else {
          errorStyle.value.id = false
          isvalidid.value = true
        }
      }) .catch((err) => {
        console.log(err)
      })
    } else {
      dupMessage.value =  '아이디를 입력해 주세요'
      errorStyle.value.id = true
    }
  }

  // 랜덤 닉네임 생성
  const randomname  = function(array) {
    const randomIndex = Math.round(Math.random() * array.length)
    if (array[randomIndex] == undefined) {
        return array[0]
    } else {
        return array[randomIndex]
    }
}
  const recommendNickName = function() {
    const tmp = document.getElementById('nickname')
    tmp.value = `${randomname(adjectives)} ${randomname(nouns)}`
    nickName.value = tmp.value
  }
  // 유효성 검사 알림창
  const errorMessage = function(res) {
    if (res.includes('This password is too short')) {
      return '비밀번호가 너무 짧습니다. 8자 이상, 특수문자를 포함해야합니다.'
    } else if (res.includes('This password is too common')){
      return '비밀번호가 너무 흔합니다. 8자 이상, 특수문자를 포함해야합니다.'
    }
  }


  // 회원가입 로직
  const signUp = function() {
    if (dupMessage.value == '존재하는 아이디입니다.') {
      errorStyle.value.id = true
    } else if (passwordmessage.value != '일치합니다') {
      errorStyle.value.password2 = true
    } else {
      if (isvalidid.value && password1.value && password2.value && nickName.value) {
        const payload = {
          username: userName.value,
          password1: password1.value,
          password2: password2.value,
          nickname: nickName.value,
        }
        store.signUp(payload)
      } else {
        if (isvalidid.value == false) {
          dupMessage.value = '중복검사를 해주세요'
        }
        errorStyle.value = {
          id : isvalidid.value ? false : true,
          password1 : password1.value ? false : true,
          password2 : password2.value ? false : true,
          nickName : nickName.value ? false : true,
        }
      }
    }
    
     
  }
  
</script>

<style scoped>

/* 반응형 조절 */
.signup-page {
  padding: 50px 20px;
}
@media screen and (min-width: 1400px) {
  .signup-page {
      padding: 50px 200px;
  }
}
.error {
  border: 1px solid red  !important;
}
.signup-container {
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

.signup-form {
  margin-top: 50px;
}

.form-group {
  margin-bottom: 25px;
}

label {
  font-size: 1.2em;
  display: block;
  margin-bottom: 8px;
}

.form-control {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  border: 1px solid #ced4da;
  border-radius: 4px;
}

.nickname-input {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.recommend-link {
  width: 80px;
  height: 40px;
  color: black;
  cursor: pointer;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background-color: #86c5c7;
  margin: 0 10px;
}

.recommend-link:hover {
  background-color: grey;
  color: white;
}

.btn {
  display: block;
  width: 100%;
  padding: 12px;
  color: #fff;
  background-color: #86c5c7;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn:hover {
  background-color: grey;
  color: white;
}
  </style>
  