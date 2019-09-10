package com.stu.market.service;

import com.stu.market.model.User;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Service;

import java.util.HashMap;


public interface UserService {
    public HashMap<String,Object> getUser(String account);

    public void logout(String token);

    public String getAccount(String token);

}
