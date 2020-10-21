<template>
  <div style="padding:30px">
    <div style="text-align:left">
    <el-button type="primary" plain @click="toMatch">按主性格匹配</el-button>
    <el-button type="warning" plain @click="toMatch">按反性格匹配</el-button>
    </div>
    <el-table
      style="margin-top:30px"
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
      :header-cell-style="{ background: '#f8f8f8' }"
    >
      <!-- <el-table-column align="center" label="ID" min-width="80">
        <template slot-scope="scope">
          <el-button type="text" @click="getUserDetail(scope.$index + 1 )">{{ scope.$index + 1}}</el-button>
        </template>
      </el-table-column> -->
    <el-table-column
      type="index"
      width="50"
      align="center">
    </el-table-column>
      <el-table-column label="昵称" min-width="120" align="center">
        <template slot-scope="scope">
          <el-button type="text" @click="getUserDetail(scope.row.nickname)">{{scope.row.nickname }}</el-button>
        </template>
      </el-table-column>
      <el-table-column label="性别" min-width="100" align="center">
        <template slot-scope="scope">
          {{ scope.row.gender }}
        </template>
      </el-table-column>
      <el-table-column label="出生时间" min-width="160" align="center">
        <template slot-scope="scope">
          {{ scope.row.date }}
        </template>
      </el-table-column>
      <el-table-column label="城市" min-width="140" align="center">
        <template slot-scope="scope">
          {{ scope.row.province }}
        </template>
      </el-table-column>
      <!-- <el-table-column label="婚否" min-width="100" align="center">
        <template slot-scope="scope">
          {{ scope.row.marriage }}
        </template>
      </el-table-column>
      <el-table-column label="工作" min-width="120" align="center">
        <template slot-scope="scope">
          {{ scope.row.job }}
        </template>
      </el-table-column> -->
    </el-table>
    <el-dialog title="用户详情" :visible.sync="dialogVisible" width="750px">
    <!-- <p class="block-title bgColor">预约信息</p> -->
    <div style="text-align:right">
      <el-button  type="warning" plain @click="toMatch">私信</el-button>
    </div>
    <el-row style="margin-left:50px">
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">姓名</div>
          <div class="content">{{ form.name }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">性别</div>
          <div class="content">{{ form.gender }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">出生时间</div>
          <div class="content">{{ form.date }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">出生地</div>
          <div class="content">{{ form.province }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">婚否</div>
          <div class="content">{{ form.marriage }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">工作</div>
          <div class="content">{{ form.job }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">联系方式</div>
          <div class="content">{{ form.contact }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">从哪看到</div>
          <div class="content">{{ form.where }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">平台</div>
          <div class="content">{{ form.platform }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">IP</div>
          <div class="content">{{ form.ip }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">选择谁</div>
          <div class="content">{{ form.choose }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">提交时间</div>
          <div class="content">{{ form.calendar }}</div>
        </div>
      </el-col>
      </el-row>
    </el-dialog>
  </div>
</template>
<script>
import { postAction } from '@/api/manage'

export default {
  data() {
    return {
      list: [
        {nickname:'a'}
      ],
      listLoading: false,
      dialogVisible:false,
      form:{}
    }
  },
  // created() {
  //   this.fetchData()
  // },
  methods:{
    toMatch(){
      this.dialogVisible = false
      this.$emit('change','third')
    },
    fetchData(){
      this.listLoading = true
      const url = 'admin/userlist'
      postAction(url).then( res => {
         this.list = res.data
         this.listLoading = false
      })
    },
    getUserDetail(id){
      this.dialogVisible = true
      // const url = 'admin/userdetail/' + id
      // postAction(url).then( res => {
      //   this.form = res.data
      //   console.log(res)
      // })
    }
  }
}
</script>
<style scoped>
.content-wrap {
  font-size: 14px;
  font-weight: 400;
  display: flex;
  align-items: center;
  margin-right:10px ;
  justify-content: flex-start;
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
  .pb20 {
    padding-bottom: 20px;
  }
</style>


