package com.stu.market.dao;

import com.stu.market.model.Match;
import com.stu.market.model.User;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface MatchDao {
    public static final String TABLE_NAME="match_db";
    public static final String INSERT_FIELDS="(match_name,match_detail,match_rule,start_time,sign_time,end_time,init_money)";

    @Insert("insert into " +TABLE_NAME+INSERT_FIELDS+"values (#{matchName},#{matchDetail},#{matchRule},#{startTime},#{signTime},#{endTime},#{initMoney})")
    public int addMatch(Match match);

    @Select({"select * from "+TABLE_NAME+" where match_name=#{match_name}"})
    public Match getMatchByName(String match_name);

    @Select({"select * from "+TABLE_NAME+" limit #{limit},#{offset}"})
    public List<Match> getMatch(int limit,int offset);

    @Select({"select * from "+TABLE_NAME+" where id=#{id}"})
    public Match getMatchById(Integer id);

    @Update({"update "+TABLE_NAME+" set match_name=#{matchName},match_detail=#{matchDetail},match_rule=#{matchRule}," +
            "start_time=#{startTime},sign_time=#{signTime},end_time=#{endTime},init_money=#{initMoney} where id=#{id}"})
    public void updateMatch(Match match);

    @Delete("delete from "+TABLE_NAME+" where id=#{id}")
    public void deleteMatchById(Integer id);
}
