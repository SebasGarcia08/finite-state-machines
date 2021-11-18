import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import CYK from '@/components/CYK'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/cyk',
      name: 'CYK',
      component: CYK
    }
  ],
  mode: 'history'
})
