<template>
 <div class="container">
  <el-card >
  <div slot="header">
    <strong>注册</strong>
  </div>
    <el-form class="mt20" ref="form" :rules="rules" :model="form" label-width="200px" label-position="top" label-suffix=":">
      <el-form-item label="用户名" prop="login_name">
        <el-input v-model.number="form.login_name"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="pwd">
        <el-input type="password" v-model="form.pwd" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="昵称" prop="nickname">
        <el-input v-model="form.nickname" placeholder="请输入昵称"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="sex">
         <el-radio-group v-model="form.sex" style="width: 100%;" placeholder="请选择性别">
           <el-radio label="男"></el-radio>
           <el-radio label="女"></el-radio>
        </el-radio-group>
      </el-form-item>
      <!-- <el-form-item label="联系方式" prop="contact">
        <div class="form-description">方便大家再次咨询时快速反馈，请填一下信息，微信或者qq都可以，eg. zxzmls(微信)。</div>
        <el-input v-model="form.contact" placeholder="请输入联系方式"></el-input>
      </el-form-item> -->
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
      </el-form-item>
      <el-form-item label="出生地(省市)" prop="city">
        <el-input v-model="form.city" placeholder="请输入出生地"></el-input>
      </el-form-item>
      <!-- <el-form-item label="婚否" prop="marriage">
        <el-radio-group v-model="form.marriage" style="width: 100%;">
           <el-radio label="已婚"></el-radio>
           <el-radio label="未婚"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="工作" prop="job">
        <div class="form-description">可以具体填写，如：会计。也可以指出行业，如：金融行业。可以为您提供适合自己五行命格与喜用神的参考意见。</div>
        <el-input v-model="form.job" placeholder="请输入工作"></el-input>
      </el-form-item> -->
      <div class="tr mt40">
        <el-button type="primary" style="width: 100%;" @click="onSubmit">注册</el-button>
      </div>
    </el-form>
  </el-card>
 </div>
</template>

<script>
import { postAction } from '@/api/manage'
  export default {
    data() {
      return {
        form: {
          login_name: '',
          pwd: '',
          nickname: '',
          sex: '',
          // contact: '',
          date: '',
          time:'',
          city: '',
          // marriage: '',
          // job: ''
        },
        rules: {
          login_name: [{required: true, message:"输入不能为空", trigger: 'blur' }],
          pwd: [{required: true, message:"输入不能为空", trigger: 'blur' }],
          nickname: [{required: true, message:"输入不能为空", trigger: 'blur' }],
          sex: [{required: true, message:"输入不能为空", trigger: 'blur' }],
          // contact: [{required: true, message:"输入不能为空", trigger: 'blur' }],
          date: [{required: true, message:"输入不能为空", trigger: 'blur' }],
          time: [{required: true, message:"输入不能为空", trigger: 'blur' }],
          city: [{required: true, message:"输入不能为空", trigger: 'blur' }]
          // job: [{required: true, message:"输入不能为空", trigger: 'blur' }]
        }
      };
    },
    methods: {
      onSubmit() {
        const url = '/user/register'
        this.$refs.form.validate((valid) => {
          if (valid) {
            const date = this.form.date
            const time = this.form.time
            this.form.year = date.split("-")[0]
            this.form.month = date.split("-")[1]
            this.form.day = date.split("-")[2]
            this.form.hour = date.split(":")[0]
            this.form.minute = date.split(":")[1]
            postAction( url, this.form).then( res => {
                if( res.code == 200) {
                  this.$message.success(res.mag)
                  this.$router.push({name: 'Login'})
                }
                else{
                  this.$message.warning(res.mag)
                }
            })

          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
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
