<template>
  <div class="wrapper">
    <!-- <el-button type="text" @click="helpVisual">使用说明</el-button> -->
    <div style="width:100%;text-align:right;margin:0px"><el-button type="text" @click="helpVisual">使用说明</el-button></div>
    <el-card class="box-card" v-for="(tableItem,index) in tableData" :key="index" shadow="always">
        <div class="card-item-head">{{tableItem.title}}</div>
        <div>
      <el-carousel height="300px" :autoplay='false'>
        <el-carousel-item v-for="(item,index) in tableItem.data" :key="`card${index}`">
          <div class="allInfo">
            <div class="userName">
                <i v-if="item.sex === '男'" class="iconfont icon-nansheng iconSize" />
                <i v-else class="iconfont icon-nvsheng iconSize" />
                <span class="userName-title"> {{item.nickname}}</span>
                <el-button class="ml10" round size="small" style="color:#FF6B3B"
                   v-clipboard:copy="item.nickname"
                   v-clipboard:success="onCopy"
                   v-clipboard:error="onError"><i class="iconfont icon-aixin"/></el-button>
                <!-- <el-button round size="small" style="color:#FF6B3B" @click="gotoMatch(item.login_name)"><i class="iconfont icon-aixin"/></el-button> -->
                <el-button round size="small" style="color:#FF6B3B" @click="gotoMessage(item.login_name,item.nickname )"><i class="iconfont icon-sixin"/></el-button>
            </div>
            <div class="userInfo">
              <!-- <div class="mb8">
                <span class="info-title">昵称:</span>
                <span class="info">{{item.nickname}}</span>
              </div> -->
              <div class="mb8">
                <span class="info-title">性别:</span>
                <span class="info">{{item.sex}}</span>
              </div>
              <div class="mb8">
                <span class="info-title">城市:</span>
                <span class="info">{{item.city}}</span>
              </div>
              <div class="mb8">
                <span class="info-title">生日:</span>
                <span class="info">{{item.date}}</span>
              </div>
              <div class="mb8">
                <span class="info-title">八字:</span>
                <span class="info">{{item.birth_year}} {{item.birth_month}} {{item.birth_day}} {{item.birth_hour}}</span>
              </div>
              <div class="mb8">
                <span class="info-title">五行主宰:</span>
                <span class="info">{{item.sex}}</span>
              </div>
              <div class="mb8">
                <span class="info-title">职业:</span>
                <span class="info">{{item.career}}</span>
              </div>
              <div class="mb8">
                <span class="info-title">个性签名:</span>
                <span class="info">{{item.birth_year}}</span>
              </div>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
        </div>
   </el-card>
       <el-dialog
      title="帮助"
      :visible.sync="messageVisial"
      width="70%"
      >
      <span>点击推荐结果卡片，可出现指示箭头,</span>
      <p>箭头左右两边箭头即可查看所有与你匹配的人。</p>
      <div class="tr mt20">
        <el-button type="primary" size="small" @click="messageVisial = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
import { postAction, getAction } from '@/api/manage'
export default {
  data () {
    return {
      list: [
        { nickname: 'a' }
      ],
      tableList: [
        { title: '谁和你最匹配？' },
        { title: '性格要合哦~' },
        { title: '性格也要互补哦~' },
        { title: '五行也很重要呢' }
      ],
      listLoading: false,
      dialogVisible: false,
      messageVisial: false,
      tableData: {},
      first: [],
      second: [],
      third: [],
      forth: [],
      tabPosition: '',
      sex: 1,
      form: {}
    }
  },
  mounted () {
    this.fetchData()
  },
  methods: {
    helpVisual () {
      this.messageVisial = true
    },
    gotoMatch (name) {
      this.$router.push({ name: 'MatchResult', query: { loginName: name } })
    },
    gotoMessage (loginName, nickName) {
      this.$router.push({ name: 'MessageDetail', query: { loginName: loginName, nickName: nickName } })
    },
    fetchData () {
      const url = '/profile/recommend'
      getAction(url).then(res => {
        this.tableData = []
        if (res.data.msg.first && res.data.msg.first.length) { this.tableData.push({ title: '谁和你最匹配？', data: [...res.data.msg.first] }) }
        if (res.data.msg.second && res.data.msg.second.length) { this.tableData.push({ title: '性格要合哦~', data: [...res.data.msg.second] }) }
        if (res.data.msg.third && res.data.msg.third.length) { this.tableData.push({ title: '性格也要互补哦~', data: [...res.data.msg.third] }) }
        if (res.data.msg.forth && res.data.msg.forth.length) { this.tableData.push({ title: '五行也很重要呢', data: [...res.data.msg.forth] }) }
        console.log('tableData', this.tableData)
      })
    },
    getUserDetail (id) {
      this.dialogVisible = true
      // const url = 'admin/userdetail/' + id
      const url = '/profile/detail/' + id
      getAction(url).then(res => {
        this.form = res.data.msg
      })
    },
    // 复制成功
    onCopy (e) {
      this.$message({
        showClose: true,
        message: '复制成功',
        type: 'success'
      })
      this.$store.commit('SET_Nick_NAME', e.text)
    },
    // 复制失败
    onError (e) {
      this.$message.success('复制失败')
    }
  }
}
</script>
<style >
.el-carousel__item {
  font-size: 14px;
  opacity: 0.75;
  margin: 0;
  /* background:#FFE0C7 */
  background:#fff
}
.allInfo{
  display: flex;
  flex-direction: column;
  padding: 10px 20px;
}
.userName{
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.userName-title{
  font-size: 18px;
  font-weight: 600;
  margin-right: 10px;
}
.userInfo{
  padding: 0px 20px;
}
.info-title{
  font-size: 14px;
  font-weight: 600;
  margin:0px 10px 10px 0px;
  font-family: DFKai-SB;
}
.info{
  font-size: 14px;
  font-weight: 500;
  margin:0px 0px 10px 0px;
  font-family: DFKai-SB;
}
.content {
  color: rgba(0, 0, 0, 0.65);
  font-size: 14px;
  padding-bottom: 32px;
  width: 70%;
  font-weight: 500;
 }
.contentTitle {
  color: rgba(0, 0, 0, 0.75);
  font-size: 14px;
  align-items: center;
  line-height: 20px;
  margin-right: 8px;
  font-weight: 600;
  padding-bottom: 32px;
  white-space: nowrap;
 }
.contentTitle::after {
    content: ':';
    margin: 0 8px 0 2px;
    position: relative;
    top: -0.5px;
  }
  .iconSize{
    font-size: 32px;
  }
</style>
