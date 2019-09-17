package com.stu.market.serviceImpl;

import com.alibaba.fastjson.JSONObject;
import com.stu.market.dao.MatchDao;
import com.stu.market.dao.UserDao;
import com.stu.market.model.Match;
import com.stu.market.service.MatchService;
import com.stu.market.utils.JsonResult;
import com.stu.market.utils.MarketUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class MatchServiceImpl implements MatchService {
    public static final Logger logger= LoggerFactory.getLogger(MatchServiceImpl.class);

    @Autowired(required = false)
    private MatchDao matchDao;

    @Override
    public JsonResult addMatch(JSONObject jsonObject) {
//        SimpleDateFormat format =  new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        try{
            Match match=new Match();
            match.setMatchName(jsonObject.getString("match_name"));
            match.setMatchDetail(jsonObject.getString("match_detail"));
            match.setMatchRule(jsonObject.getString("match_rule"));
//            String startTime=jsonObject.getString("start_time");
//            String signTime=jsonObject.getString("sign_time");
//            String endTime=jsonObject.getString("end_time");
//            match.setStartTime(Integer.parseInt(String.valueOf(format.parse(startTime).getTime()/1000)));
//            match.setSignTime(Integer.parseInt(String.valueOf(format.parse(signTime).getTime()/1000)));
//            match.setEndTime(Integer.parseInt(String.valueOf(format.parse(endTime).getTime()/1000)));
            match.setStartTime(Integer.valueOf(jsonObject.getString("start_time")));
            match.setSignTime(Integer.valueOf(jsonObject.getString("sign_time")));
            match.setEndTime(Integer.valueOf(jsonObject.getString("end_time")));
            match.setInitMoney(Integer.valueOf(jsonObject.getString("init_money")));
            matchDao.addMatch(match);
            return new JsonResult(200,"新增比赛成功",null);
        }catch (Exception e){
            logger.error(e.getMessage());
            return new JsonResult(400,"参数格式错误",null);
        }
    }

    @Override
    public Match getMatchByName(String match_name) {
        return matchDao.getMatchByName(match_name);
    }

    @Override
    public List<Match> getMatch(int limit, int offset) {
        return matchDao.getMatch(limit,offset);
    }

    @Override
    public Match getMatchById(Integer id) {
        return matchDao.getMatchById(id);
    }

    @Override
    public void updateMatch(JSONObject jsonObject) {
        Integer id = Integer.valueOf(jsonObject.getString("id"));
        Match match=new Match();
        match.setId(id);
        match.setMatchName(jsonObject.getString("match_name"));
        match.setMatchDetail(jsonObject.getString("match_detail"));
        match.setMatchRule(jsonObject.getString("match_rule"));
        match.setStartTime(Integer.valueOf(jsonObject.getString("start_time")));
        match.setSignTime(Integer.valueOf(jsonObject.getString("sign_time")));
        match.setEndTime(Integer.valueOf(jsonObject.getString("end_time")));
        match.setInitMoney(Integer.valueOf(jsonObject.getString("init_money")));
        matchDao.updateMatch(match);
    }

    @Override
    public void deleteMatch(Integer id) {
        matchDao.deleteMatchById(id);
    }
}
