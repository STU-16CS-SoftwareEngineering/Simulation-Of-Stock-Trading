package com.stu.market.serviceImpl;

import com.stu.market.dao.UserDao;
import com.stu.market.model.User;
import com.stu.market.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.StringRedisSerializer;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

@Service
public class UserServiceImpl implements UserService {

    @Autowired(required = false)
    private UserDao userDao;

    @Autowired
    private RedisTemplate<Object,Object> redisTemplate;


    @Override
    public HashMap<String,Object> getUser(String account) {
        HashMap<String,Object> map = new HashMap<>();
        User user=userDao.getUser(account);
        if (user!=null){
            map.put("user",user);
            String token= UUID.randomUUID().toString().replace("-","");
            map.put("token",token);
            redisTemplate.setKeySerializer(new StringRedisSerializer());
            redisTemplate.setValueSerializer(new StringRedisSerializer());
            redisTemplate.opsForValue().set(token,user.getAccount());
            redisTemplate.expire(token,1, TimeUnit.DAYS);
        }else {
            map.put("user",null);
        }
        return map;
    }

    @Override
    public void logout(String token) {
        redisTemplate.delete(token);
    }

    @Override
    public String getAccount(String token) {
        //return (String) redisTemplate.opsForValue().get(token);
        return (String) redisTemplate.boundValueOps(token).get();
    }


}
