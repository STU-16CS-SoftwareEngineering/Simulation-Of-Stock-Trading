package com.stu.market.service;

import com.alibaba.fastjson.JSONObject;
import com.stu.market.model.Match;
import com.stu.market.utils.JsonResult;

import java.util.List;

public interface MatchService {
    public JsonResult addMatch(JSONObject jsonObject);

    public Match getMatchByName(String match_name);

    public List<Match> getMatch(int limit,int offset);

    public Match getMatchById(Integer id);

    public void updateMatch(JSONObject jsonObject);

    public void deleteMatch(Integer id);
}
