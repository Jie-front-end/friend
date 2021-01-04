<template>
  <div>
     <el-button type="text" style="color: rgba(0, 0, 0, 0.65);" @click="$router.push({name: 'MessageList'})"><i class="el-icon-arrow-left" /></el-button>
      <div class="twoPeople">
        <div>
            <i v-if="chatPepole.name_sex === '女'" class="iconfont icon-nvsheng iconSize" />
            <i v-else class="iconfont icon-nansheng iconSize" />
            <span class="ml5">{{chatPepole.name}}</span>
        </div>
        <div>
            <i v-if="chatPepole.host_sex === '女'" class="iconfont icon-nvsheng iconSize" />
            <i v-else class="iconfont icon-nvsheng iconSize" />
            <span class="ml5">{{chatPepole.host_name}}</span>
        </div>
      </div>
      <el-card class="card">
        <div v-for="(item, index) in massageList" :class="[item.status === 'receive'?'box-left':'box-right']" :key="index" >
           <div :class="[item.status === 'receive'?'big-box-shou':'big-box-fa']">
              <div class="timeFont">{{item.time}}</div>
              <div class="box-bord">
                <span>{{item.message}}</span>
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
      chatPepole: {
        host_name: '',
        host_sex: '',
        name: '',
        name_sex: ''
      },
      listLoading: false,
      dialogVisible: false,
      form: {},
      sendText: '',
      loading: false
    }
  },
  computed: {
    loginName () {
      return this.$route.query.loginName
    },
    nickName () {
      return this.$route.query.nickName
    },
    ...mapState([
      'login_name'
    ])
  },
  created () {
    this.message()
  },
  activated () {
    this.message()
  },
  methods: {
    message () {
      const url = '/message/content'
      postAction(url, { name: this.loginName }).then(res => {
        this.massageList = []
        this.msglist = res.data.msg.list
        this.chatPepole = res.data.msg.sex
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
        postAction(url, { login_name: this.loginName, content: this.sendText }).then(res => {
          this.sendText = ''
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
  .twoPeople{
    display: flex;
    justify-content: space-between;
  }
  .box-right{
    display: flex;
    justify-content: flex-end;
  }
  .timeFont{
    margin-left: 8px;
    font-size: 12px;
  }
  .big-box-fa span{
    background-color: #CDF3E4;
    padding: 5px 8px;
    height: 20px;
    display: inline-block;
    border-radius: 4px;
    margin:10px 0 10px 10px;
    position: relative;

  }
  .big-box-fa span::after{
    content: '';
    border: 8px solid #FFF;
    border-left: 8px solid #CDF3E4;
    position: absolute;
    top: 6px;
    right: -16px;
  }
  .big-box-shou span{
    background-color: #F08BB4;
    padding: 5px 8px;
    height: 20px;
    display: inline-block;
    border-radius: 4px;
    margin:10px 0 10px 10px;
    position: relative;

  }
  .big-box-shou span::after{
    content: '';
    border: 8px solid #FFF;
    border-right: 8px solid #F08BB4;
    position: absolute;
    top: 6px;
    left: -16px;
  }
  .iconSize{
    font-size: 32px;
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
