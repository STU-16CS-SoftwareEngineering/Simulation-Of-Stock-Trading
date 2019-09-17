package com.stu.market.controller;

import com.alibaba.fastjson.JSONObject;
import com.stu.market.model.BlackList;
import com.stu.market.serviceImpl.BlackListServiceImpl;
import com.stu.market.utils.JsonResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class BlackListController {

    @Autowired
    private BlackListServiceImpl blackListService;

    @PostMapping("/addBlackList")
    public JsonResult addBlackListUser(@RequestBody(required = false)JSONObject jsonObject){
        String wxid=jsonObject.getString("wxid");
        BlackList blackList=blackListService.getBlackListByWxid(wxid);
        if (blackList==null){
            blackListService.addBlackList(jsonObject);
            return new JsonResult(200,"ok",null);
        }else{
            return new JsonResult(400,"该用户已被拉黑",blackList);
        }
    }

    @PostMapping("/deleteBlackList")
    public JsonResult deleteBlackListUser(@RequestParam("id") Integer id){
        BlackList blackList=blackListService.getBlackListById(id);
        if (blackList!=null){
            blackListService.deleteBlackListById(id);
            return new JsonResult(200,"ok",null);
        }else{
            return new JsonResult(400,"该用户不存在",null);
        }
    }

    @GetMapping("/getAllBlackList")
    public JsonResult getAllBlackList(@RequestParam("page") int page){
        int limit=(page-1)*10;
        int offset=10;
        return new JsonResult(200,"ok",blackListService.getBlackList(limit,offset));
    }

    @GetMapping("/getBlackList")
    public JsonResult getMatch(@RequestParam("wxid") String wxid){
        BlackList blackList=blackListService.getBlackListByWxid(wxid);
        if (blackList!=null){
            return new JsonResult(200,"ok",blackList);
        }else{
            return new JsonResult(200,"无该用户记录",null);
        }
    }
}
