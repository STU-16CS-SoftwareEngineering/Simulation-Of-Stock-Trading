package com.stu.market.dao;

import com.stu.market.model.BlackList;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface BlackListDao {
    public static final String TABLE_NAME="blacklist_db";
    public static final String INSERT_FIELDS="(wxid,reason,op_time)";

    @Insert("insert into " +TABLE_NAME+INSERT_FIELDS+"values (#{wxid},#{reason},#{opTime})")
    public int addBlackList(BlackList blackList);

    @Select({"select * from "+TABLE_NAME+" limit #{limit},#{offset}"})
    public List<BlackList> getBlackList(int limit,int offset);

    @Delete("delete from "+TABLE_NAME+" where id=#{id}")
    public void deleteBlackListById(Integer id);

    @Select({"select * from "+TABLE_NAME+" where id=#{id}"})
    public BlackList getBlackListById(Integer id);

    @Select({"select * from "+TABLE_NAME+" where wxid=#{wxid}"})
    public BlackList getBlackListByWxid(String wxid);

}
