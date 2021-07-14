import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex';
import vuetify from "./plugins/vuetify.js"
import router from "./router/router.js"
import store from './store'

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App), // templateレンダリング
}).$mount('#app') // htmlにappとしてマウントする