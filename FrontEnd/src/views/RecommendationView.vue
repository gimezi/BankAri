<template>
  <div>
    <div class="title-box">
        <h2> <span class="highlight">자산</span>과 <span class="highlight">연소득</span>을 입력해주시면 </h2>
        <h2> 나와 비슷한 사람들이 사용하는 <span class="highlight">예금,적금을 추천</span>해드려요 </h2>
    </div>
    <div style="margin-top: 40px;">
        <form @submit.prevent="recommendation" >
            <label for="age">나이</label>
            <input type="number" v-model.trim="age" min="20" max="100" step="1" placeholder="나이를 입력해주세요!">
        
            <br>
            <br>

            <label for="money">자산</label>
            <select type="select" v-model.trim="money">
                <option selected value="" disabled>현재 자산 규모 선택</option>
                <option v-for="(value, key) in money_options" :key="key" :value="value">
                    {{ key }}
                </option>
            </select>

            <br> 
            <br>

            <label for="salary">연소득</label>
            <select type="select" v-model.trim="salary">
                <option value=""  disabled selected>연소득 선택</option>
                <option v-for="(value, key) in salary_options" :key="key" :value="value">
                    {{ key }}
                </option>
            </select>
            <br>
            <br>
            <div> 
                <button type="submit" > 상품 추천 받기 </button>
            </div>
    </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter' 
import { useRouter } from 'vue-router';


const store = useCounterStore()
const age = ref(null)
const money = ref(null)
const salary = ref(null)

// 나이
// age_bins = [20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80]

// 자산
// money_bins = [100000, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000]

// 연봉 
// salary_bins = [10000000, 19000000, 28000000, 37000000, 46000000, 55000000, 64000000, 73000000, 82000000, 91000000, 100000000]

// 연봉 범위
const salary_options = { '10,000,000 - 19,999,999':'15000000','20,000,000 - 29,999,999':'25000000' ,'30,000,000 - 39,999,999':'35000000' ,'40,000,000 - 49,999,999':'45000000' ,'50,000,000 - 59,999,999':'55000000' ,'60,000,000 - 69,999,999':'65000000' ,'70,000,000 - 79,999,999':'75000000' , '80,000,000 - 89,999,999': '85000000','90,000,000 - 100,000,000':'95000000' }

// 자산 범위
// const average_money  = ['100,000 - 9,999,999','10,000,000 - 19,999,999','20,000,000 - 29,999,999','30,000,000 - 39,999,999','40,000,000 - 49,999,999','50,000,000 - 59,999,999', '60,000,000 - 69,999,999','70,000,000 - 79,999,999','80,000,000 - 89,999,999','90,000,000 - 100,000,000']
const money_options = { '100,000 - 9,999,999':'5050000',  '10,000,000 - 19,999,999':'15000000',  '20,000,000 - 29,999,999':'25000000',  '30,000,000 - 39,999,999':'35000000',  '40,000,000 - 49,999,999':'45000000',  '50,000,000 - 59,999,999':'55000000',  '60,000,000 - 69,999,999':'65000000',  '70,000,000 - 79,999,999':'75000000',  '80,000,000 - 89,999,999':'85000000',  '90,000,000 - 100,000,000':'95000000'}

const router = useRouter()

const recommendation = function() {
    // 실행됨
    console.log(money.value)
    console.log(age.value)
    console.log(salary.value)
    const payload = {
        age : age.value,
        money : money.value,
        // money : '5050000',
        salary : salary.value
        // salary : '15000000'
    }
    store.recommend(payload)
    router.push({name: 'MyPageView', params: {username: store.nowUserName}})
}


</script>

<style scoped>
.highlight {
  color: #86c5c7;
  font-size: 1.4em;
}

.title-box {
  text-align: center;
  margin-bottom: 2rem;
}


form {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  background: #eeeded;
}

label {
  font-size: 1.3em;
  display: block;
  margin-bottom: .5rem;
  color: #333;
}

input[type=number], select {
  width: 100%;
  padding: 10px;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box; /* Include padding and border in the element's width and height */
}

button {
  width: 100%;
  padding: 10px;
  background-color:  #86c5c7;
  color: black;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color:  grey;
  color: white;
}

@media (max-width: 768px) {
  .h h2 {
    font-size: 1.2rem;
  }

  form {
    padding: 1rem;
  }

  label {
    margin-bottom: .3rem;
  }

  input[type=number], select, button {
    padding: .5rem;
  }
}
</style>

