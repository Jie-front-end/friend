<template>
 <div class="container">
  <el-card >
  <div slot="header">
    <strong>忘记密码</strong>
  </div>
    <el-form class="mt20" ref="form" :rules="rules" :model="form" label-width="200px" label-position="top" label-suffix=":">
      <el-form-item label="用户名" prop="login_name">
        <el-input v-model.number="form.login_name"></el-input>
      </el-form-item>
      <el-form-item label="联系方式" prop="contact">
        <el-input v-model="form.phone" placeholder="请输入联系方式"></el-input>
      </el-form-item>
      <el-form-item label="出生时间" prop="date">
        <div class="form-description">八字排盘需要，填写阳历生日，最好能够准确到分如果实在不清楚精确到小时也可以。</div>
        <el-col :span="11">
          <el-date-picker
            type="date"
            value-format="yyyy-MM-dd"
            placeholder="请选择阳历生日"
            v-model="form.date"
            style="width: 100%;"
          ></el-date-picker>
        </el-col>
        <el-col class="tr" :span="2">-</el-col>
        <el-col :span="11">
          <el-time-picker
            placeholder="选择时间"
            value-format="HH:mm:ss"
            v-model="form.time"
            style="width: 100%;"
          ></el-time-picker>
        </el-col>
      <el-form-item label="出生地(省市)" prop="city">
        <el-input v-model="form.city" placeholder="请输入出生地"></el-input>
      </el-form-item>
      </el-form-item>
      <div class="tr mt40">
        <el-button type="primary" style="width: 100%;" @click="onSubmit">提交</el-button>
      </div>
    </el-form>
    <el-dialog
      title="请输入密码"
      :visible.sync="messageVisial"
      width="80%"
      >
      <el-form :model="ruleForm" status-icon :rules="codeRules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="密码" prop="pass">
            <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="checkPass">
            <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
    </el-form>
      <div class="tr mt20">
        <el-button type="primary" size="small" @click="messageVisial = false">确 定</el-button>
      </div>
    </el-dialog>
  </el-card>
 </div>
</template>
<script>
import { postAction } from '@/api/manage'
export default {
  data () {
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.ruleForm.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
    return {
      messageVisial:false,
      form: {
        login_name: '',
        phone: '',
        date: '',
        time: '',
        city: ''
      },
      ruleForm: {
          pass: '',
          checkPass: ''
      },
      rules: {
        login_name: [{ required: true, message: '输入不能为空', trigger: 'blur' }],
        phone: [{required: true, message:"输入不能为空", trigger: 'blur' }],
        date: [{ required: true, message: '输入不能为空', trigger: 'blur' }],
        time: [{ required: true, message: '输入不能为空', trigger: 'blur' }],
        city: [{ required: true, message: '输入不能为空', trigger: 'blur' }]
      },
      codeRules: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ]
        }
    }
  },
  methods: {
    onSubmit () {
      const url = '/user/forget/first'
      this.$refs.form.validate((valid) => {
        if (valid) {
          const date = this.form.date
          const time = this.form.time
          this.form.year = date.split('-')[0]
          this.form.month = date.split('-')[1]
          this.form.day = date.split('-')[2]
          this.form.hour = date.split(':')[0]
          this.form.minute = date.split(':')[1]
          postAction(url, this.form).then(res => {
            if (res.code == 200) {
              this.$message.success(res.mag)
              this.messageVisial = true
            //   this.$router.push({ name: 'Login' })
            } else {
              this.$message.warning(res.mag)
            }
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    submitForm(formName) {
        const url = '/user/forget/second'
        this.$refs[formName].validate((valid) => {
          if (valid) {
           postAction(url, { pwd:this.ruleForm.checkPass }).then(res => {
            if (res.code == 200) { 
              this.$message.success(res.mag)
              this.messageVisial = false
              this.$router.push({ name: 'Login' })
            } else {
              this.$message.warning(res.mag)
            }
          })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
    },
    resetForm(formName) {
    this.$refs[formName].resetFields();
    }
  }
}
</script>
<style >
.container {
   text-align: justify;
   width: 100%;
   max-width: 800px;
   margin-right: auto;
   margin-left: auto;
   /* padding-left: 16px;
   padding-right: 16px; */
}
.el-form-item__label{
  font-weight: bold;
  font-size: 1em ;
}
.el-form--label-top .el-form-item__label {
    float: none;
    display: inline-block;
    text-align: left;
    padding: 0px;
}
.el-form-item__content{
  font-size: 0.95em ;
}
.title{
  color: #409EFF;
  text-align: center;
  margin: 16px 0px;
}
.tr{
  text-align: center;
}
.mt20{
  margin-top: 24px;
}
.mt40{
  margin-top: 40px;
}
.form-description{
  color: rgba(0,0,0,0.6);
  font-size:0.9em;
  line-height: 1.75em;
  padding: 2px;
}
</style>
