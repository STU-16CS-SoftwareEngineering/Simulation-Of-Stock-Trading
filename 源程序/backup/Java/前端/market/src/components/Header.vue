<template>
  <div>
    <div class="container">
      <router-link class="logo" to="/match">
        <h1>模拟股市</h1>
        <h3>管理员</h3>
      </router-link>
      <div class="userInfo">
        <p>你好, {{account}}!</p>
        <el-button type="danger" round @click="logout">退出登陆</el-button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Header",
  computed: {
    account() {
      return this.$store.state.account;
    }
  },
  mounted() {
    this.getAccount();
  },
  methods: {
    logout() {
      axios
        .get("logout", {
          withCredentials: true
        })
        .then(res => {
          if (res.data.status == 200) {
            this.$alert("退出成功！", "提示", {
              confirmButtonText: "确定",
              callback: action => {
                this.$router.push({ path: "/" });
              }
            });
          } else {
            this.$message(res.data.msg);
          }
        })
        .catch(err => {
          this.$message(err.message);
        });
    },
    getAccount() {
      axios
        .get("/getAccount", {
          withCredentials: true
        })
        .then(res => {
          if (res.status == 200) {
            this.$store.commit("updateUserName", res.data.data.account);
          }
        })
        .catch(err => {
          this.$message(err.message);
        });
    }
  }
};
</script>
<style scoped>
a {
  text-decoration: none;
  color: #333;
}
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background: url('../assets/img/binding_dark.png');
  /* border-bottom: 1px solid rgba(122, 122, 122, 0.8); */
}
.container .userInfo {
  display: flex;
}
.container p {
  text-align: center;
  margin: 10px 10px;
  color: #fff;
}
.container .logo {
  display: flex;
}
.container .logo h1 {
  margin: 0 20px;
  color: #ed7d31;
}
.container .logo h3 {
  margin: 0;
  align-self: flex-end;
  color: #767676;
}
</style>