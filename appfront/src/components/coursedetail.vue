<template>
    <a-layout style="padding: 0 24px 24px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>{{"课程"}}</a-breadcrumb-item>
          <a-breadcrumb-item>{{"课程列表"}}</a-breadcrumb-item>
          <a-breadcrumb-item>{{breadcrumbInfo.title}}</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }">
            <a-row>
                <h3>标题:{{detailCourseInfo.slogon}}</h3> 
            </a-row>
            <a-row>
                {{detailCourseInfo.img}}
            </a-row>
            <a-row>
                {{detailCourseInfo.why}}
            </a-row>
            <a-row>
                {{detailCourseInfo.level}}
            </a-row>
            <a-row>
                <h2>章节详情:</h2>
            </a-row>
             <a-row v-for="item in detailCourseInfo.chapter" :key="item.id">
                <p>{{item.num}}. {{item.name}}</p>
            </a-row>
            <a-row>
                <h2>推荐课程:</h2>
            </a-row>
             <a-row v-for="item in detailCourseInfo.recommend_courses" :key="item.id">
               <a @click="handleChange(item.id)">{{item.title}}</a>
            </a-row>
        </a-layout-content>
      </a-layout>
</template>


<script>
export default {
    name: "Coursedetail",
    data(){
        return {
            
        }
    },
    methods: {
        handleChange(id){
            this.$store.dispatch("getCourseDetailInfo", id);
            // 重定向到对应的课程详细URL
            this.$router.push(`/course/detail/${id}`);
            // 重新对select标签选中的值进行复制，必须这样通过index来赋值，不然VUE检测不到数据发生了变更
            this.$store.state.courseListSelectInit[0] = id.toString();
        }
    },
    computed: {
        breadcrumbInfo: {
           set: function(newvalue){
                this.$store.state.currentCourseListInfo = newvalue
           },
           get: function(){
               return this.$store.state.currentCourseListInfo
           }
        },
        detailCourseInfo: {
            set: function(newvalue){
                this.$store.state.detailCourseInfo = newvalue
            },
            get: function(){
                return this.$store.state.detailCourseInfo
            }
        }
    },
    created(){
        // $route.params可以获取到当前URL coursedetail 
        this.$store.dispatch("getCourseDetailInfo", this.$route.params.id);
        for (let i=0;i<this.$store.state.courseDetail.length;i++){
            if (this.$store.state.courseDetail[i].id == this.$route.params.id){
                this.breadcrumbInfo = this.$store.state.courseDetail[i];
                return
            }
        }
    }
}
</script>

<style scoped>

</style>


