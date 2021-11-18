import Vue from 'vue'
import Router from 'vue-router'
import CYK from '@/components/cyk/CYK'
import FSM from '@/components/fsm/FSM'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/cyk',
      name: 'CYK',
      component: CYK
    },
    {
      path: '/fsm',
      name: 'FSM',
      component: FSM
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    }
  ],
  mode: 'history'
})
