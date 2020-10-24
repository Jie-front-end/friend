<template>
 <div class="container">
  <el-card >
  <div slot="header">
    <strong>主页</strong>
    <div style="float:right">
     <!-- <el-input v-model="name" size="small" style="width:200px;margin-right:10px" placeholder="请输入内容"></el-input> -->
     <el-autocomplete
          v-model="state"
          :fetch-suggestions="querySearchAsync"
          placeholder="请输入内容"
          @select="handleSelect"
          style="margin-right:20px"
          size="small"
        ></el-autocomplete>
     <el-button type="primary" size="small" style="margin-left：20px" @click="search()">查询</el-button>
    </div>
  </div>
  <div>
      <el-tabs v-model="activeName">
        <el-tab-pane label="个人信息" name="first">
          <myself @change="getActiveName" />
        </el-tab-pane>
        <el-tab-pane label="推荐" name="second">
          <match @change="getActiveName" />
        </el-tab-pane>
        <el-tab-pane label="私信" name="third">
          <message @numChange="getflag" v-if="flag === 'out'"/>
          <message-detail @numChange="getflag" v-if="flag === 'in'"/>
        </el-tab-pane>
     </el-tabs>
  </div>
  </el-card>
 </div>
</template>

<script>
import echartBar from "@/components/echartsBar";
import myself from "./myself";
import message from "./message";
import match from "./match";
import messageDetail from "./messageDetail";
import { postAction } from '@/api/manage'
  export default {
  components:{
    echartBar,
    myself,
    message,
    match,
    messageDetail
  },
    data() {
      return {
        name:'',
        state:'',
        flag:'out',
        activeName:'first',
        queryResult:{},
        filtList:[],
        queryInput:'',
        form:{
          name:'',
        },
        option:{
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b}: {c} ({d}%)'
            },
            legend: {
                orient: 'vertical',
                left: 10,
                data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
            },
            series: [
                {
                    name: '访问来源',
                    type: 'pie',
                    radius: ['50%', '70%'],
                    avoidLabelOverlap: false,
                    label: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        label: {
                            show: true,
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    },
                    labelLine: {
                        show: false
                    },
                    data: [
                        {value: 335, name: '直接访问'},
                        {value: 310, name: '邮件营销'},
                        {value: 234, name: '联盟广告'},
                        {value: 135, name: '视频广告'},
                        {value: 1548, name: '搜索引擎'}
                    ]
                }
            ]
        }
      };
    },
    methods: {
      getflag(param){
        this.flag = param
      },
      search(){
        const url = '/profile/search'
        postAction( url, { search: this.state }).then( res => {
          this.queryResult = res.data.msg.list
        this.filtList = this.queryResult.map( item => {  return { value : `${this.queryInput}-${item.birth}-${item.city}-${item.sex }`, loginName: item.login_name } })
        console.log('filtList', this.filtList)
        })
        console.log('this.queryResult',this.queryResult)
      },
      getActiveName(param){
        this.activeName = param
      },
      querySearchAsync(queryString, cb){
        const value = [] 
        this.queryInput = queryString
        console.log('queryString','cb',queryString, cb(this.filtList))
        this.search()
      },
      he(){
        const url = `/profile/co/adminzxz`
        getAction(url).then( res => {
            console.log('res.data',res.data)
        })
      },
      handleSelect(item){
         console.log(item);
         const select = item.value.split('-')
         const loginName = item.loginName
         console.log('select', select)
         console.log('loginName', loginName)
         this.state = select[0]
      }
    }
  }
</script>
<style scoped>
.container {
   text-align: justify;
   width: 90%;
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
