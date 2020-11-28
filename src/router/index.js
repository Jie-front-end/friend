import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '@/layout'
import Message from '../views/message.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import(/* webpackChunkName: "about" */ '../views/login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import(/* webpackChunkName: "about" */ '../views/register.vue')
  },
  {
    path: '/friend',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'Home',
        component: () => import(/* webpackChunkName: "about" */ '../views/home.vue')
      }
    ]
  },
  {
    path: '/message',
    name: 'Message',
    component: () => import(/* webpackChunkName: "about" */ '../views/message.vue')
  },
  {
    path: '/messageList',
    component: Message,
    children: [
      {
        path: 'index',
        name: 'MessageList',
        component: () => import(/* webpackChunkName: "about" */ '../views/messageList.vue')
      }
    ]
  },
  {
    path: '/messageDetail',
    component: Message,
    children: [
      {
        path: 'index',
        name: 'messageDetail',
        component: () => import(/* webpackChunkName: "about" */ '../views/messageDetail.vue')
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
        component: () => import(/* webpackChunkName: "about" */ '../views/myself.vue')
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
        component: () => import(/* webpackChunkName: "about" */ '../views/match.vue')
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
        component: () => import(/* webpackChunkName: "about" */ '../views/matchResult.vue')
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
