<template>
 <div class="container">
  <div class="navigation">
    <!-- <el-radio-group v-model="tabPosition" fill="#FFAB57">
      <el-radio-button label="1">个人</el-radio-button>
      <el-radio-button label="2">推荐</el-radio-button>
    </el-radio-group> -->
    <el-tabs type="card" v-model="activeName" style="width:100%">
      <el-tab-pane name="1">
        <span slot="label"><i class="el-icon-user-solid"></i>个人</span>
        <myself />
      </el-tab-pane>
      <el-tab-pane name="2">
         <span slot="label"><i class="iconfont icon-icon_jiaoyou"/> 推荐</span>
        <match />
      </el-tab-pane>
    </el-tabs>
  </div>
  <!-- <myself v-if="tabPosition === '1'"  />
  <match v-else /> -->
 </div>
</template>

<script>
import myself from './myself'
import match from './match'
import { postAction, getAction } from '@/api/manage'
export default {
  components: {
    myself,
    match
  },
  data () {
    return {
      name: '',
      state: '',
      flag: 'out',
      tabPosition: '1',
      activeName: '2',
      queryResult: {},
      filtList: [],
      queryInput: '',
      form: {
        name: ''
      },
      msg: '这是被复制的内容',
      login: '',
      coResult: {}
    }
  },
  methods: {
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
    he () {
      const url = `/profile/co/${this.login}`
      getAction(url).then(res => {
        this.coResult = res.data.msg.result
      })
    },
    handleSelect (item) {
      console.log(item)
      const select = item.value.split('-')
      this.state = select[0]
      this.login = item.loginName
    }
  }
}
</script>
<style>
.container {
   text-align: justify;
   /* width: 90%; */
   margin-right: auto;
   margin-left: auto;
   /* border:2px solid#888888 ; */
   border-radius:4px;
   /* box-shadow: 2px 2px 2px #888888; */
   display: flex;
   flex-direction: column;
   justify-content: center;
   /* padding-left: 16px;
   padding-right: 16px; */
}
.navigation{
  display: flex;
  justify-content: center;
  margin: 6px ;
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
.iconbox{
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.iconStyle{
  font-size: 24px;
  margin: 0px 5px;
  color:#F6903D;
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
