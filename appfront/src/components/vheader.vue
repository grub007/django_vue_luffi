<template>
  <a-layout>
    <a-layout-header class="header">
      <div class="logo"/>
      <!-- 通过v-model来实现哪一个标签实现选中 -->
      <a-menu
        theme="dark"
        mode="horizontal"
        v-model="selectValueinfo"
        :defaultSelectedKeys="selectValueinfo"
        :style="{ lineHeight: '64px' }"
      >
        <!-- 这边给key传的值必须是字符串 -->
        <a-menu-item v-for="item in titleList" :key="item.id.toString()">

          <router-link :to="item.url">{{item.title}}</router-link>
        </a-menu-item>
        <a-menu-item>
          <!-- 判断token是否获取了,如果获取了则直接显示用户名称 -->
          <div v-if="Token"><span>{{User}}</span><span class="logout" @click="Logout()">注销</span> </div>
          <router-link v-else to="/login">登录</router-link>
          
          </a-menu-item> 
        
      </a-menu>
      
    </a-layout-header>
  </a-layout>
</template>

<script>
export default {
    name: "Vheader",
    data(){
        return {
          titleList: [
              {id:1, url: "/index", title:"首页"},
              {id:2, url: "/course", title:"课程"},
              {id:3, url: "/micro", title:"微职位"},
              {id:4, url: "/news", title:"深科技"},
              //  {id:5, url: "/login", title:"登录"},

          ],

        }
    },
    mounted(){
       
    },
    created(){
       for (let i=0;i<this.titleList.length;i++){
           let urlInfo = this.$route.path;
           urlInfo = "/" + urlInfo.split("/")[1];
           if (this.titleList[i].url == urlInfo){
               this.selectValueinfo = [(i+1).toString()]
               return
           }
       }
    },
    computed: {
      Token: {
            get: function(){
                return this.$store.state.token
            }
        },
      User: {
        get: function(){
                return this.$store.state.username
            }
      },
      selectValueinfo: {
          get: function(){
              return this.$store.state.headerSelectInit
          },
          set: function(newvaule){
              this.$store.state.headerSelectInit = newvaule
          }
      }
    },
    methods: {
      Logout(){
        // 调用注销逻辑，删除cookie中的token
        this.$store.commit("clearToken");
        // 注销登录页面后强制跳转到登录页面
        this.$router.push('/login');
      }
    }
}
</script>


<style scoped>
  .logout {
    margin-left: 20px
  }
</style>


