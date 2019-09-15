<template>
  <div>
    <el-menu :default-active="index" class="el-menu-vertical-demo" @select="goPage">
      <el-submenu index="1">
        <template slot="title">
          <span class="sub-title">比赛</span>
        </template>
        <el-menu-item index="1-1">查看比赛</el-menu-item>
        <el-menu-item index="1-2">增加比赛</el-menu-item>
      </el-submenu>
      <el-menu-item index="2">
        <span slot="title">查看日志</span>
      </el-menu-item>
      <el-menu-item index="3">
        <span slot="title">查看用户</span>
      </el-menu-item>
      <el-submenu index="4">
        <template slot="title">
          <span class="sub-title">用户黑名单</span>
        </template>
        <el-menu-item index="4-1">查看黑名单</el-menu-item>
        <el-menu-item index="4-2">添加黑名单</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>
<script>
export default {
  name: "Aside",
  props: {
    index: String
  },
  methods: {
    goPage(index) {
      let url = "/match";
      this.index = index;
      switch (this.index) {
        case "1-1": {
          url = "/match";
          break;
        }
        case "1-2":{
          url="/addMatch";
          break;
        }
        case "2":{
          url = "/log";
          break;
        }
        case "3":{
          url = "/wxUser";
          break;
        }
        case "4-1":{
          url='/blacklist';
          break;
        }
        case "4-2":{
          url="/addBlacklist"
        }
      }
      console.log(url);
      this.$router.push({ path: url });
    }
  }
};
</script>
<style scoped>
.el-menu-item.is-active {
  background-color: aliceblue;
}
.sub-title {
  color: #ababab;
}
</style>