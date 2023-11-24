<template>
    <div class="info">
        <div class="greeting">
            <h3>반가워요,</h3>
            <h1>{{ user.username }}님!</h1>
        </div>
        
        <div class="basic-info">
            <p>여기서 기본적인 정보를 확인하세요</p>
            <p>아이디: {{ user.username }}</p>
            <p>email: {{ user.email }}</p>
            <p>닉네임: {{ user.nickname }}</p>
        </div>

        <!-- <div class="additional-info">
            <div>
                <p>몰라ㅏㅏ..........</p>
            </div>
        </div> -->
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
defineProps({
    user : {
        type: Object
    }
})
</script>

<style scoped>
    .info {
        padding: 50px 20px;
        display: flex;
        flex-direction: column;
        align-content: center;
    }
    .greeting h3 {
    color: #000;
    font-size: 1.5em; /* Make the greeting stand out */
    }

    .greeting h1 {
    color: #000;
    font-size: 2.5em; /* Larger font for the main greeting */
    }

    .basic-info {
    background-color: #f0f8ff; /* Light blue background for the info area */
    border-left: 5px solid rgba(160, 159, 159, 0.685); /* Blue left border for emphasis */
    padding: 1em;
    margin-top: 1em;
    border-radius: 8px; /* Rounded corners for the info boxes */
    }

    .basic-info p {
    color: #000;
    font-size: 1em;
    margin: 0.5em 0; /* Spacing between paragraphs */
    }

    /* Add additional styling for buttons and inputs as per the image */
    input, select, button {
    font-size: 1em;
    margin: 0.5em 0; /* Spacing between form elements */
    padding: 0.5em;
    }

    button {
    background-color: #add8e6; /* Light blue background for buttons */
    color: #fff;
    border: none;
    border-radius: 20px; /* Rounded corners for buttons */
    padding: 0.5em 1em;
    cursor: pointer; /* Cursor changes to pointer on hover over button */
    }

    button:hover {
    background-color:  rgb(224, 188, 110); /* Button color changes to blue on hover */
    }

    /* Responsive design adjustments */
    @media (max-width: 768px) {
    .greeting h1 {
        font-size: 2em; /* Smaller font size for mobile */
    }

    .basic-info, input, select, button {
        margin-top: 0.5em;
    }
    }

</style>