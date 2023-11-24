<template>
    <div class="detail-page">
        <div v-if="saving">
            <h3>{{ saving.bank_name }}</h3>
            <h1 style="margin-bottom: 30px;">{{ saving.deposit_name }}</h1>
            <div class="header-box">
                <div class="intr-box">
                    <p style="margin-bottom: 5px;">최고 금리</p>
                    <p style="font-size: 1.6em; color: #86c5c7;" >{{ maxval2 }}%</p>
                </div>
                <div class="intr-box">
                    <p style="margin-bottom: 5px;">기본 금리</p>
                    <p style="font-size: 1.6em;">{{ maxval1 }}%</p>
                </div>
            </div>
            <hr>
            <div>
                <div class="percent-box">
                    <h3 style="margin-top: 20px;">이자 계산기</h3>
                    <div class="navbox">
                        <ul class="nav nav-underline">
                            <li v-for="month in months" class="nav-item">
                                <button :class="{'nav-link': true , 'active': false }" @click="pick(month)" >{{ month }}</button>
                            </li>
                        </ul>
                    </div>
                    <div class="persent-output" v-if="basicoptions[selectedmonth] && selectedmonth"> 
                        <h1 style="text-align: center; color: #86c5c7;">금리 {{ maxoptions[selectedmonth] }}%</h1>
                        <div style="margin: 0 auto; display: flex;">
                            <p>기본 {{ maxoptions[selectedmonth] }}%</p>
                            <p v-if="iszero()" style="margin-left: 5px;">+ 우대 {{ (Number(maxoptions[selectedmonth]) - Number(basicoptions[selectedmonth])).toFixed(2) }}%</p>
                        </div>
                    </div>
                    <div v-else class="persent-output">
                        <p v-if="selectedmonth" style="margin: 0 auto;">해당 상품은 {{ selectedmonth }}짜리 상품이 없습니다!</p>
                        <div v-else></div>
                    </div>
                    
                </div>
                <div style="text-align: center;" v-if="selectedmonth">
                    <p style="color: rgb(156, 156, 156);">매달 <input type="text" inputmode="numeric" pattern="[0-9]*" v-model="money" class="money-input">원을 예금하면</p>
                    <p style="font-size: 1.2em;">총 {{ (money * Number(maxoptions[selectedmonth]) * Number(month[selectedmonth]) / 12).toFixed(0) }}원의 이자를 받을 수 있어요!</p>
                    <p style="font-size: 0.8em; color: rgb(156, 156, 156);">우대금리가 반영된 금액이에요!(세전)</p>
                </div>
                <div v-else style="text-align: center;">
                    <h2 style="margin-bottom: 20px;">기간을 선택해주세요!</h2>
                </div>
            </div>
            <hr>
            <div>
                <h3 style="margin-bottom: 40px;">더 자세한 정보</h3>
                <div style="margin: 15px 0px;">
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">가입 대상</p>
                    <p style="font-size: 1.3em;">{{ saving.join_member }}</p>
                </div>
                <div style="margin: 15px 0px;">
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">가입 방법</p>
                    <p style="font-size: 1.3em;">{{ saving.join_way }}</p>
                </div>
                <div style="margin: 15px 0px;">
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">상품 코드</p>
                    <p style="font-size: 1.3em;">{{ saving.fin_prdt_cd }}</p>
                </div>
            </div>
        </div>
        <div v-else>
            <p>로딩중</p>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const store = useCounterStore()
const route = useRoute()
const saving = ref(null)
const basicoptions = ref({})
const maxoptions = ref({})
const maxval1 = ref(0)
const maxval2 = ref(0)
const data = ref([])
const months = ['6개월', '12개월', '24개월', '36개월']
const selectedmonth = ref(null)
const money = ref(100000)
const month = ref({
    '6개월' : 6,
    '12개월' : 12,
    '24개월' : 24,
    '36개월' : 36
})
const intr = ref(money.value * Number(maxoptions.value[selectedmonth.value]) * Number(month.value[selectedmonth.value]) / 12)
const pick = function(month) {
    selectedmonth.value = month
}
const iszero = function() {
    if ( Number(maxoptions.value[selectedmonth.value]) - Number(basicoptions.value[selectedmonth.value]) != 0 ) {
        return true
    } else {return false}
}



onMounted(() => {
    // detail 가져오기
    axios({
        method: 'get',
        url: `${store.API_URL}/bankings/saving-detail/${route.params.id}/`,
    }) .then((res) => {
        saving.value = res.data
        basicoptions.value = {
            '6개월' : saving.value.option6 !== '-' ? saving.value.option6 : null,
            '12개월' : saving.value.option12 !== '-' ? saving.value.option12 : null,
            '24개월' : saving.value.option24 !== '-' ? saving.value.option24 : null,
            '36개월' : saving.value.option36 !== '-' ? saving.value.option36 : null,
        }
        maxoptions.value = {
            '6개월' : saving.value.maxoption6 !== '-' ? saving.value.maxoption6 : null,
            '12개월' : saving.value.maxoption12 !== '-' ? saving.value.maxoption12 : null,
            '24개월' : saving.value.maxoption24 !== '-' ? saving.value.maxoption24 : null,
            '36개월' : saving.value.maxoption36 !== '-' ? saving.value.maxoption36 : null, 
        }
        const values1 = Object.values(basicoptions.value).map(val => val === null ? 0 : val);
        maxval1.value = Math.max(...values1)
        const values2 = Object.values(maxoptions.value).map(val => val === null ? 0 : val);
        maxval2.value = Math.max(...values2)
        data.value = [basicoptions.value, maxoptions.value]
    }) .catch((err) => console.log(err))
})

</script>

<style scoped>
.detail-page{
    padding: 50px 20px;
    display: flex;
    flex-direction: column;
    align-content: center;
}
@media screen and (min-width: 1100px) {
    .detail-page{
        padding: 50px 250px;
    }
}
.header-box {
    display: flex;
    width: 200px;
    justify-content: space-between;
    margin-bottom: 20px;
}
.intr-box {
    margin-top: 10px;
    width: 89px;
    height: 70px;
}
.nav-link{
    color: rgb(156, 156, 156);
    font-size: 1.2em;
}

.percent-box {
    display: flex;
    justify-content: center;
    flex-direction: column;
}
.navbox {
    margin: auto;
}
.persent-output {
    height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-content: center;
}
.money-input {
    width: 100px;
    text-align: center;
    border: none;
    background-color: aliceblue;
}
</style>