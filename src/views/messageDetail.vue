<template>
  <div>
     <el-button type="text" style="color: rgba(0, 0, 0, 0.65);" @click="$router.push({name: 'MessageList'})"><i class="el-icon-arrow-left" /></el-button>
      <el-card class="card">
        <div v-for="(item, index) in massageList" :class="[item.status === 'receive'?'box-left':'box-right']" :key="index" >
           <div class="big-box">
              <div class="timeFont">{{item.time}}</div>
              <div class="box-bord">
                {{item.name}} :
                {{item.message}}
              </div>
           </div>
        </div>
        <div style="display:flex; margin-top:20px">
          <el-input v-model="sendText" style="width:200px;margin-right:10px;flex:1" placeholder="请输入内容"></el-input>
          <el-button type="primary" size="small" style="margin-left：20px" @click="send()">发送</el-button>
        </div>
      </el-card>
  </div>
</template>
<script>
import { postAction, getAction } from '@/api/manage'

export default {
  data () {
    return {
      page: 1,
      massageList: [
        { name: '李大力', num: 1, time: '2020-10-12 9:00', status: 'receive', message: '你好' },
        { name: '苏大强', num: 0, time: '2020-10-12 9:10', status: 'send', message: '很高兴认识你！你是哪里人？' }
      ],
      list: [
        { name: '1' }
      ],
      listLoading: false,
      dialogVisible: false,
      form: {},
      sendText: ''
    }
  },
  computed: {
    name () {
      return this.$route.params.name
    }
  },
  mounted () {
    this.message()
  },
  methods: {
    message () {
      const url = '/message/content'
      postAction(url, { name: this.name }).then(res => {
        console.log('res.data', res.data)
      })
    },
    send () {
      const url = '/message/send'
      postAction(url, { login_name: this.name, text: this.sendText }).then(res => {
        console.log('res.data', res.data)
      })
    }
  }
}
</script>
<style scoped>
  .box-left{
    display: flex;
    justify-content: flex-start;
  }
  .box-right{
    display: flex;
    justify-content: flex-end;
  }
  .timeFont{
    margin-left: 8px;
    font-size: 12px;
  }
  .big-box{
    width: 50%;
    margin-bottom: 10px;
  }
  .box-bord{
    border: 1px solid #CED4DE;
    display: flex;
    align-items: center;
    padding: 10px 10px;
    margin: 5px 0px;
    border-radius: 12px;
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
