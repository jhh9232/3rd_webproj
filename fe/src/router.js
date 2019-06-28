import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/main',
      name: 'main',
      component: () => import('./views/main.vue')
    },
    {
      path: '/join',
      name: 'join',
      component: () => import('./views/join.vue')
    },
    {
      path: '/scrap',
      name: 'scrap',
      component: () => import('./views/scrap.vue')
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: () => import('./views/mypage.vue')
    },
    {
     path:'/block',
     name:'차단'
    }
  ]
})
