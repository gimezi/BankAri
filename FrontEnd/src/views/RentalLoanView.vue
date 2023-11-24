<template>
    <div class="detail-page">
        <div v-if="rentalloan">
            <h3>{{ rentalloan.bank_name }}</h3>
            <h1 style="margin-bottom: 30px;">{{ rentalloan.deposit_name }}</h1>
            <hr>
            <div>
                <h3 v-if="rentalloan.options">옵션</h3>
                <div style="margin: 25px 0px;" v-for="option in rentalloan.options" :key="option.id">
                    <p style="font-size: 1.3em; margin-bottom: 5px;">{{ option.lend_rate_type_nm }}</p>
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">대출 상환 유형: {{ option.rpay_type_nm }}</p>
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">대출 금리(최저): {{ option.lend_rate_min }}</p>
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">대출 금리(최고): {{ option.lend_rate_max }}</p>
                </div>
            </div>
            <hr>
            <div>
                <h3 style="margin-bottom: 40px;">더 자세한 정보</h3>
                <div style="margin: 15px 0px;">
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">중도상환 수수료</p>
                    <p style="font-size: 1.3em;" v-html="rentalloan.erly_rpay_fee.replace(/\n/g,'<br>')"></p>
                </div>
                <div style="margin: 15px 0px;">
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">연체 이자율</p>
                    <p style="font-size: 1.3em;">{{ rentalloan.dly_rate }}</p>
                </div>
                <div style="margin: 15px 0px;">
                    <p style="margin: 0; color: rgb(156, 156, 156) ;">대출 한도</p>
                    <p style="font-size: 1.3em;">{{ rentalloan.loan_lmt }}</p>
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
const router = useRouter()
const rentalloan = ref(null)

onMounted(() => {
    // detail 가져오기
    axios({
        method: 'get',
        url: `${store.API_URL}/bankings/rentalloan-detail/${route.params.id}/`,
    }) .then((res) => {
        rentalloan.value = res.data
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
</style>