<template>
 <div class="wrapper">
    <!-- <div style="text-align:right">
      <el-button plain @click="toMatch">修改</el-button>
    </div> -->
  <el-card class="box-card" shadow="false" >
    <div slot="header" class="head-box">
        <span class="card-head">与{{other_nickname}}的匹配结果</span>
         <el-button style="float: left; padding: 3px 4px;margin-right:10px;color:#FF6B3B" @click="$router.push({name: 'Home'})" icon="el-icon-caret-left" circle></el-button>
    </div>
    <el-card class="box-card" shadow="always">
      <div class="twoEnd">
        <div class="card-item-head">匹配程度</div>
        <el-button round size="small" style="color:#FF6B3B" @click="gotoMessage(other_login_name,other_nickname )"><i class="iconfont icon-sixin"/></el-button>
      </div>
        <div>
           <p class="info-weight">匹配得分：{{coResult.harmony.harmony_score}}</p>
           <span class="info">{{coResult.harmony.harmony_words}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">本人性格特点</div>
        <div>
           <span class="info">{{coResult.charactor.female_char}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">匹配者性格特点</div>
        <div>
           <span class="info">{{coResult.charactor.male_char}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">本人性格缺陷部分</div>
        <div>
           <span class="info">{{coResult.charactor.female_nonchar}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">匹配者性格缺陷部分</div>
        <div>
           <span class="info">{{coResult.charactor.male_nonchar}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">本人接受的沟通方式</div>
        <div>
           <span class="info">{{coResult.charactor.female_attention}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">与匹配者沟通应注意</div>
        <div>
           <span class="info">{{coResult.charactor.male_attention}}</span>
        </div>
   </el-card>
    <!-- <el-form class="mt20" ref="coResult" :model="coResult" label-width="200px" label-position="top" label-suffix=":">
      <el-form-item label="事业">
        <p>本人：{{coResult.cooperation.female_char}}</p>
        <p>匹配者：{{coResult.cooperation.male_char}}</p>
    </el-form> -->
  </el-card>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { postAction, getAction } from '@/api/manage'
export default {
  data () {
    return {
      form: {},
      coResult: {
        harmony: {}
      },
      other_nickname:'',
      other_login_name:''
    }
  },
  computed: {
    loginName () {
      return this.$route.query.loginName
    }
  },
  created () {
    this.he()
  },
  methods: {
    he () {
      const url = '/profile/co'
      postAction(url, { name: this.loginName }).then(res => {
        this.coResult = res.data.msg.result
        this.other_nickname = res.data.msg.other_nickname
        this.other_login_name = res.data.msg.other_login_name
      })
    },
    gotoMessage (loginName, nickName) {
      this.$router.push({ name: 'MessageDetail', query: { loginName: loginName, nickName: nickName } })
    }
  }
}
</script>
<style scoped>
.info-weight{
  color: #000;
  font-family: DFKai-SB;
  font-weight: 600;
}
.info-title{
  font-size: 14px;
  font-weight: 500;
  margin:0px 6px 0px 0px;
  color: #000;
  font-family: DFKai-SB;
}
.info{
  font-size: 14px;
  font-weight: 500;
  margin:0px 6px 10px 0px;
  color: rgba(0,0,0,0.7);
  font-family: DFKai-SB;
  line-height: 24px;
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
.twoEnd{
  display: flex;
  justify-content: space-between;
}
</style>
