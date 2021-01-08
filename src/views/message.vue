<template>
   <div class="wrapper">
    <div class="content-head">
        <el-button style="float: left; padding: 3px 4px;margin-right:10px;color:#FF6B3B" @click="$router.push({name: 'Home'})" icon="el-icon-caret-left" circle></el-button>
        <span class="card-head">私信</span>
    </div>
    <el-card class="box-card" shadow="false" >
      <div class="content-body">
          <router-view />
      </div>
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
        { name: '李大力', num: 1 },
        { name: '苏大强', num: 0 }
      ],
      twoMassageList: [
        { name: '李大力', message: '你好', status: 'send' },
        { name: '苏大强', message: '你好', status: 'receive' }
      ],
      list: [
        { name: '1' }
      ],
      listLoading: false,
      dialogVisible: false,
      form: {}
    }
  },
  created () {
    this.box()
  },
  methods: {
    toMatch () {

    },
    detail () {
      this.$emit('numChange', 'in')
    },
    dialogVisual () {

    },
    hasRead () {},
    box () {
      const url = '/message/box'
      getAction(url).then(res => {
        console.log('res.data', res.data)
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
  .card-head{
  font-size: 20px;
  font-weight: bold;
  color: #474747 ;
  font-family: NSimSun;
  }
  .content-head{
    display: flex;
    align-items: center;
    height: 60px;
    width: 100%;
    padding: 0px 20px;
    background:#FFE0C7;
    border-radius: 10px;
  }
  .content-body{
    min-height: 1000px;
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
