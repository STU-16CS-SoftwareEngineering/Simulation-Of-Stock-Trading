package com.stu.market.controller;

import com.stu.market.serviceImpl.LogServiceImpl;
import com.stu.market.utils.JsonResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LogController {

    @Autowired
    private LogServiceImpl logService;

    @GetMapping("/log")
    public JsonResult getLog(@RequestParam("page") int page){
        int limit=(page-1)*10;
        int offset=10;
        return new JsonResult(200,"ok",logService.getLog(limit,offset));
    }
}
