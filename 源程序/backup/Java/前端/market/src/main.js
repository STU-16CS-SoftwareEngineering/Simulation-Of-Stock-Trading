// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import 'normalize.css'
import Vuex from 'vuex'
import CKEditor from '@ckeditor/ckeditor5-vue';
Vue.use( CKEditor );
import axios from "axios";

Vue.use(ElementUI)
Vue.config.productionTip = false
axios.defaults.baseURL = 'http://localhost:8081/'
Vue.prototype.axios = axios

Vue.use(Vuex)
const store = new Vuex.Store({
  state: {
    account: ''
  },
  mutations: {
    updateUserName (state, account) {
      state.account = account;
    }
  }
})

//Date的prototype 属性可以向对象添加属性和方法。   
Date.prototype.Format = function(fmt){
  var o = {
      "M+": this.getMonth()+1,
      "d+": this.getDate(),
      "H+": this.getHours(),
      "m+": this.getMinutes(),
      "s+": this.getSeconds(),
      "S+": this.getMilliseconds()
  };
  //因为date.getFullYear()出来的结果是number类型的,所以为了让结果变成字符串型，下面有两种方法：
  if(/(y+)/.test(fmt)){
      //第一种：利用字符串连接符“+”给date.getFullYear()+""，加一个空字符串便可以将number类型转换成字符串。
      fmt=fmt.replace(RegExp.$1,(this.getFullYear()+"").substr(4-RegExp.$1.length));
  }
  for(var k in o){
      if (new RegExp("(" + k +")").test(fmt)){
          //第二种：使用String()类型进行强制数据类型转换String(date.getFullYear())，这种更容易理解。
          fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(String(o[k]).length)));
      }
  }
  return fmt;
};

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
