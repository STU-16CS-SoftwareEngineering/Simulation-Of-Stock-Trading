package com.stu.market.dao;

import com.stu.market.model.Log;
import com.stu.market.model.Match;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface LogDao {
    public static final String TABLE_NAME="log_db";
    public static final String INSERT_FIELDS="(op_type,op_time,op_detail)";

    @Insert("insert into " +TABLE_NAME+INSERT_FIELDS+"values (#{opType},#{opTime},#{opDetail})")
    public void addLog(Log log);

    @Select({"select * from "+TABLE_NAME+" limit #{limit},#{offset}"})
    public List<Log> getLog(int limit, int offset);
}
