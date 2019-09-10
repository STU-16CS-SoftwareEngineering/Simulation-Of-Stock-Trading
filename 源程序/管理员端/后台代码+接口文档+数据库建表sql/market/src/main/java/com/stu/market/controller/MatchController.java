package com.stu.market.controller;

import com.alibaba.fastjson.JSONObject;
import com.stu.market.model.Match;
import com.stu.market.serviceImpl.MatchServiceImpl;
import com.stu.market.utils.JsonResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
public class MatchController {

    @Autowired
    private MatchServiceImpl matchService;

    @PostMapping("/addMatch")
    public JsonResult addMatch(@RequestBody(required = false) JSONObject jsonObject){
        String matchName=jsonObject.getString("match_name");
        Match match=matchService.getMatchByName(matchName);
        if (match==null){
            return matchService.addMatch(jsonObject);
        }else{
            System.out.println(match.getMatchName());
            return new JsonResult(400,"该比赛已存在",match);
        }
    }

    @GetMapping("/getAllMatch")
    public JsonResult getAllMatch(@RequestParam("page") int page){
        int limit=(page-1)*10;
        int offset=10;
        return new JsonResult(200,"ok",matchService.getMatch(limit,offset));
    }

    @PostMapping("/updateMatch")
    public JsonResult updateMatch(@RequestBody(required = false) JSONObject jsonObject){
        Integer id=Integer.valueOf(jsonObject.getString("id"));
        Match match=matchService.getMatchById(id);
        if (match!=null){
            matchService.updateMatch(jsonObject);
            return new JsonResult(200,"ok",null);
        }else{
            return new JsonResult(400,"该比赛不存在",null);
        }
    }

    @PostMapping("/deleteMatch")
    public JsonResult deleteMatch(@RequestParam("id") Integer id){
        Match match=matchService.getMatchById(id);
        if (match!=null){
            matchService.deleteMatch(id);
            return new JsonResult(200,"ok",null);
        }else{
            return new JsonResult(400,"该比赛不存在",null);
        }
    }

    @GetMapping("/getMatch")
    public JsonResult getMatch(@RequestParam("match_name") String matchName){
        Match match=matchService.getMatchByName(matchName);
        if (match!=null){
            return new JsonResult(200,"ok",match);
        }else{
            return new JsonResult(200,"无该比赛记录",null);
        }
    }
}
