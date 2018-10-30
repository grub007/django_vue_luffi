// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

// 导入vue
import Vue from 'vue'

//这边其实导入了App.vue,但由于webpack进行了优化所以这边简写成了App
import App from './App'

//导入router文件夹,其实webpack也进行了优化其实是导入了router文件夹下的所有文件
import router from './router'

//导入vuex， vuex需要额外下载 npm install vuex --save
import Vuex from "vuex"


//引入antd design组件
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
Vue.use(Antd);
Vue.config.productionTip = false;


// 将Vuex与vue进行关联
Vue.use(Vuex);

//引用axios, 全局设置axios的baseurl
import axios from "axios"
axios.defaults.baseURL = 'http://127.0.0.1:8000';
Vue.prototype.$axios = axios;

// 引入element-ui, 该模块相当于bootstrap组件，需要单独下载npm i element-ui -S
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI, { size: 'small', zIndex: 3000 });


// 引入vue-cookie
import Cookie from 'vue-cookies';

// 实列化vue store对象, store就是存放所有数据的容器
const store = new Vuex.Store({
  state: {
     courseDetail: [],
    currentCourseListInfo: {},
    headerSelectInit: ["1"],
    // 设置课程列表的初始选择的key id
    courseListSelectInit: ["1"],
    detailCourseInfo: {},
    // 从cookie中获取token
    username: Cookie.get("username"),
    token: Cookie.get("token")
  },
  mutations: {
      GETCOURSELIST(state, courselist){
        state.courseDetail = courselist;
        // 更新数组元素时必须
        state.courseListSelectInit[0] = courselist[0].id.toString()
      },
      getCourseDetailInfo(state, data){
        state.detailCourseInfo = data
      },
      saveToken(state, userToken){
        state.username = userToken.username;
        state.token = userToken.token;
        // 将token写入cookie中，并设置超时时间为20分钟
        Cookie.set("username", userToken.username, "20min");
        Cookie.set("token", userToken.token, "20min")
      },
      clearToken(state){
        state.username = null;
        state.token = null;
        Cookie.remove("username");
        Cookie.remove("token")
      }
  },
  // 创建actions，actions内的操作都为异步操作
  actions: {
    getCourseList(context, data){
      context.commit("GETCOURSELIST", data)
    },
    getCourseDetailInfo(context, courseid){
        axios.request({
           method: "GET",
           url: `/api/course/${courseid}`,
           headers: {
            "token": context.state.token
          }
        }).then(function(ret){
            if (ret.data.code == 1000 && ret.data.data){
               context.commit("getCourseDetailInfo", ret.data.data)
            }
        }).catch(function(err){

        })
    }
  }
})


// 该配置是vue生产环境的一个配置文件，如果不配置也没什么影响
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  //将router对象挂载到Vue对象,这边的router相当于router:router
  router,
  //将store挂载到当前vue对象,其他组件可以通过this.$store来访问该对象
  store,
  // 这边的components是vue的主组件其挂载的router对象必须在App组件中调用
  components: { App },
  template: '<App/>'
})

// vue拦截器, to表示去哪个Url, from表示从那个url过来的, next标识跳转
router.beforeEach(function(to, from, next){
  // 判断去往的URL是否必须要登录
  if(to.meta.requireAuth){
     // 如果必须要登录则判断当前的token是否存在
     if (store.state.token){
       next()
     }else{
        //如果没有获取到token则跳转到登录页面
        next({path: "/login", query: {backUrl: to.fullPath}})
     }
  }else{
    next()
  }
})