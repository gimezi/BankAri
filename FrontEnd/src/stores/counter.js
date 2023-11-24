import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const articles = ref(null)
  const ex_info = ref(null)
  const exchange = ref(null)
  const user = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const nowUserName = ref(null)
  const selectedBank = ref(null)
  const saving_recommproduct = ref(null)
  const deposit_recommproduct = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const nowUserId = ref(null)

  
  // 게시글 가져오기
  const getArticles = function() {
    axios({
      method:'get',
      url: `${API_URL}/api/v1/articles/`,
    }) .then((respones) => {
      // console.log(respones)
      articles.value = respones.data
    }).catch((error) => {
      if (error.response.status == 404) {
        articles.value = null
        console.log('작성된 글이 없습니다!')
      }
    })
  }

  // 유효성 검사 알림창
  const errorMessage = function(res) {
    if (res.includes('This password is too short')) {
      return '비밀번호가 너무 짧습니다. 8자 이상, 특수문자를 포함해야합니다.'
    } else if (res.includes('This password is too common')){
      return '비밀번호가 너무 흔합니다. 8자 이상, 특수문자를 포함해야합니다.'
    }
  }

  // 회원가입
  const signUp = function(payload) {
    const {username, password1, password2, nickname} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname
      }
    }) .then((res) => {
      const password = password1
      console.log(res)
      logIn({username, password}) // 얘한테도 push가 있으니까 안써도 댐
      window.alert('회원가입 완료!')
    })
    .catch((err) => {
      const error = errorMessage(err.request.response)
      window.alert(error)
    })
  }
  
  // 로그인
  const logIn = function(payload) {
    const {username, password} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    }) .then((res) => {
      token.value = res.data.key
      nowUserName.value = username
      nowUserId.value = res.data.user
      console.log(res.data)
      router.push({name: 'MainView'})
    })
    .catch((err) => {console.log(err)
    if (err.request.response.includes('Unable to log in')) {
      window.alert('회원정보를 다시 확인해주세요')
    }
    })
  }
  
  // 비밀번호 변경
  const changePW = function(payload) {
    const {new_password1, new_password2, old_password} = payload
    const username = nowUserName.value
    const password = old_password
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    }) .then((res) => {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,
        data: {
          new_password1, new_password2, old_password
        },
        headers: {
          Authorization: `Token ${token.value}`
        }
      }) .then((res) => {
        router.push({name: 'MainView'})
      }).catch((err) => {
        window.alert('변경 완료되었습니다.')
      })
    }) .catch((err)=> {
      console.log(err)
      const res = err.request.response
      if (res.includes('Unable to log in')) {
        window.alert('비밀번호가 잘못되었습니다')
      }
    }) 
  }


  const get_info = function() {
    if (ex_info.value == null) {
        axios({
          method: 'get',
          url: `${API_URL}/exchange/`,
          // headers: {
          //   Authorization: `Token ${token.value}`
          // }
      }) .then((res) => {
        ex_info.value = res.data
      }) .catch((err) => {
        console.log(err)
      })} else {
        console.log(ex_info.value)
      }
    }
    
  // 환율검색
  const searchEx = function(payload) {
    const{ nation, tot } = payload
    axios({
      method: 'get',
      url: `${API_URL}/exchange/search/${nation}`,
      }) .then((res) => {
      exchange.value = res.data
      console.log(exchange.value)
    }) .catch((err) => {
      console.log(err)
    })}

  // 금융상품 정보 가져오기
  const issaved = ref(false)
  const getBankData = async function() {
    try {
      let res = await axios.get(`${API_URL}/bankings/1/`);
      console.log('첫 번째 요청 성공:', res.data);

      res = await axios.get(`${API_URL}/bankings/2/`);
      console.log('두 번째 요청 성공:', res.data);

      res = await axios.get(`${API_URL}/bankings/3/`);
      console.log('세 번째 요청 성공:', res.data);

      console.log('데이터가 DB에 저장됨!')
      issaved.value = true
    } catch (err) {
      console.log(err);
    }
  }

  // 추천 상품
  const recommend = function(payload) {
    const { age, money, salary } = payload
    axios({
      method: 'post',
      url: `${API_URL}/recommends/recomproducts/`,
      data: {
        age, money, salary
      }
    }) .then ((res) => {
      router.push({name:'MyPageView', param:{username:nowUserName}})
      deposit_recommproduct.value = res.data.deposit
      saving_recommproduct.value = res.data.saving
      
    })
    .catch((err) => {console.log(err)})
  }
  
  return { 
    articles, user ,API_URL, getArticles, 
    signUp, logIn, changePW, token, isLogin, nowUserId, nowUserName,
    ex_info, searchEx ,exchange, get_info, 
    issaved, getBankData, selectedBank ,recommend, saving_recommproduct,deposit_recommproduct }


}, { persist: true })
