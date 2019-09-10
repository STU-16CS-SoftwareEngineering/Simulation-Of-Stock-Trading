package com.stu.market.dao;

import com.stu.market.model.User;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

@Mapper
public interface UserDao {
    public static final String TABLE_NAME="manager_db";
    public static final String INSERT_FIELDS="(account,password,salt)";

    @Insert("insert into " +TABLE_NAME+INSERT_FIELDS+"values (#{account},#{password},#{salt})")
    public int addUser(User user);

    @Select("select * from "+TABLE_NAME+" where account=#{account}")
    public User getUser(String account);
}
