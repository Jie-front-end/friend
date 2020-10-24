<template>
  <div style="padding:30px">
    <!-- <div style="text-align:left">
    <el-button type="primary" plain @click="toMatch">按主性格匹配</el-button>
    <el-button type="warning" plain @click="toMatch">按反性格匹配</el-button>
    </div> -->
    <el-radio-group v-model="tabPosition" @change="changeTab" style="margin-bottom: 30px;">
      <el-radio-button label="first"></el-radio-button>
      <el-radio-button label="second"></el-radio-button>
      <el-radio-button label="third"></el-radio-button>
      <el-radio-button label="forth"></el-radio-button>
    </el-radio-group>
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
          {{ scope.row.sex }}
        </template>
      </el-table-column>
      <!-- <el-table-column label="出生时间" min-width="160" align="center">
        <template slot-scope="scope">
          {{ scope.row.date }}
        </template>
      </el-table-column> -->
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
          <div class="contentTitle">昵称</div>
          <div class="content">{{ form.nicknameme }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">性别</div>
          <div class="content">{{ form.sex }}</div>
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
          <div class="contentTitle">城市</div>
          <div class="content">{{ form.city }}</div>
        </div>
      </el-col>
      <!-- <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">婚否</div>
          <div class="content">{{ form.marriage }}</div>
        </div>
      </el-col> -->
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">十神性格</div>
          <div class="content">{{ form.advantage }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">缺点</div>
          <div class="content">{{ form.disadvantage }}</div>
        </div>
      </el-col>
      <el-col :md="8" :sm="12">
        <div class="content-wrap">
          <div class="contentTitle">其他</div>
          <div class="content">{{ form.other_coop }}</div>
        </div>
      </el-col>
      <!-- <el-col :md="8" :sm="12">
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
      </el-col> -->
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
      tableData:{},
      first:[],
      second:[],
      third:[],
      forth:[],
      tabPosition:''
    }
  },
  created() {
    this.fetchData()
  },
  methods:{
    changeTab(){
      if(this.tabPosition === 'first') {
        this.tableData = this.tableData.first
      } else if(this.tabPosition === 'second'){
        this.tableData = this.tableData.second
      } else if(this.tabPosition === 'third'){
        this.tableData = this.tableData.third
      } else {
        this.tableData = this.tableData.forth
      }
    },
    toMatch(){
      this.dialogVisible = false
      this.$emit('change','third')
    },
    fetchData(){
      this.listLoading = true
      const url = `/profile/recommend`
      getAction(url).then( res => {
          this.tableData = res.data.msg
      })
       this.listLoading = false
    },
    getUserDetail(id){
      this.dialogVisible = true
      // const url = 'admin/userdetail/' + id
        const url = `/profile/detail/`+ id
        getAction(url).then( res => {
            this.form = res.data.msg
        })
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


