<template>
    
    <div class="login">
       
        <p>用户名:<input type="text" placeholder="请输入用户名" v-model="username"></p>
        <p>密码:<input type="password" placeholder="请输入密码" v-model="password"></p>
        <button @click="LoginHandle()">登录</button>
    </div>   
</template>

<script>
export default {
    data(){
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        // 发送登录验证请求
        LoginHandle(){
            var this_ = this;
            this.$axios.request({
                method:'POST', 
                url: "/api/auth/",
                data: {
                    username: this_.username,
                    password: this_.password
                },
                headers: {
                    "Content-type": "application/json"
                } 
            }).then(function(args){
                if (args.data.code == 1000){
                    this_.$store.state.token = args.data.token;
                    this_.$store.state.username = this_.username;
                    this_.$store.commit("saveToken", {username: this_.username, token: args.data.token});

                    // 判断是否有backURL, backURL就是那些必须登录才能访问的页面跳转到登录页面的那些URL
                    // 如果没有backURL则跳转到/index主页面
                    var backurl = this_.$route.query.backUrl
                    if (backurl){
                        this_.$router.push(backurl)
                    }else{
                        this_.$store.state.headerSelectInit[0] = "1"
                        this_.$router.push("/index");    
                    }
                }else{
                    console.log(args.data.error)
                }
            }).catch(function(err){
                console.log(err)
            })
        }
    }
}
</script>

<style scoped>
    .login {
        margin-left: 20px;
        margin-top: 20px;
    }
</style>


