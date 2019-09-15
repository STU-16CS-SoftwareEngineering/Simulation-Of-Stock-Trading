<template>
  <div>
    <nav-header></nav-header>
    <el-container>
      <el-main>
        <el-form ref="form" :model="matchInfo" label-width="80px">
          <el-form-item label="比赛名称">
            <el-input v-model="matchInfo.match_name"></el-input>
          </el-form-item>
          <el-form-item label="简介">
            <el-input v-model="matchInfo.match_detail"></el-input>
          </el-form-item>
          <el-form-item label="比赛时间">
            <el-date-picker
              v-model="timeVal"
              type="datetimerange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
            ></el-date-picker>
          </el-form-item>
          <el-form-item label="初始金额">
            <el-input v-model="matchInfo.init_money"></el-input>
          </el-form-item>
          <ckeditor :editor="editor" v-model="matchInfo.match_rule" :config="editorConfig"></ckeditor>
          <el-button type="primary" @click="onSubmit">发布比赛</el-button>
        </el-form>
      </el-main>
      <el-aside width="200px">
        <nav-aside index="1-2"></nav-aside>
      </el-aside>
    </el-container>
  </div>
</template>
<script>
import header from "@/components/Header";
import aside from "@/components/Aside";
import axios from "axios";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import "@ckeditor/ckeditor5-build-classic/build/translations/zh-cn";
export default {
  name: "AddMatch",
  components: {
    "nav-header": header,
    "nav-aside": aside
  },
  data() {
    return {
      editor: null,
      timeVal: [new Date(), new Date()],
      matchInfo: {
        match_name: "",
        match_detail: "",
        match_rule: "",
        start_time: "",
        sign_time: "",
        end_time: "",
        init_money: ""
      },
      editor: ClassicEditor,
      editorConfig: {
        language: "zh-cn",
        height: "800px",
        toolbar: [
          "heading", //段落
          "|", //分隔
          "bold", //加粗
          "italic", //倾斜
          "link", //超链接
          "bulletedList", //项目列表
          "numberedList", //编号列表
          "blockQuote", //块引用
          "undo", //撤销
          "redo" //重做
        ]
      }
    };
  },
  methods: {
    onSubmit() {
        // 注意秒级时间戳
      this.matchInfo.start_time = (Date.parse(this.timeVal[0])/1000).toString();
      this.matchInfo.end_time = (Date.parse(this.timeVal[1])/1000).toString();
      this.matchInfo.sign_time = (Date.parse(new Date())/1000).toString();
      axios.post("/addMatch", this.matchInfo).then(res => {
        if (res.data.status == 200) {
          this.$alert(res.data.msg, "提示", {
            confirmButtonText: "确定",
            callback: action => {
              this.$router.push({ path: "/match" });
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