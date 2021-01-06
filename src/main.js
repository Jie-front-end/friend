import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import element from './element/index'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/iconfont/iconfont.css'
import './assets/scss/style.scss'
Vue.config.productionTip = false
// 引入基本模板
// const echarts = require('echarts/lib/echarts')
import VueClipboard from 'vue-clipboard2';
// 引入柱状图组件
// require('echarts/lib/chart/bar')
// // 引入提示框和title组件
// require('echarts/lib/component/tooltip')
// require('echarts/lib/component/title')
// Vue.prototype.$echarts = echarts
Vue.use(element)
Vue.use(VueClipboard);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
