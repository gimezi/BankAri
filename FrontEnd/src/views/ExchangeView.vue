<template>
    <div class="exchange-page">
        <h1 style="margin: 20px auto; text-align: center;">환율 계산기</h1>
        <div v-if="store.ex_info" class="calculator">
            <p style="font-size: 2em; text-align: center; color :#86c5c7 ;">나라를 골라주세요</p>
            <select type="select" v-model="nation" class="select-box">
                <option v-for="option in options" :key="option">
                    {{ option }}
                </option>
            </select>
        </div>
        <div v-else><p>로딩중</p></div>
        <form @submit.prevent="searchfunction" class="calculator" v-if="nation">
            <p style="font-size: 2em; text-align: center; color :#86c5c7 ;">얼마를 환산할까요?</p>
            <input :class="{ 'select-box' : true, 'isEmpty' : isEmpty }" type="text" id="tot" v-model="tot">
            <button v-if="isNumeric(tot)" class="submit-btn" type="submit"><i class="fa-solid fa-right-left fa-xl"></i>  환산!</button>
            <p v-else>숫자만 입력해주세요!</p>
        </form>
        <div v-if="store.exchange" class="result">
            <p style="font-size: 1.5em;">{{ store.exchange['unit'] + '  ' + tot}} 을 원화로 환산하면,</p>
            <p style="font-size: 2em; color: #86c5c7;">{{ store.exchange['price']*tot }}원 입니다!</p>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter' 


const store = useCounterStore()
const nation = ref(null)
const unit = ref(null)
const tot = ref(null)
const isEmpty = ref(null)

const options = [
    'AED','AUD','BHD','BND','CAD','CHF','CNH','DKK','EUR','GBP','HKD','IDR(100)','JPY(100)','KWD',
    'MYR','NOK','NZD','SAR','SEK','SGD','THB','USD'
]
function isNumeric(str) {
    return /^\d+$/.test(str);
}


const searchfunction = function() {
    if (tot.value == null) {
        isEmpty.value = true
    } else {
        isEmpty.value = false
        const payload = {
            nation : nation.value,
            unit : unit.value,
            tot : tot.value
        }
        store.searchEx(payload)  
    }
}

onMounted(async() => {
    // onmount하면서 데이터 갖고옴.
    await store.get_info()
    store.exchange = null
})

</script>


<style scoped>
.exchange-page {
    padding: 50px 20px;
}
@media screen and (min-width: 1400px) {
    .exchange-page {
        padding: 50px 200px;
    }
}
.calculator {
    margin-top: 100px;
    display: flex;
    flex-direction: column;
    text-align: center;
}
.select-box {
    width: 30%;
    margin: auto;
    height: 40px;
}
.submit-btn {
    margin: 30px auto;
    width: 20%;
    border: none;
    height: 50px;
    border-radius: 30px;
    font-size: 1.3em;
}
.isEmpty {
    border: 1px solid red;
}
.result {
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    text-align: center;
}


/* 올라오는 효과 */
.slideUp-enter-active, .slideUp-leave-active {
  transition: transform 1s;
}
.slideUp-enter, .slideUp-leave-to {
  transform: translateY(20px); /* 텍스트가 아래에서 위로 올라오는 효과를 위한 translateY */
  opacity: 0;
}
</style>