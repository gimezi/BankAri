<template>
    <div>
        <table>
            <thead>
            <tr>
                <th>대출상품 이름</th>
                <th>은행명</th>
                <th>대출 한도</th>
            </tr> 
            </thead>
            <tbody>
                <tr v-for="rentalloan in rentalloans" :key="rentalloans.fin_prdt_cd">
                    <td>
                        <RouterLink :to="{ name:'RentalLoanView', params: { id: rentalloan.fin_prdt_cd } }">
                        {{ rentalloan.deposit_name }}
                        </RouterLink>
                    </td>
                    <td>
                        {{ rentalloan.bank_name }}
                    </td>
                  <td>
                    <p v-html="rentalloan.loan_lmt.replace(/\n/g,'<br>')"></p>
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
    rentalloans : {
        type: Object
    }
})

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

td p {
    margin: auto;
}
</style>