<template>
  <div class="wrapper">
    <el-card class="box-card" v-for="(tableItem,index) in tableData" :key="index" shadow="always">
        <div class="card-item-head">{{tableList[index].title}}</div>
        <div>
      <el-carousel height="300px" :autoplay='false'>
        <el-carousel-item v-for="item in tableItem" :key="item">
          <div class="allInfo">
            <div class="userName">
                <i class="iconfont icon-nansheng iconSize" />
                <span class="userName-title"> 李大力</span>
                <el-button round size="small" style="color:#FF6B3B" @click="gotoMatch(item.login_name)"><i class="iconfont icon-aixin"/></el-button>
                <el-button round size="small" style="color:#FF6B3B" @click="gotoMessage(item.login_name)"><i class="iconfont icon-sixin"/></el-button>
            </div>
            <div class="userInfo">
              <div>
                <span class="info-title">昵称:</span>
                <span class="info">{{item.nickname}}</span>
              </div>
              <div>
                <span class="info-title">性别:</span>
                <span class="info">{{item.sex}}</span>
              </div>
              <div>
                <span class="info-title">城市:</span>
                <span class="info">{{item.city}}</span>
              </div>
              <div>
                <span class="info-title">生日:</span>
                <span class="info">{{item.date}}</span>
              </div>
              <div>
                <span class="info-title">八字:</span>
                <span class="info">{{item.birth_year}} {{item.birth_month}} {{item.birth_day}} {{item.birth_hour}}</span>
              </div>
              <div>  
                <span class="info-title">五行主宰:</span>
                <span class="info">{{item.sex}}</span>
              </div>
              <div>
                <span class="info-title">职业:</span>
                <span class="info">{{item.career}}</span>
              </div>
              <div>
                <span class="info-title">个性签名:</span>
                <span class="info">{{item.birth_year}}</span>
              </div>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
        </div>
   </el-card>
  </div>
</template>
<script>
import Connect from '@/connect.js'
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
    gotoMatch (name) {
      // Connect.$emit('getName',{
      //       name:name
      // })
      this.$router.push({ name: 'MatchResult', params: { name: name } })
    },
    gotoMessage (name) {
      this.$router.push({ name: 'messageDetail', params: { name: name } })
    },
    fetchData () {
      const url = '/profile/recommend'
      getAction(url).then(res => {
        this.tableData = []
        this.first = res.data.msg.first
        this.tableData[0] = [...this.first]
        this.second = res.data.msg.second
        this.tableData[1] = [...this.second]
        this.third = res.data.msg.third
        this.tableData[2] = [...this.third]
        this.forth = res.data.msg.forth
        this.tableData[3] = [...this.forth]
      })
      console.log('tableData', this.tableData)
      console.log('first', this.first)
      console.log('second', this.second)
      console.log('third', this.third)
    },
    getUserDetail (id) {
      this.dialogVisible = true
      // const url = 'admin/userdetail/' + id
      const url = '/profile/detail/' + id
      getAction(url).then(res => {
        this.form = res.data.msg
      })
    }
  }
}
</script>
<style >
.el-carousel__item {
  font-size: 14px;
  font-size: 14px;
  font-size: 14px;
  opacity: 0.75;
  margin: 0;
  background:#FFE0C7
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
  font-weight: 500;
  margin:0px 0px 10px 0px;
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
