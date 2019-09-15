<template>
  <div>
    <nav-header></nav-header>
    <el-container>
      <el-main>
        <h3>比赛名称</h3>
        <p>{{matchInfo.matchName}}</p>
        <h3>比赛简介</h3>
        <p>{{matchInfo.matchDetail}}</p>
        <h3>开始时间</h3>
        <p>{{formatTimeStamp(matchInfo.startTime)}}</p>
        <h3>结束时间</h3>
        <p>{{formatTimeStamp(matchInfo.endTime)}}</p>
        <h3>初始金额</h3>
        <p>{{matchInfo.initMoney}}</p>
        <h3>规则</h3>
        <p>{{matchInfo.matchRule}}</p>
      </el-main>
      <el-aside width="200px">
        <el-button @click="modifyMatch" type="info" >修改比赛</el-button>
        <span></span>
        <el-button @click="deleteMatch" type="info" >删除比赛</el-button>
      </el-aside>
    </el-container>
  </div>
</template>
<script>
import header from "@/components/Header";
import axios from "axios";
import Qs from "qs";
export default {
  name: "MatchDetail",
  components: {
    "nav-header": header
  },
  data() {
    return {
      matchInfo: {
        endTime: "",
        id: "",
        initMoney: "",
        matchDetail: "",
        matchName: "",
        matchRule: "",
        signTime: "",
        startTime: ""
      }
    };
  },
  mounted() {
    let matchName = this.$route.query.match_name;
    let url = `/getMatch?match_name=${matchName}`;
    axios
      .get(url)
      .then(res => {
        if (res.data.status == 200) {
          this.matchInfo = res.data.data;
          console.log(this.matchInfo);
        } else {
          this.$message(res.data.msg);
        }
      })
      .catch(err => {
        this.$message(err.message);
      });
  },
  methods: {
    formatTimeStamp(str) {
      return new Date(Number(str)*1000).Format("yyyy/MM/dd HH:mm:ss");
    },
    modifyMatch() {
      this.$router.push({name:'ModifyDetail', query:{match_name:this.matchInfo.matchName}});
    },
    deleteMatch() {
      this.$confirm("此操作将删除该比赛, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          axios({
            method: "post",
            url: "/deleteMatch",
            data: Qs.stringify({
              id: this.matchInfo.id
            })
          })
            .then(res => {
              if (res.data.status == 200) {
                this.$message({
                  type: "success",
                  message: "删除成功!"
                });
                this.$router.back();
              } else {
                this.$message(res.data.msg);
              }
            })
            .catch(err => {
              this.$message(err.message);
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除"
          });
        });
    }
  }
};
</script>
<style>
.ck-content {
  min-height: 250px !important;
  margin-bottom: 10px !important;
}
.el-main{
  padding-left: 50px;
}
.el-aside{
  padding-top: 10px;
}
.el-aside button{
  margin-bottom: 10px;
}
</style>