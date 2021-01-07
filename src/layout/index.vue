<template>
<div>
   <div class="header">
     <el-autocomplete
          v-model="state"
          :fetch-suggestions="querySearchAsync"
          placeholder="请输入查询人的全部昵称"
          @select="handleSelect"
          clearable
          style="margin-right:8px; width:72%"
        > <i slot="prefix" class="el-input__icon el-icon-search"></i>
     </el-autocomplete>
    <!-- <el-button icon="el-icon-search"  @click="inputSearch()" circle style="color:#FF6B3B "></el-button> -->
    <el-button icon="el-icon-question"  @click="messageVisial = true" circle style="color:#FF6B3B "></el-button>
    <div class="redRoundFa">
      <el-button icon="el-icon-message" @click="gotoMessage" circle style="color:#FF6B3B "></el-button>
      <div v-if="code_new === '1'" class="redRound"></div>
    </div>
    <!-- <el-button  @click="gotoLink" circle style="color:#FF6B3B "><i style="font-size:20px" class="iconfont icon-maomi"/></el-button> -->
    <el-dropdown trigger="click" @command="handleClick">
    <el-button icon="el-icon-more" style="margin-left:8px;color:#FF6B3B"  circle></el-button>
      <el-dropdown-menu slot="dropdown" >
        <!-- <el-dropdown-item  command="1" icon="el-icon-question">帮助</el-dropdown-item> -->
        <el-dropdown-item command="1"><i style="font-size:16px" class="iconfont icon-maomi"/>关注</el-dropdown-item>
        <el-dropdown-item command="2" icon="el-icon-switch-button">退出</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
    <el-dialog
      title="帮助"
      :visible.sync="messageVisial"
      width="80%"
      >
      <div class="mb10">我俩合不合？</div>
      <span>在搜索框中输入查询人的全部昵称，然后选择对应的出生时间，即可获取合婚/合作匹配指数和建议。注：只能查询已经注册的人哦~</span>
      <div class="tr mt20">
        <el-button type="primary" size="small" @click="messageVisial = false">确 定</el-button>
      </div>
    </el-dialog>
    <el-dialog
      title="关注我们"
      :visible.sync="imgVisial"
      width="80%"
      >
     <img :src="imgUrl" style="width:80%;height:80%">
    </el-dialog>
    <router-view />
</div>

</template>

<script>
import { postAction, getAction } from '@/api/manage'
import { mapState } from 'vuex'
export default {
  components: {
  },
  data () {
    return {
      name: '',
      state: '',
      queryResult: {},
      filtList: [],
      queryInput: '',
      messageVisial: false,
      imgVisial:false,
      code_new:'',
      imgUrl: require("../assets/miao.jpg")
    }
  },
  computed: {
    ...mapState([
      'nickname'
    ])
  },
  mounted(){
    this.box()
  },
  watch: {
    nickname (newName, oldName) {
      this.state = newName
    }
  },
  methods: {
    loginOut () {
      const url = '/user/logout'
      getAction(url).then(res => {
        if (res.data.code == 200) {
          this.$message.success(res.data.msg)
          this.$router.push({ name: 'Login' })
        } else {
          this.$message.warning('退出失败')
        }
      })
    },
    handleClick (command) {
      if(command === '1'){
        this.imgVisial = true
      } else if(command === '2'){
        this.loginOut()
      }
    },
    gotoMessage () {
      this.$router.push({ name: 'MessageList' })
    },
    gotoLink(){
      window.open('https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzAxNTE1OTgyNA==&scene=124&uin=&key=&devicetype=Windows+10+x64&version=63010029&lang=zh_CN&a8scene=7&fontgear=2')
    },
    handleSelect (item) {
      console.log(item)
      const select = item.value.split('-')
      this.state = select[0]
      this.login = item.loginName
      this.$router.push({ name: 'MatchResult', query: { loginName: this.login } })
    },
    search (cb) {
      const url = '/profile/search'
      postAction(url, { search: this.state }).then(res => {
        this.queryResult = res.data.msg.list
        this.filtList = this.queryResult.map(item => { return { value: `${this.queryInput}-${item.birth}-${item.city}-${item.sex}`, loginName: item.login_name } })
        console.log('filtList', this.filtList)
        cb(this.filtList)
      })
      console.log('this.queryResult', this.queryResult)
    },
    querySearchAsync (queryString, cb) {
      const value = []
      this.queryInput = queryString
      console.log('queryString', queryString)
      this.search(cb)
    },
    box () {
      const url = '/message/box'
      getAction(url).then(res => {
        this.code_new = res.data.msg.code_new
      })
    }
    // inputSearch () {
    //   this.$router.push({ name: 'MatchResult', query: { matchName: this.login } })
    // }
  }
}
</script>
<style >
.header{
  display: flex;
  flex-wrap: nowrap;
  padding: 20px 10px;
  background: #FFAB57 ;
  border-radius: 12px;
}
.draw-line{
   width: 100%;
   height: 1px;
   border-top: solid  #FF9E7B 1px;
   margin-bottom: 10px;
}
.el-dropdown-link {
    cursor: pointer;
    color: #FF9E7B;
  }
  .redRoundFa{
    display: inline-block;
    position: relative;
    margin-left: 10px;
  }
  .redRound{
    width: 6px;
    height: 6px;
    background: red;
    border-radius: 3px;
    position: absolute;
    top:8px;
    right:8px;
  }
</style>
