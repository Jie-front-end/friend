<template>
 <div class="center">
  <el-card class="card">
  <div slot="header">
    <strong><i class="iconfont icon-icon_jiaoyou iconStyle"/> 登录</strong>
  </div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="80px" class="demo-ruleForm">
      <el-form-item label="用户名" prop="login_name">
        <el-input v-model.number="ruleForm.login_name"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="login_pwd">
        <el-input type="password" v-model="ruleForm.login_pwd" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item style="text-align:left">
        <el-button size="small" type="primary" @click="submitForm('ruleForm')">登录</el-button>
        <el-button size="small" @click="register()">注册</el-button>
        <el-button style="margin-left:0px" type="text" @click="foget()">忘记密码</el-button>
      </el-form-item>
    </el-form>
  </el-card>
 </div>
</template>

<script>
import { postAction, getAction } from '@/api/manage'
export default {
  data () {
    return {
      ruleForm: {
        login_name: '',
        login_pwd: ''
      },
      rules: {
        login_pwd: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ],
        login_name: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    foget () {
      this.$router.push({ name: 'ForgetCode' })
    },
    submitForm () {
      const url = '/user/login'
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
          this.$store.commit('SET_LOGIN_NAME', this.ruleForm.login_name)
          postAction(url, this.ruleForm).then(res => {
            if (res.data.code === 200) {
              this.$store.commit('SET_LOGIN_NAME', this.ruleForm.login_name)
              this.$router.push({ name: 'Home' })
            } else {
              this.$message.warning(res.data.msg)
            }
          }).catch(err =>{
             this.$message.warning('注册名密码错误')
          })
        }
      })
    },
    register () {
      this.$router.push({ name: 'Register' })
    }
  }
}
</script>
<style scoped>
.center{
   display: flex;
   height: 90vh;
   justify-content: center;
   align-items: center;
}
.card{
  width: 90%;
  padding: 30px;
}
.iconStyle{
  color:#F6903D;
  font-size: 18px;
}
</style>
