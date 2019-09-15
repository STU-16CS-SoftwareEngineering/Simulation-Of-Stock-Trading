<template>
  <div class="blacklist">
    <nav-header></nav-header>
    <el-container>
      <el-main>
        <div class="controls">
          <h3>操作日志栏</h3>
          <div class="pagebtn">
            <el-button
              type="primary"
              icon="el-icon-arrow-left"
              round
              @click="changePage('left')"
            >上一页</el-button>
            <el-button
              type="primary"
              icon="el-icon-arrow-right"
              round
              @click="changePage('right')"
            >下一页</el-button>
          </div>
        </div>
        <el-table :data="tableData" :cell-class-name="setCellStyle">
          <el-table-column prop="id" label="id" width="100"></el-table-column>
          <el-table-column prop="opType" label="修改类型"></el-table-column>
          <el-table-column label="修改时间" width="200">
            <template slot-scope="scope">
              <span>{{transformTimestamp(scope.row.opTime)}}</span>
            </template>
          </el-table-column>
          <el-table-column prop="opDetail" label="修改详情"></el-table-column>
        </el-table>
      </el-main>
      <el-aside width="200px">
        <nav-aside index="2"></nav-aside>
      </el-aside>
    </el-container>
  </div>
</template>
<script>
import header from "@/components/Header";
import aside from "@/components/Aside";
import axios from "axios";
export default {
  name: "Log",
  components: {
    "nav-header": header,
    "nav-aside": aside
  },
  data() {
    return {
      tableData: [],
      page: 1
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    transformTimestamp(time) {
      return new Date(Number(time)*1000).Format("yyyy/MM/dd HH:mm:ss");
    },
    changePage(type) {
      if (type == "left") {
        if (this.page == 1) {
          this.$message("当前是第一页");
          return;
        } else {
          this.page--;
          this.getData();
        }
      } else if (type == "right") {
        this.page++;
        let url = `/getAllBlackList?page=${this.page}`;
        axios
          .get(url)
          .then(res => {
            if (res.data.status == 200) {
              if (res.data.data.length > 0) {
                this.tableData = res.data.data;
              } else {
                this.$message("没有更多数据了！");
                this.page--;
              }
            } else {
              this.$message(res.data.msg);
            }
          })
          .catch(err => {
            this.$message(err.message);
          });
      }
    },
    getData() {
      let url = `/log?page=${this.page}`;
      axios
        .get(url)
        .then(res => {
          if (res.data.status == 200) {
            this.tableData = res.data.data;
          } else {
            this.$message(res.data.msg);
          }
        })
        .catch(err => {
          this.$message(err.message);
        });
    },
    setCellStyle() {
      return "el-table-td";
    }
  }
};
</script>
<style lang="scss">
.blacklist {
  .el-table,
  .el-table th,
  .el-table tr {
    background: transparent;
  }
  .el-table-td {
    padding: 6px !important;
  }
  .el-main .controls {
    display: flex;
    justify-content: space-between;
  }
  .el-main .pagebtn {
    display: flex;
    justify-content: flex-end;
    margin: 10px;
  }
}
</style>