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
          <el-button type="primary" :loading="loading" size="small" style="margin-left：20px" @click="send()">发送</el-button>
        </div>
      </el-card>
  </div>
</template>
<script>
import { postAction, getAction } from '@/api/manage'
import { mapState } from 'vuex'
export default {
  data () {
    return {
      page: 1,
      massageList: [

      ],
      msglist: [
      ],
      listLoading: false,
      dialogVisible: false,
      form: {},
      sendText: '',
      loading: false
    }
  },
  computed: {
    loginName () {
      return this.$route.params.loginName
    },
    nickName () {
      return this.$route.params.nickName
    },
    ...mapState([
      'login_name'
    ])
  },
  mounted () {
    this.message()
  },
  methods: {
    message () {
      const url = '/message/content'
      postAction(url, { name: this.loginName }).then(res => {
        this.massageList = []
        this.msglist = res.data.msg.list
        this.msglist.forEach(item => {
          if (item.send === this.login_name) {
            this.massageList.push({ name: res.data.msg.sex.host_name, time: item.time, status: 'send', message: item.content })
          } else if (item.accept === this.login_name) {
            this.massageList.push({ name: this.nickName, time: item.time, status: 'receive', message: item.content })
          }
        })
        console.log('this.msglist', this.massageList)
      })
    },
    send () {
      const url = '/message/send'
      this.loading = true
      setTimeout(() => {
        this.sendText = ''
        postAction(url, { login_name: this.loginName, content: this.sendText }).then(res => {
          this.message()
          this.loading = false
        }).catch(err => {
          console.log('err', err)
          this.loading = false
        })
      }, 300)
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
