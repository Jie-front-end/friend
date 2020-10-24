<template>
 <div class="container">
    <div style="text-align:right">
      <!-- <el-button  type="warning" plain @click="toMatch">私信</el-button> -->
    </div>
    <el-form class="mt20" ref="form" :model="form" label-width="200px" label-position="top" label-suffix=":">
      <el-form-item label="昵称">
        <span>{{form.nick}}</span>
      </el-form-item>
      <el-form-item label="八字">
        <span>{{form.birth_year}} {{form.birth_month}} {{form.birth_day}} {{form.birth_hour}}</span>
      </el-form-item>
      <el-form-item label="性别">
        <span>{{form.sex}}</span>
      </el-form-item>
      <el-form-item label="职业">
        <span>{{form.career}}</span>
      </el-form-item>
      <el-form-item label="五行主宰">
        <span>{{form.five_elements}}</span>
      </el-form-item>
      <el-form-item label="主性格">
        <span>{{form.user_adv}}</span>
      </el-form-item>
      <el-form-item label="反性格">
        <span>{{form.user_dis}}</span>
      </el-form-item>
      <el-form-item label="流年运势">
        <!-- <div v-for="(item,index) in form.lucky" :key="index"><p>{{item.emotion}}</p></div> -->
      <el-tabs v-model="activeName" type="card">
         <el-tab-pane v-for="(item,index) in form.lucky" :label="item.year" name="index">
            <p>感情：{{item.emotion}}</p>
            <p>领导关系：{{item.leader}}</p>    
         </el-tab-pane>
      </el-tabs>
      </el-form-item>
      <el-form-item label="注意">
        <span>{{form.attention}}</span>
      </el-form-item>
      <!-- <el-form-item label="后三年流年" prop="name">
         <div id="myChart2" :style="{width: '300px', height: '300px'}"></div>
      </el-form-item> -->
    </el-form>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import echartBar from "@/components/echartsBar";
import { postAction,getAction } from '@/api/manage'
  export default {
  components:{
    echartBar
  },
    data() {
      return {
        activeName:'',
        form:{
          name:'',
        },
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
      };
    },
    computed:{
      ...mapState([
        'login_name'
      ])
    },
    mounted(){
      console.log('login_name', this.login_name)
      this.drawLine();
    },
    methods: {
      host() {
        const url = '/profile/host'
        getAction(url).then( res => {
            console.log(res.data)
            this.form = res.data.msg
        })
      },
      toMatch(){
        this.$emit('change','third')
      },
      goBack(){
         this.$router.push({name: 'Home'})
      },
     drawLine(){
        // 基于准备好的dom，初始化echarts实例
        let myChart = this.$echarts.init(document.getElementById('myChart1'))
        // 绘制图表
        myChart.setOption({
            title: { text: '流年趋势' },
            tooltip: {},
            xAxis: {
                data: ["2011","2015","2016"]
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36]
            }]
        });
    }
    }
  }
</script>
<style scoped>
.container {
   width: 80%;
   text-align: justify;
   border: 2px solid gray;
   padding:30px;
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
