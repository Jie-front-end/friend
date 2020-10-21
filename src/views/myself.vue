<template>
 <div class="container">
    <div style="text-align:right">
      <!-- <el-button  type="warning" plain @click="toMatch">私信</el-button> -->
    </div>
    <el-form class="mt20" ref="form" :model="form" label-width="200px" label-position="top" label-suffix=":">
      <el-form-item label="用户名" prop="login_name">
        <span>111</span>
      </el-form-item>
      <el-form-item label="主性格" prop="pass">
        <span>111</span>
      </el-form-item>
      <el-form-item label="反性格" prop="name">
        <span>111</span>
      </el-form-item>
      <el-form-item label="前三年流年" prop="pass">
         <div id="myChart1" :style="{width: '300px', height: '300px'}"></div>
      </el-form-item>
      <el-form-item label="后三年流年" prop="name">
         <div id="myChart2" :style="{width: '300px', height: '300px'}"></div>
      </el-form-item>
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
            this.form = res.data
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
