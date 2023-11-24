<template>
    <div style="width: 100%;">
        <DepositListItem 
        v-if="deposits"
        :deposits="deposits"/>
        <p v-else>로딩중..</p>
    </div>
</template>

<script setup> 
import DepositListItem from '@/components/DepositListItem.vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
import { ref,onMounted, watch } from 'vue';

const deposits = ref(null)
const store = useCounterStore()

onMounted(() => {
    console.log(store.issaved)
    if (store.issaved == true) {
       axios({
            method: 'get',
            url: `${store.API_URL}/bankings/`,
        }) .then((res) => {
            deposits.value = res.data.deposits
        }) .catch((err) => console.log(err)) 
    }
})

</script>

<style scoped>

</style>