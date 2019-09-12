package com.stu.market.dao;

import com.stu.market.model.Log;
import com.stu.market.model.WxUser;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface WxUserDao {
    public static final String TABLE_NAME="user_db";

    @Select({"select * from "+TABLE_NAME+" limit #{limit},#{offset}"})
    public List<WxUser> getWxUser(int limit, int offset);
}
