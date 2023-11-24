<template>
    <div class="banking-page">
        <h1 class="banking-title">금융상품 정보</h1>
        <ul v-if="store.issaved" class="nav nav-underline">
            <li class="nav-item">
                <button :class="{'nav-link': true , 'active': actives.deposit }" @click="goDeposit">예금 목록</button>
            </li>
            <li class="nav-item">
                <button :class="{'nav-link': true , 'active': actives.saving }" @click="goSaving">적금 목록</button>
            </li>
            <li class="nav-item">
                <button :class="{'nav-link': true , 'active': actives.rentalloan }" @click="goRentalloan">대출 목록</button>
            </li>
        </ul>
       
        <div v-if="store.issaved" class="table">
            <DepositList v-if="store.selectedbanking == '예금 보기' | ''"/> 
            <SavingList v-if="store.selectedbanking == '적금 보기'"/>
            <RentalLoanList v-if="store.selectedbanking == '대출 보기'"/>
        </div>
        <div v-else>
            <p>로딩중~</p>
        </div>
    </div>
</template>

<script setup>
import DepositList from '@/components/DepositList.vue'
import SavingList from '@/components/SavingList.vue'
import RentalLoanList from '@/components/RentalLoanList.vue'
import { useCounterStore } from '@/stores/counter'
import { onMounted, ref } from 'vue'

const store = useCounterStore()
const iscomplete = ref(false)
const actives = ref({
    deposit: true,
    saving: false,
    rentalloan: false
})
const goDeposit = function() {
    actives.value.deposit = true
    actives.value.saving = false
    actives.value.rentalloan = false
    store.selectedbanking = '예금 보기'
}
const goSaving = function() {
    actives.value.deposit = false
    actives.value.saving = true
    actives.value.rentalloan = false
    store.selectedbanking = '적금 보기'
}
const goRentalloan = function() {
    actives.value.deposit = false
    actives.value.saving = false
    actives.value.rentalloan = true
    store.selectedbanking = '대출 보기'
}



onMounted(async() => {
    if (store.issaved != true) {
        // 초기에 DB에 저장
        await store.getBankData()
    } 
})

    
</script>

<style scoped>

.banking-page{
    padding: 50px 20px;
    display: flex;
    flex-direction: column;
    align-content: center;
}
@media screen and (min-width: 1100px) {
    .banking-page{
        padding: 50px 250px;
    }
}
.banking-title {
    margin-bottom: 20px;
}

.nav {
    margin: 10px 0px;
}
.nav-link{
    color: #86c5c7;
    font-size: 1.2em;
}
.table {
    margin-top: 20px ;
    display: flex;
    justify-content: center;
}
</style>