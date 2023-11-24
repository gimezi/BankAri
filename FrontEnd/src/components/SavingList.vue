<template>
    <div style="width: 100%;">
        <SavingListItem 
        v-if="savings"
        :savings="savings"/>
        <p v-else>로딩중..</p>
    </div>
</template>

<script setup> 
import SavingListItem from '@/components/SavingListItem.vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
import { ref,onMounted } from 'vue';

const savings = ref(null)
const store = useCounterStore()
onMounted(() => {
    // 전체 데이터를 가져옴
    axios({
        method: 'get',
        url: `${store.API_URL}/bankings/`,
    }) .then((res) => {
        savings.value = res.data.savings
    }) .catch((err) => console.log(err))
})

</script>

<style scoped>

</style>