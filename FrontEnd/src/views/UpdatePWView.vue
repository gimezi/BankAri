<template>
    <div>
      <div class="back-btn">
        <button @mouseenter="invi = false" @mouseleave="invi = true" @click="goback" class="back-button"><i class="fa-solid fa-left-long fa-xl" style="color: darkslategray;"></i></button>
        <p :class="{'invisible' : invi, 'button-p': true}" style="font-size: 1.2em;">뒤로가기</p>
      </div>
      <h2 style="text-align: center; margin-top: 20px;">비밀번호 변경하기</h2>
      <form @submit.prevent="changePW" class ="password-form">
          <div class="form-group">
              <label for="cur">기존 비밀번호</label>
              <input type="password" id="cur" v-model.trim="old_password" class="form-control">
          </div>
          
          <div class="form-group">
              <label for="new1">새 비밀번호</label>
              <input type="password" id="new1" v-model.trim="new_password1" class="form-control"> 
          </div>
          <div class="form-group">
              <label for="new2">새 비밀번호 확인</label>
              <input type="password" id="new2" v-model.trim="new_password2" class="form-control">
              {{ passwordmessage }}
            </div>
          <button type="submit" class="btn btn-primary">비밀번호 변경하기</button>
      </form>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const new_password1 = ref(null)
const new_password2 = ref(null)
const old_password = ref(null)
const passwordmessage = ref(null)
const router = useRouter()
const invi = ref(true)
const goback = function() {
    router.go(-1)
}


// 둘이 일치하는지 확인
const passwordWatch = function() {
    if (new_password1.value && new_password2.value) {
      passwordmessage.value = new_password1.value === new_password2.value ? '일치합니다' : '일치하지 않습니다'
    } else {
      passwordmessage.value = null
    }
  }
watch([new_password1, new_password2], passwordWatch)

// 비밀번호 바꾸기
const changePW = function() {
  if (passwordmessage.value == '일치하지 않습니다') {
    window.alert('일치하지 않습니다.')
  } else {
    const payload = {
      new_password1 : new_password1.value,
      new_password2 : new_password2.value,
      old_password : old_password.value
    }
    store.changePW(payload)
  }
  
}


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
    padding-left: 30px;
}
.button-p {
    margin: 0;
    color: darkslategray;
}


.password-form {
    max-width: 400px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f4f4f4;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  }

  .form-group {
    margin-bottom: 15px;
  }

  label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
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
    background-color:#86c5c7;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: grey;
    color: white;
  }
</style>