<template>
<div>
   <div class="header">
     <el-autocomplete
          v-model="state"
          :fetch-suggestions="querySearchAsync"
          placeholder="请输入用户名"
          @select="handleSelect"
          clearable
          style="margin-right:8px; width:72%"
        > <i slot="prefix" class="el-input__icon el-icon-search"></i>
     </el-autocomplete>
    <!-- <el-button icon="el-icon-search"  @click="inputSearch()" circle style="color:#FF6B3B "></el-button> -->
    <el-button icon="el-icon-question"  @click="messageVisial = true" circle style="color:#FF6B3B "></el-button>
    <el-button  icon="el-icon-message" @click="gotoMessage" circle style="color:#FF6B3B "></el-button>
    <el-dropdown trigger="click" @command="handleClick">
    <el-button icon="el-icon-more" style="margin-left:8px;color:#FF6B3B"  circle></el-button>
      <el-dropdown-menu slot="dropdown" >
        <!-- <el-dropdown-item  command="1" icon="el-icon-question">帮助</el-dropdown-item> -->
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
      <span>在搜索框中输入查询人的昵称，然后选择对应的出生时间，即可获取合婚/合作匹配指数和建议。注：只能查询已经注册的人哦~</span>
      <div class="tr mt20">
        <el-button type="primary" size="small" @click="messageVisial = false">确 定</el-button>
      </div>
    </el-dialog>
    <router-view />
</div>

</template>

<script>
import { postAction, getAction } from '@/api/manage'
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
      messageVisial: false
    }
  },
  methods: {
    loginOut () {
      const url = '/logout'
      getAction(url).then(res => {
        if (res.data.code == 200) {
          this.$message.success(res.data.msg)
          this.$router.push({ name: 'Home' })
        } else {
          this.$message.warning('退出失败')
        }
      })
    },
    handleClick (command) {
      this.loginOut()
    },
    gotoMessage () {
      this.$router.push({ name: 'MessageList' })
    },
    handleSelect (item) {
      console.log(item)
      const select = item.value.split('-')
      this.state = select[0]
      this.login = item.loginName
      this.$router.push({ name: 'MatchResult', params: { loginName: this.login } })
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
</style>
