<template>
    <a-layout>
        <a-layout-sider width="200" style="background: #fff">
            <a-menu
          mode="inline"
          :defaultSelectedKeys="defaultSelectKey"
          :defaultOpenKeys="['sub1']"
          :style="{ height: '100%', borderRight: 0 }"
        >
          <a-sub-menu key="sub1">
            <span slot="title"><a-icon type="user" />课程列表</span>
            <a-menu-item v-for="item in courseDetail" :key="item.id.toString()" @click="clickHandle(item)">
                <router-link :to="{name:'coursedetail', params:{id:item.id}}">{{item.title}}</router-link>
            </a-menu-item>
          </a-sub-menu>
        </a-menu>
        </a-layout-sider>
        <!-- router-view就像一个视图这边嵌套在课程页里面 -->
        <router-view></router-view>
    </a-layout>   

</template>


<script>
export default {
    name: "Course",
    data(){
        return {
            
        }
    },
    methods: {
        // 切换路由方法，根据切换的路由获取当前url对象
       clickHandle(item){
           this.$store.state.currentCourseListInfo = item;
           this.$store.dispatch("getCourseDetailInfo", this.$route.params.id)
       } 
    },
    computed: {
        courseDetail: {
            set: function(newvalue){
                this.$store.state.courseDetail = newvalue;
            },
            get: function(){
                return this.$store.state.courseDetail
            }
        },
        defaultSelectKey: {
            set: function(newvalue){
                this.$store.state.courseListSelectInit = newvalue
            },
            get: function(){
                return this.$store.state.courseListSelectInit
            }
        }
    },
    created(){
        //在重新刷新页面后设置课程详细列表选中值
        // this.$store.dispatch("getCourseList");
        var this_ = this
        this.$axios.request({method:'GET',
         url: "/api/course/", 
         headers: {
             "token": this.$store.state.token
         }
         }).then(function(res){
          if (res.data.code == 1000 && res.data.data){
            this_.$store.dispatch("getCourseList", res.data.data);
            // 让在点击课程详情时自动跳转到linux课程的url
            let redictUrl = res.data.data[0].id;
            this_.$router.push(`/course/detail/${redictUrl}`);
            this_.$store.dispatch("getCourseDetailInfo", redictUrl)
          }else{
              console.log(res.data)
          }
       }).catch(function(err){
            console.log(err)
       });
    },
    mounted(){
        
    }
}
</script>

<style scoped>

</style>


