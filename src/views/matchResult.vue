<template>
 <div class="wrapper">
    <!-- <div style="text-align:right">
      <el-button plain @click="toMatch">修改</el-button>
    </div> -->
  <el-card class="box-card" shadow="false" >
    <div slot="header" class="head-box">
        <span class="card-head">匹配结果</span>
         <el-button style="float: left; padding: 3px 4px;margin-right:10px;color:#FF6B3B" @click="$router.push({name: 'Home'})" icon="el-icon-caret-left" circle></el-button>
    </div>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">匹配程度</div>
        <div>
           <span>{{form.user_adv}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">本人主性格</div>
        <div>
           <span>{{form.user_adv}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">匹配者主性格</div>
        <div>
           <span>{{form.user_adv}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">本人缺少性格</div>
        <div>
           <span>{{form.user_adv}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">匹配者缺少性格</div>
        <div>
           <span>{{form.user_adv}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">本人应注意</div>
        <div>
           <span>{{form.user_adv}}</span>
        </div>
   </el-card>
    <el-card class="box-card" shadow="always">
        <div class="card-item-head">匹配者应注意</div>
        <div>
           <span>{{form.user_adv}}</span>
        </div>
   </el-card>
    <!-- <el-form class="mt20" ref="coResult" :model="coResult" label-width="200px" label-position="top" label-suffix=":">
      <el-form-item label="事业">
        <p>本人：{{coResult.cooperation.female_char}}</p>
        <p>匹配者：{{coResult.cooperation.male_char}}</p>
      </el-form-item>
    </el-form> -->
  </el-card>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { postAction, getAction } from '@/api/manage'
export default {
  props: {
    coResult: {
      type: Object,
      default: () => {}
    }
  },
  data () {
    return {
      form: {}
    }
  },
  computed: {

  },
  mounted () {
  },
  methods: {
  }
}
</script>
<style scoped>
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
</style>
