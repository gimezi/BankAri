<template>
    <div style="width: 100%;">
        <RentalLoanListItem 
        v-if="rentalloans"
        :rentalloans="rentalloans"/>
        <p v-else>로딩중...</p>
    </div>
</template>

<script setup> 
import RentalLoanListItem from '@/components/RentalLoanListItem.vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
import { ref,onMounted } from 'vue';

const rentalloans = ref(null)
const store = useCounterStore()
onMounted(() => {
    // 전체 데이터를 가져옴
    axios({
        method: 'get',
        url: `${store.API_URL}/bankings/`,
    }) .then((res) => {
        rentalloans.value = res.data.rentalloans
    }) .catch((err) => console.log(err))
}) 
</script>

<style scoped>

</style>