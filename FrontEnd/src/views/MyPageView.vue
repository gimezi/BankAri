<template>
    <div class="my-page">
        <div class="table-container">
            <div class="mypage">
                <div>
                <h1 class="banking-title">회원 정보</h1>
                <ul class="nav nav-underline">
                    <li class="nav-item">
                        <button :class="{'nav-link': true }"  @click="router.push({name: 'UserUpdateView'})">회원 정보 수정</button>
                    </li>
                    <li class="nav-item">
                        <button :class="{'nav-link': true  }" @click="router.push({name: 'PWUpdateView'})">비밀 번호 수정</button>
                    </li>
                    <li class="nav-item">
                        <button :class="{'nav-link': true  }" @click="router.push({name: 'RecommendationView'})">금융 상품 추천</button>
                    </li>
                </ul>
            </div>

            <ProfileList v-if="user" :user="user"/>


            <div v-if="store.saving_recommproduct">
                <p> 나의 추천 목록 </p>
                    <h3>예금 추천 목록</h3>
                    <div>
                        <router-link v-if="typeof deposit_prdt_code !== 'undefined'"  v-bind:to="{ name:'DepositView', params: { id: deposit_prdt_code} }">나에게 맞는 예금 상품 지금 확인하러 갈까요? </router-link>
                    </div>
                    <h3>적금 추천 목록</h3>
                    <div>
                        <router-link v-if="typeof saving_prdt_code !== 'undefined'" v-bind:to="{ name:'SavingView', params: { id: saving_prdt_code} }">나에게 맞는 적금 상품 지금 확인하러 갈까요? </router-link>
                    </div>
                </div>
                <div v-else>
                    <p> </p>
                </div>
            </div>
        </div>
        <RouterView/>
    </div>
    
</template>


<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import { RouterView, RouterLink, useRouter } from 'vue-router'
import ProfileList from '@/components/ProfileList.vue'

const store = useCounterStore()
const user = ref(null)
const router = useRouter()

// 적금 데이타
const deposit_list = {27:'200-0135-12', 29:'200000303', 9 : '05100',17 : '10-01-20-388-0002' ,21 : '10120114700011' ,14 : '10-003-1387-0001' ,7:'01211310127',
5 : '01030500600002',16: '10-01-20-024-0059-0000',2: '010300100335',20:'10120114300011',25:'10511008001166004',3:'01030500510002',23 : '10511008000996000',
37: 'WR0001B',35:'TD11300035000',4: '01030500560002',11:'10-003-1225-0001',19 : '10120110400011',22:'10120116100011',12 : '10-003-1381-0001',
8:'01211310130',30: '21001115',24: '10511008001004000',31: '21001203',13: '10-003-1384-0001',26: '10511008001278000',18: '1001202000002',6:'01211310121',
0:'00320342',15:'10-01-20-024-0046-0000',28:'200000301',1:'01013000110000000001',10:'06492',36:'TD11300036000',33:'TD11300027000',32:'4'}

// 예금 데이타
const saving_list = {0: 'WR0001F',1: 'WR0001L',2: '00266451',3: '10521001000846001',4: '10521001001177000',5: '10527001000925000',
    6: '10527001001272000', 7: '10527001001278000', 8: '01020400380001', 9: '01020400490001',10: '01020400490002', 11: '01020400510001',
    12: '01020400530001', 13: '01020400610001', 14: 'TD11330029000', 15: 'TD11330030000', 16: 'TD11330031000', 17: 'TD11330032000',
    18: '220002101', 19: '220002301', 20: '220002501', 21: '220002701', 22: '10-01-30-031-0018-0000', 23: '10-01-30-031-0037-0000',
    24: '21000111',25: '21001116', 26: '21001199',27: '21001236', 28: '21001259', 29: '01211210110',30: '01211210113',31: '01211210121',
    32: '01211210122', 33: '03010', 34: '03100',35: '03202',36: '010200100051', 37: '010200100092', 38: '010200100104',39: '230-0119-85',
    40: '10-047-1360-0002',41: '10-047-1365-0001', 42: '10-047-1381-0001', 43: '10-047-1387-0001', 44: '10-059-1264-0001', 45: '52',
    46: '53', 47: '01012000200000000003', 48: '01012000210000000000', 49: '10140110400011', 50: '10140114300011', 51: '10140114700031',
    52: '10141109800021',53: '10141114300011', 54: '10141114700031', 55: '10141116600001',56: '10-01-30-355-0002', 57: '10-01-30-355-0005', 58: '1001303001001',
    59: '1001303001003',60: '1001303001004', 61: '1001303001005'}

const deposit_prdt_code = deposit_list[store.saving_recommproduct]
const saving_prdt_code = saving_list[store.deposit_recommproduct]



onMounted(() => {
      // 회원 정보 가져오기
    axios({
        method: 'get',
        url: `${store.API_URL}/accountsapps/profile/${store.nowUserName}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    }) .then((res) => {
        user.value = res.data
    }) .catch((error) => {
        console.log(error)
    })
})

</script>


<style scoped>
.my-page {
    padding: 50px 20px;
}
@media screen and (min-width: 1400px) {
    .my-page {
        padding: 50px 200px;
    }
}


.nav {
    margin: 10px 0px;
}
.nav-link{
    color: #86c5c7;
    font-size: 1.2em;
}
.table-container {
    padding: 50px 20px;
    display: flex;
    flex-direction: column;
}


.mypage {
    display: flex;
    flex-direction: column;
    align-items: baseline;
    width: 100%; 
    padding: 0; 
}

.h1 {
    display: flex;
    width: 100%;
    padding: 0;
}



.nav-link {
    color: #86c5c7;
    font-size: 1.2em;
}


table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
}

th, td {
    border: 1px solid #ddd;
    text-align: center;
    padding: 8px;
}


th {
    background-color: #ffc107;
    color: white;
}
</style>