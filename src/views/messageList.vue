<template>
   <div>
    <div style="display:flex;justify-content:space-between">
      <div class="ml10 mb8">
        {{this.nameList.length}}位联系人
      </div>
      <!-- <el-button style="margin-bottom:5px" size="small">全部已读</el-button> -->
    </div>
    <el-card class="card">
      <div>
           <div v-for="(item, index) in nameList" :key="index" style="margin-left:12px" @click="detail(item.login_name,item.nickname)">
              <div class="readState">
                  <div>
                    <i v-if="item.sex === '女'" class="iconfont icon-nvsheng iconSize ml10" />
                    <i v-else class="iconfont icon-nansheng iconSize ml10" />
                    <span class="ml10">{{item.nickname}}</span>
                  </div>
                  <div v-if="readFlag.length" class="redRound"></div>
                  <!-- <span class="right-corner">1</span> -->
              </div>
              <el-divider></el-divider>
           </div> 
            <!-- <el-button plain style="width:100%;margin-bottom:10px">
              {{item.name}}
            <el-tag :type="item.num > 0 ? 'warning' : 'success'">{{item.num}}</el-tag>
            </el-button> -->
      </div>
      <!-- <div v-else>
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
      </div> -->
    </el-card>
  </div>
</template>
<script>
import { postAction, getAction } from '@/api/manage'

export default {
  data () {
    return {
      page: 1,
      name: '',
      massageList: [
        { name: '李大力', num: 1, time: '' },
        { name: '苏大强', num: 0, time: '' }
      ],
      list: [
        { name: '1' }
      ],
      nameList: [],
      listLoading: false,
      dialogVisible: false,
      form: {},
      readFlag:[],
    }
  },
  mounted () {
    this.box()
  },
  methods: {
    toMatch () {

    },
    detail (loginName, nickName) {
      this.$router.push({ name: 'MessageDetail', query: { loginName: loginName, nickName: nickName } })
    },
    hasRead () {},
    box () {
      const url = '/message/box'
      getAction(url).then(res => {
        this.nameList = res.data.msg.name
        this.readFlag = res.data.msg.code
      })
    }
  }
}
</script>
<style scoped>
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
  .iconSize{
    font-size: 40px;
  }
  .readState{
    position: relative; 
  }
  .redRound{
    width: 10px;
    height: 10px;
    background: red;
    border-radius: 5px;
    position: absolute;
    top:4px;
    left: 12px;
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
</style>
