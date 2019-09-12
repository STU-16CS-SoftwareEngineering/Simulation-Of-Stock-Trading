package com.stu.market.controller;

import com.stu.market.serviceImpl.WxUserServiceImpl;
import com.stu.market.utils.JsonResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WxUserController {
    @Autowired
    private WxUserServiceImpl wxUserService;

    @GetMapping("/wxUser")
    public JsonResult getWxUser(@RequestParam("page") int page){
        int limit=(page-1)*10;
        int offset=10;
        return new JsonResult(200,"ok",wxUserService.getWxUser(limit,offset));
    }
}
