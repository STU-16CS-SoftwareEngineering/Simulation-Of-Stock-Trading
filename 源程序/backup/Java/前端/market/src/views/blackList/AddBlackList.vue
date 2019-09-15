<template>
  <div>
    <nav-header></nav-header>
    <el-container>
      <el-main>
        <el-form ref="form" :model="blackListInfo" label-width="80px">
          <el-form-item label="微信ID">
            <el-input v-model="blackListInfo.wxid"></el-input>
          </el-form-item>
          <el-form-item label="拉黑原因">
            <el-input v-model="blackListInfo.reason"></el-input>
          </el-form-item>
          <el-button type="primary" @click="onSubmit">拉黑用户</el-button>
        </el-form>
      </el-main>
      <el-aside width="200px">
        <nav-aside index="4-2"></nav-aside>
      </el-aside>
    </el-container>
  </div>
</template>
<script>
import header from "@/components/Header";
import aside from "@/components/Aside";
import axios from "axios";
export default {
  name: "AddMatch",
  components: {
    "nav-header": header,
    "nav-aside": aside
  },
  data() {
    return {
      blackListInfo: {
        wxid:'',
        op_time:'',
        reason:''
      }
    };
  },
  methods: {
    onSubmit() {
        // 注意秒级时间戳
      this.blackListInfo.op_time = (Date.parse(new Date())/1000).toString();
      axios.post("/addBlackList", this.blackListInfo).then(res => {
        if (res.data.status == 200) {
          this.$alert(res.data.msg, "提示", {
            confirmButtonText: "确定",
            callback: action => {
              this.$router.push({path:"/blacklist"});
            }
          });
        }else{
            this.$message(res.data.msg);
        }
      }).catch((err)=>{
      this.$message(err.message);
    });;
    }
  }
};
</script>
<style>
.ck-content {
  min-height: 250px !important;
  margin-bottom: 10px !important;
}
</style>