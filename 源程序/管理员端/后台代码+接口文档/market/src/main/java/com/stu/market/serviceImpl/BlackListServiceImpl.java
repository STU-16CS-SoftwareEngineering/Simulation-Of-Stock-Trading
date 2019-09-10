package com.stu.market.serviceImpl;

import com.alibaba.fastjson.JSONObject;
import com.stu.market.dao.BlackListDao;
import com.stu.market.model.BlackList;
import com.stu.market.service.BlackListService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BlackListServiceImpl implements BlackListService {

    @Autowired(required = false)
    private BlackListDao blackListDao;

    @Override
    public void addBlackList(JSONObject jsonObject) {
        BlackList blackList=new BlackList();
        blackList.setWxid(jsonObject.getString("wxid"));
        blackList.setOpTime(Integer.valueOf(jsonObject.getString("op_time")));
        blackList.setReason(jsonObject.getString("reason"));
        blackListDao.addBlackList(blackList);
    }

    @Override
    public List<BlackList> getBlackList(int limit, int offser) {
        return blackListDao.getBlackList(limit,offser);
    }

    @Override
    public void deleteBlackListById(Integer id) {
        blackListDao.deleteBlackListById(id);
    }

    @Override
    public BlackList getBlackListByWxid(String wxid) {
        return blackListDao.getBlackListByWxid(wxid);
    }

    @Override
    public BlackList getBlackListById(Integer id) {
        return blackListDao.getBlackListById(id);
    }
}
