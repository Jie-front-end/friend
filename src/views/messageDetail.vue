<template>
  <div style="padding:30px">
  <div style="display:flex;justify-content:space-between">
      <div>60条</div>
      <div style="text-align:right">
        <el-button style="margin-bottom:5px" size="small" @click="goBack">返回</el-button>
      </div>
  </div>
  <el-card class="card">
    <div class="lr">
        <div v-for="(item, index) in twoMassageList" :key="index" >
            <el-button plain style="width:100%;margin-bottom:10px;text-align:left">
              {{item.name}} :
              {{item.message}}
            </el-button>
        </div>
    </div>
    <div style="display:flex; margin-top:20px">
      <el-input v-model="name" style="width:200px;margin-right:10px;flex:1" placeholder="请输入内容"></el-input>
      <el-button type="primary" size="small" style="margin-left：20px" @click="goBack()">发送</el-button>
    </div>
  </el-card>
  </div>
</template>
<script>
import { postAction } from '@/api/manage'

export default {
  data() {
    return {
      page: 1,
      name:'',
      massageList:[
        {name:'李大力', num: 1},
        {name:'苏大强', num: 0}
      ],
      twoMassageList:[
        {name:'李大力', message: '你好', status: 'send'},
        {name:'苏大强', message: '你好', status: 'receive'}
      ],
      list: [
        {name:'1'}
      ],
      listLoading: false,
      dialogVisible:false,
      form:{}
    }
  },
  // created() {
  //   this.fetchData()
  // },
  methods:{
    toMatch(){

    },
    detail(){
      this.$message.warning('按键111')
    },
    dialogVisual(){

    },
    goBack(){
      this.$emit('numChange','out')
    },
    message(){
      const url = `/message/content/adminzxz`
      getAction(url).then( res => {
          console.log('res.data',res.data)
      })
    },
    send(){
      const url = `/message/send`
      postAction(url,{login_name:'adminzxz', content:'你好'}).then( res => {
          console.log('res.data',res.data)
      })
    },
  }
}
</script>
<style scoped>
.lr{
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;

}
  .fr{
     align-self:flex-end
  }
  .fl{
     align-self:flex-start
  }
  .body-item{
    display:flex;
    justify-content:space-between
  }
  .small-font{
    font-size: 12px;
    color: #686868;
    margin-right:20px;
  }
  .right-corner{
    display: inline-block;
    width: 16px;
    height: 16px;
    font-size: 8px;
    position:absolute;
    left:-18px;
    top:-8px;
    text-align: center;
    background-color: #FDEDBE;
    border:2px solid #D2EDC8;
    border-radius:10px
  }
  .name-position{
    position: relative;
  }
</style>


