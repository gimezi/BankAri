// import '@/assets/fonts.css'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()
// localStorage.clear()

app.use(router)
pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.mount('#app')