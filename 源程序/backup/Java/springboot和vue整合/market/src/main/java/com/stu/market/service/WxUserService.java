package com.stu.market.service;

import com.stu.market.model.Log;
import com.stu.market.model.WxUser;

import java.util.List;

public interface WxUserService {
    public List<WxUser> getWxUser(int limit, int offset);

}
