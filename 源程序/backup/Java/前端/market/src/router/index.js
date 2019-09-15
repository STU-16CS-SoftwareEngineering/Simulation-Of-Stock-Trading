import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/Login'
import Match from '@/views/Match'
import addMatch from '@/views/AddMatch'
import MatchDetail from '@/views/MatchDetail'
import ModifyDetail from '@/views/ModifyMatch'
import blacklist from '@/views/blacklist/BlackList'
import addBlacklist from '@/views/blacklist/AddBlackList'
import log from '@/views/Log/LogList'
import wxUser from '@/views/User/UserList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/match',
      name: 'Match',
      component: Match
    },
    {
      path: '/addMatch',
      name: 'addMatch',
      component: addMatch
    },
    {
      path: '/MatchDetail',
      name: 'MatchDetail',
      component: MatchDetail
    },
    {
      path: '/ModifyDetail',
      name: 'ModifyDetail',
      component: ModifyDetail
    },
    {
      path: '/blacklist',
      name: 'blacklist',
      component: blacklist
    },
    {
      path: '/addBlacklist',
      name: 'addBlacklist',
      component: addBlacklist
    },
    {
      path: '/log',
      name: 'log',
      component: log
    },
    {
      path: '/wxUser',
      name: 'wxUser',
      component: wxUser
    }
  ]
})
