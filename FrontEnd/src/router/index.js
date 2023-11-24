import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import MapView from '@/views/MapView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import UpdatePWView from '@/views/UpdatePWView.vue'
import MainView from '@/views/MainView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MyPageView from '@/views/MyPageView.vue'
import UpdateUserView from '@/views/UpdateUserView.vue'
import RecommendationView from '@/views/RecommendationView.vue'
import BankingView from '@/views/BankingView.vue'
import DepositView from '@/views/DepositView.vue'
import SavingView from '@/views/SavingView.vue'
import RentalLoanView from '@/views/RentalLoanView.vue'
import UpdateArticleView from '@/views/UpdateArticleView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
    },
    {
      path: '/articles/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/article/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/article/update/:id',
      name: 'UpdateArticleView',
      component: UpdateArticleView
    },
    {
      path: '/create/',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/map/',
      name: 'MapView',
      component: MapView,
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/passwordchange',
      name: 'PWUpdateView',
      component: UpdatePWView
      },
      {path: '/exchange/',
      name: 'ExchangeView',
      component: ExchangeView
    },
    {
      path: '/mypage/:username',
      name: 'MyPageView',
      component: MyPageView
    },
    {
      path: '/userchange',
      name: 'UserUpdateView',
      component: UpdateUserView
    },
    {
      path: '/recommendation',
      name: 'RecommendationView',
      component: RecommendationView
    },
    {
      path: '/bankings/:content',
      name: 'BankingView',
      component: BankingView
    },
    {
      path: '/bankings/deposit/:id',
      name: 'DepositView',
      component: DepositView
    },
    {
      path: '/bankings/saving/:id',
      name: 'SavingView',
      component: SavingView
    },
    {
      path: '/bankings/rentalloan/:id',
      name: 'RentalLoanView',
      component: RentalLoanView
    },
  ]
})

import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'CreateView' && !store.isLogin) {
    window.alert('로그인이 필요합니다')
    return {name:'LogInView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && store.isLogin){
    window.alert('이미 로그인 했습니다!')
    return {name: 'ArticleView'}
  }
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'RecommendationView' && !store.isLogin) {
    window.alert('로그인이 필요합니다')
    return {name:'LogInView'}
  }
})


router.beforeEach((to,from) => {
  const store = useCounterStore()
  if (to.name === 'CreateView' && from.name === 'ArticleView') {
    store.getArticles()
  }
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name == 'BankingView') {
      if (to.params.content == 'deposit') {
        store.selectedbanking = '예금 보기'
      } else if (to.params.content == 'saving') {
        store.selectedbanking = '적금 보기'
      } else if (to.params.content == 'rentalloan') {
        store.selectedbanking = '대출 보기'
      }
  }
})

export default router
