package com.stu.market.serviceImpl;

import com.stu.market.dao.WxUserDao;
import com.stu.market.model.WxUser;
import com.stu.market.service.WxUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class WxUserServiceImpl implements WxUserService {

    @Autowired(required = false)
    private WxUserDao wxUserDao;

    @Override
    public List<WxUser> getWxUser(int limit, int offset) {
        return wxUserDao.getWxUser(limit,offset);
    }
}
