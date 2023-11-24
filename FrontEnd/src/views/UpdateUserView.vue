<template>
    <div>
        <div class="back-btn">
            <button @mouseenter="invi = false" @mouseleave="invi = true" @click="goback" class="back-button"><i class="fa-solid fa-left-long fa-xl" style="color: darkslategray;"></i></button>
            <p :class="{'invisible' : invi, 'button-p': true}" style="font-size: 1.2em;">뒤로가기</p>
        </div>
        <h2 style="text-align: center; margin-top: 20px;"> 회원 정보 수정 </h2>
        <form @submit.prevent="updateUser" >
            <label for="username">username : </label>
            <input type="text" id="username" v-model.trim="username" >
            <br>
            
            <br>
            <label for="nickname">nickname : </label>
            <input type="text" id="nickname" v-model.trim="nickname" > 

            <br>
            <br>
            
            <button @click="updateUser" >수정하기</button>       
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const router = useRouter()
const username = ref(null)
const nickname = ref(null)
const invi = ref(true)
const goback = function() {
    router.go(-1)
}

// 회원 정보 업데이트
const updateUser = function() {
    axios({
        method: 'patch',
        url: `${store.API_URL}/accounts/user/`,
        data: {
            username : username.value,
            first_name : "not",
            last_name : "not",
            nickname : nickname.value,
        },
        headers: {
            Authorization: `Token ${store.token}`   
        }
    }) .then((res) => {
        window.alert('회원정보수정완료')
        router.push({name: 'MyPageView'})
    }) .catch((error) => {
        console.log(error)
    })   
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

    form {
    max-width: 400px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    background: #fff;
    }

    label {
    color: #333;
    display: block;
    margin: 10px 0 5px;
    font-size: 0.9rem;
    }

    input[type="text"] {
    width: calc(100% - 22px);
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box; /* Include padding and border in the element's width and height */
    }

    button {
    width: 100%;
    padding: 10px;
    border: none;
    background-color: #86c5c7;
    color: black;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    }

    button:hover {
    background-color: gray;
    color: white;
    }

    /* Additional responsive adjustments can be made here */
    @media (max-width: 600px) {
    form {
        width: 90%;
    }
    }

</style>