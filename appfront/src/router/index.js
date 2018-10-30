import Vue from 'vue'
import Router from 'vue-router'

// import Vmain from "@/components/vmain"
// import Vnote from "@/components/vnote"

import Index from "@/components/index"
import Micro from "@/components/micro"
import News from "@/components/news"
import Course from "@/components/course"
import CourseDetail from "@/components/coursedetail"
import Login from "@/components/login"


//Vue实例化对象注册Router对象
Vue.use(Router)

export default new Router({
  // 这边的key必须为routes
  routes: [
    {
      path: '/index',
      name: 'Index',
      // 一个routes对应一个组件
      component: Index
    },
    {
      path: '/login',
      name: 'Login',
      // 一个routes对应一个组件
      component: Login
    },
    {
      path: '/course',
      name: 'Course',
      // 一个routes对应一个组件
      component: Course,
      // children为子路由，detail/:id失通过CourseDetail组件中循环的数据来给id传值
      children: [
        {
          path: "detail/:id",
          name: "coursedetail",
          component: CourseDetail,
          meta: {
            requireAuth: true
          }
      },
      ],
      // 给课程url详情添加必须登录才能访问的标识
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/micro',
      name: 'Micro',
      // 一个routes对应一个组件
      component: Micro
    },
    {
      path: '/news',
      name: 'News',
      // 一个routes对应一个组件
      component: News
    }
  ]
})
