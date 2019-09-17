package com.stu.market.service;

import com.alibaba.fastjson.JSONObject;
import com.stu.market.model.BlackList;

import java.util.List;

public interface BlackListService {
    public void addBlackList(JSONObject jsonObject);

    public List<BlackList> getBlackList(int limit, int offser);

    public void deleteBlackListById(Integer id);

    public BlackList getBlackListByWxid(String wxid);

    public BlackList getBlackListById(Integer id);
}
