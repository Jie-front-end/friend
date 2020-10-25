<template>
 <div class="container">
    <div style="text-align:right">
      <!-- <el-button  type="warning" plain @click="toMatch">私信</el-button> -->
    </div>
    <el-form class="mt20" ref="coResult" :model="coResult" label-width="200px" label-position="top" label-suffix=":">
      <el-form-item label="本人主性格">
        <span>{{coResult.charactor.female_char}}</span>
      </el-form-item>
      <el-form-item label="本人缺少性格">
        <span>{{coResult.charactor.female_char}}</span>
      </el-form-item>
      <el-form-item label="本人应注意">
        <span>{{coResult.charactor.female_char}}</span>
      </el-form-item>
      <el-form-item label="匹配者主性格">
        <span>{{coResult.charactor.male_char}}</span>
      </el-form-item>
      <el-form-item label="匹配者缺少性格">
        <span>{{coResult.charactor.male_nonchar}}</span>
      </el-form-item>
      <el-form-item label="匹配者应注意">
        <span>{{coResult.charactor.male_attention}}</span>
      </el-form-item>
      <el-form-item label="匹配程度">
        <span>{{coResult.harmony.harmony_words}}</span>
      </el-form-item>
      <el-form-item label="事业">
        <p>本人：{{coResult.cooperation.female_char}}</p>
        <p>匹配者：{{coResult.cooperation.male_char}}</p>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { postAction,getAction } from '@/api/manage'
  export default {
    props:{
     coResult:{
         type: Object,
         default:()=>{},
     }
    },
    data() {
      return {

      };
    },
    computed:{

    },
    mounted(){
    },
    methods: {
    }
  }
</script>
<style scoped>
.container {
   width: 80%;
   text-align: justify;
   border: 2px solid gray;
   padding:30px;
   /* padding-left: 16px;
   padding-right: 16px; */
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
</style>
