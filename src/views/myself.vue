<template>
 <div class="wrapper">
    <!-- <div style="text-align:right">
      <el-button plain @click="toMatch">修改</el-button>
    </div> -->
  <el-card class="box-card" shadow="always" >
        <div style="display:flex;justify-content: space-between;">
          <span class="card-item-head">个人信息</span>
          <el-button icon="el-icon-edit" round size="small" style="color:#FF6B3B" @click="openEditVisual"></el-button>
        </div>
        <div class="mb8">
          <span class="info-title">昵称:</span>
          <span class="info">{{form.nick}}</span>
        </div>
        <div class="mb8">
        <span class="info-title">性别:</span>
        <span class="info">{{form.sex}}</span>
        </div>
        <!-- <span class="info-title">生日:</span>
         <span class="info">{{form.sex}}</span> -->
        <div class="mb8">
         <span class="info-title">八字:</span>
         <span class="info">{{form.birth_year}} {{form.birth_month}} {{form.birth_day}} {{form.birth_hour}}</span>
        </div>
        <div class="mb8">
        <span class="info-title">五行主宰:</span>
         <span class="info">{{form.five_elements}}</span>
         </div>
         <div class="mb8">
        <span class="info-title">职业:</span>
         <span class="info">{{form.career}}</span>
         </div>
         <div class="mb8">
        <span class="info-title">个性签名:</span>
         <span class="info">{{form.sign}}</span>
         </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">性格优势</div>
        <div>
           <span class="info">{{form.user_adv}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">性格缺陷</div>
        <div>
          <span class="info">{{form.user_dis}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">流年运势</div>
        <div>
        <el-tabs v-model="activeName" type="card">
         <el-tab-pane v-for="(item,index) in form.lucky" :key="index" :label="item.year" :name="`tab${index}`">
            <p class="info">{{item.emotion}}</p>
            <p class="info">{{item.leader}}</p>
         </el-tab-pane>
      </el-tabs>
        </div>
   </el-card>
    <!-- <el-card class="box-card" shadow="hover">
        <div class="card-item-head">注意</div>
        <div>
          <span class="info">{{form.attention}}</span>
        </div>
   </el-card> -->
    <el-dialog
      title="修改"
      :visible.sync="editVisual"
      width="70%"
      >
      
    <el-form :model="editForm" ref="editForm" label-width="60px">
      <el-form-item label="生日" >
          <el-date-picker
            type="date"
            value-format="yyyy-MM-dd"
            placeholder="请选择阳历生日"
            v-model="editForm.date"
            style="width: 100%;"
          ></el-date-picker>
      </el-form-item>
      <el-form-item label="时辰" >
          <el-time-picker
            placeholder="选择出生时间"
            value-format="HH:mm:ss"
            v-model="editForm.time"
            style="width: 100%;"
          ></el-time-picker>
      </el-form-item>
      <el-form-item
        label="昵称"
        prop="nick_name"
        :rules="[
          { required: true, message: '昵称不能为空'},
        ]"
      >
        <el-input v-model="editForm.nick_name"></el-input>
      </el-form-item>
      <el-form-item
        label="职业"
        prop="career"
        :rules="[
          { required: true, message: '职业不能为空'},
        ]"
      >
        <el-input v-model="editForm.career"></el-input>
      </el-form-item>
      <el-form-item
        label="签名"
        prop="sign"
        :rules="[
          { required: true, message: '个性签名不能为空'},
        ]"
      >            
        <el-input type="textarea" v-model="editForm.sign"></el-input>
      </el-form-item>
      
      <el-form-item>
      </el-form-item>  
          
    </el-form>
    
      <div style="text-align:center">
        <el-button type="plain" size="small" @click="resetForm">取消</el-button>
        <el-button type="primary" size="small" @click="submitForm">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import echartBar from '@/components/echartsBar'
import { postAction, getAction } from '@/api/manage'
export default {
  components: {
    echartBar
  },
  data () {
    return {
      activeName: 0,
      form: {
        name: ''
      },
      editForm: {
        career: '',
        sign: '',
        nick_name: '',
        date:'',
        time:''
      },
      editVisual: false
      // option:{
      //     tooltip: {
      //         trigger: 'item',
      //         formatter: '{a} <br/>{b}: {c} ({d}%)'
      //     },
      //     legend: {
      //         orient: 'vertical',
      //         left: 10,
      //         data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
      //     },
      //     series: [
      //         {
      //             name: '访问来源',
      //             type: 'pie',
      //             radius: ['50%', '70%'],
      //             avoidLabelOverlap: false,
      //             label: {
      //                 show: false,
      //                 position: 'center'
      //             },
      //             emphasis: {
      //                 label: {
      //                     show: true,
      //                     fontSize: '30',
      //                     fontWeight: 'bold'
      //                 }
      //             },
      //             labelLine: {
      //                 show: false
      //             },
      //             data: [
      //                 {value: 335, name: '直接访问'},
      //                 {value: 310, name: '邮件营销'},
      //                 {value: 234, name: '联盟广告'},
      //                 {value: 135, name: '视频广告'},
      //                 {value: 1548, name: '搜索引擎'}
      //             ]
      //         }
      //     ]
      // }
    }
  },
  computed: {
    ...mapState([
      'login_name'
    ])
  },
  mounted () {
    console.log('login_name', this.login_name)
    this.host()
  },
  methods: {
    openEditVisual () {
      this.editVisual = true
      this.editForm.nick_name = this.form.nick
      this.editForm.career = this.form.career
      this.editForm.sign = this.form.sign
    },
    submitForm () {
      this.$refs.editForm.validate((valid) => {
        if (valid) {
          const url = '/user/info'
          const date = this.editForm.date
          const time = this.editForm.time
          this.editForm.year = date.split('-')[0]
          this.editForm.month = date.split('-')[1]
          this.editForm.day = date.split('-')[2]
          this.editForm.hour = time.split(':')[0]
          this.editForm.minute = time.split(':')[1]
          postAction(url, this.editForm).then(res => {
            if (res.data.code == 200) {
              this.editVisual = false
              this.host()
              this.$message.warning(res.data.msg)
            } else {
              this.$message.warning(res.data.msg)
            }
          })
        } 
      })
    },
    resetForm () {
      this.$refs.editForm.resetFields()
      this.editVisual = false
    },
    host () {
      const url = '/profile/host'
      getAction(url).then(res => {
        console.log(res.data)
        this.form = res.data.msg
      }).catch(err => {
         this.$router.push({ name: 'Login' })
      })
    },
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      const myChart = this.$echarts.init(document.getElementById('myChart1'))
      // 绘制图表
      myChart.setOption({
        title: { text: '流年趋势' },
        tooltip: {},
        xAxis: {
          data: ['2011', '2015', '2016']
        },
        yAxis: {},
        series: [{
          name: '销量',
          type: 'bar',
          data: [5, 20, 36]
        }]
      })
    }
  }
}
</script>
<style scoped>
.form-line{
  margin-bottom: 10px;
}
.info-title{
  font-size: 14px;
  font-weight: 500;
  margin:0px 6px 0px 0px;
  color: #000;
  font-family: DFKai-SB;
}
.info{
  font-size: 14px;
  font-weight: 500;
  margin:0px 6px 10px 0px;
  color: rgba(0,0,0,0.7);
  font-family: DFKai-SB;
  line-height: 24px;
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
