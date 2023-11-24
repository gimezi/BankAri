<template>
    <div>
        <table>
            <thead>
            <tr>
                <th style="white-space: nowrap;">금융상품 이름</th>
                <th style="white-space: nowrap;">은행명</th>
                <th>
                    <div class="month-box">
                        <p>6개월</p>
                        <button @click="change6(savings)" class="custombutton">
                            <i :class="{'fa-solid': true, 'fa-caret-up': true, 'fa-rotate-180': !align6}"></i>                  
                        </button>
                    </div>
                </th>
                <th>
                    <div class="month-box">
                        <p>12개월</p>
                        <button @click="change12(savings)" class="custombutton">
                            <i :class="{'fa-solid': true, 'fa-caret-up': true, 'fa-rotate-180': !align12}"></i>                  
                        </button>
                    </div>
                </th>
                <th>
                    <div class="month-box">
                        <p>24개월</p>
                        <button @click="change24(savings)" class="custombutton">
                            <i :class="{'fa-solid': true, 'fa-caret-up': true, 'fa-rotate-180': !align24}"></i>                  
                        </button>
                    </div>
                </th>
                <th>
                    <div class="month-box">
                        <p>36개월</p>
                        <button @click="change36(savings)" class="custombutton">
                            <i :class="{'fa-solid': true, 'fa-caret-up': true, 'fa-rotate-180': !align36}"></i>                  
                        </button>
                    </div>
                </th>
            </tr>
            </thead>
            <tbody>
                <tr v-for="saving in savings" :key="saving.fin_prdt_cd">
                    <td>
                        <RouterLink :to="{ name:'SavingView', params: { id: saving.fin_prdt_cd } }">{{ saving.deposit_name }}</RouterLink>
                    </td>
                    <td>
                        {{ saving.bank_name }}
                    </td>
                    <td>
                        {{ saving.option6 }}
                    </td>
                    <td>
                        {{ saving.option12 }}
                    </td>
                    <td>
                        {{ saving.option24 }}
                    </td>
                    <td>
                        {{ saving.option36 }}
                    </td>
                </tr>
            </tbody>
        </table>    
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

defineProps({
    savings : {
        type: Object
    }
})

const align6 = ref(true)
const align12 = ref(true)
const align24 = ref(true)
const align36 = ref(true)

const change6 = function(savings) {
    if (align6.value == true) {
        align6.value = false
        savings.sort((a, b) => {
            const valueA = a.option6 === "-" ? Number.MIN_VALUE : parseFloat(a.option6);
            const valueB = b.option6 === "-" ? Number.MIN_VALUE : parseFloat(b.option6);

        return valueA - valueB
    })} else {
        align6.value = true
        savings.sort((a, b) => {
            const valueA = a.option6 === "-" ? Number.MIN_VALUE : parseFloat(a.option6);
            const valueB = b.option6 === "-" ? Number.MIN_VALUE : parseFloat(b.option6);

        return valueB - valueA
    })}
}

const change12 = function(savings) {
    if (align12.value == true) {
        align12.value = false
        savings.sort((a, b) => {
            const valueA = a.option12 === "-" ? Number.MIN_VALUE : parseFloat(a.option12);
            const valueB = b.option12 === "-" ? Number.MIN_VALUE : parseFloat(b.option12);

        return valueA - valueB
    })} else {
        align12.value = true
        savings.sort((a, b) => {
            const valueA = a.option12 === "-" ? Number.MIN_VALUE : parseFloat(a.option12);
            const valueB = b.option12 === "-" ? Number.MIN_VALUE : parseFloat(b.option12);

        return valueB - valueA
    })}
}

const change24 = function(savings) {
    if (align24.value == true) {
        align24.value = false
        savings.sort((a, b) => {
            const valueA = a.option24 === "-" ? Number.MIN_VALUE : parseFloat(a.option24);
            const valueB = b.option24 === "-" ? Number.MIN_VALUE : parseFloat(b.option24);

        return valueA - valueB
    })} else {
        align24.value = true
        savings.sort((a, b) => {
            const valueA = a.option24 === "-" ? Number.MIN_VALUE : parseFloat(a.option24);
            const valueB = b.option24 === "-" ? Number.MIN_VALUE : parseFloat(b.option24);

        return valueB - valueA
    })}
}

const change36 = function(savings) {
    if (align36.value == true) {
        align36.value = false
        savings.sort((a, b) => {
            const valueA = a.option36 === "-" ? Number.MIN_VALUE : parseFloat(a.option36);
            const valueB = b.option36 === "-" ? Number.MIN_VALUE : parseFloat(b.option36);

        return valueA - valueB
    })} else {
        align36.value = true
        savings.sort((a, b) => {
            const valueA = a.option36 === "-" ? Number.MIN_VALUE : parseFloat(a.option36);
            const valueB = b.option36 === "-" ? Number.MIN_VALUE : parseFloat(b.option36);

        return valueB - valueA
    })}
}
</script>

<style scoped>

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0px 4px 8px rgba(201, 201, 201, 0.9);
}

th, td {
  text-align: center;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

table thead {
  background-color: #f9e9a9; /* 배경색 */
  font-size: 19px;
}

table thead th {
  padding: 10px; /* 패딩 */
}

tbody tr:hover {
  background-color: #f4f4f4;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

td a {
  color: darkblue;
  text-decoration: none;
}

td a:hover {
  text-decoration: underline;
}
.article-table-title {
    width: 60%;
}
.custombutton {
    border: none;
    background: none;
}
.month-box {
    display: flex;
    flex-direction: row;
    align-items: center;
}
.month-box p {
    margin: 0; 
    white-space: nowrap;
}

</style>