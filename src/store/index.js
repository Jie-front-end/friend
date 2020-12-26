import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login_name: sessionStorage.getItem('login_name') || '',
    nickname: sessionStorage.getItem('nickname') || ''
  },
  mutations: {
    SET_LOGIN_NAME: (state, name) => {
      state.loginName = name
      sessionStorage.setItem('login_name', name)
    },
    SET_Nick_NAME: (state, nickname) => {
      state.nickname = nickname
      sessionStorage.setItem('nickname', nickname)
    }
  },
  actions: {
  },
  modules: {
  }
})
