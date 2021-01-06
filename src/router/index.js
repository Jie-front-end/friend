import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '@/layout'
import Message from '../views/message.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import(/* webpackChunkName: "Login" */ '../views/login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import(/* webpackChunkName: "Register" */ '../views/register.vue')
  },
  {
    path: '/forgetCode',
    name: 'ForgetCode',
    component: () => import(/* webpackChunkName: "ForgetCode" */ '../views/forgetCode.vue')
  },
  {
    path: '/friend',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'Home',
        component: () => import(/* webpackChunkName: "Home" */ '../views/home.vue')
      }
    ]
  },
  {
    path: '/message',
    name: 'Message',
    component: () => import(/* webpackChunkName: "Message" */ '../views/message.vue')
  },
  {
    path: '/messageList',
    component: Message,
    children: [
      {
        path: 'index',
        name: 'MessageList',
        component: () => import(/* webpackChunkName: "MessageList" */ '../views/messageList.vue')
      }
    ]
  },
  {
    path: '/messageDetail',
    component: Message,
    children: [
      {
        path: 'index',
        name: 'MessageDetail',
        component: () => import(/* webpackChunkName: "MessageDetail" */ '../views/messageDetail.vue')
      }
    ]
  },
  {
    path: '/myself',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'Myself',
        component: () => import(/* webpackChunkName: "Myself" */ '../views/myself.vue')
      }
    ]
  },
  {
    path: '/match',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'Match',
        component: () => import(/* webpackChunkName: "Match" */ '../views/match.vue')
      }
    ]
  },
  {
    path: '/matchResult',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'MatchResult',
        component: () => import(/* webpackChunkName: "MatchResult" */ '../views/matchResult.vue')
      }
    ]
  }
  // {
  //   path: '/myself',
  //   name: 'Myself',
  //   component: () => import(/* webpackChunkName: "about" */ '../views/myself.vue')
  // },
  // {
  //   path: '/message',
  //   name: 'Message',
  //   component: () => import(/* webpackChunkName: "about" */ '../views/message.vue')
  // },
  // {
  //   path: '/match',
  //   name: 'Match',
  //   component: () => import(/* webpackChunkName: "about" */ '../views/match.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
