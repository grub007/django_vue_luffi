<template>
  <div id="app">
    <Vheader></Vheader>
    <!-- App组件中调用router对象，必须执行该步骤否则router内容无法在页面中显示 -->
    <router-view/>
    <a-layout-footer style="text-align: center">
      Ant Design ©2018 Created by Ant UED
    </a-layout-footer>
  </div>
</template>

<script>
import Vheader from "@/components/vheader"

export default {
  name: 'App',
  components: {
    Vheader
  },
  
  //加页面加载完成后到后台请求数据
  mounted(){
      
  },
  // created方法是页面加载之前调用该方法
  created(){
   
  }
}
</script>

<style>

</style>
