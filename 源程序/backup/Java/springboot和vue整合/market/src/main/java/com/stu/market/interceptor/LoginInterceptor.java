package com.stu.market.interceptor;

import com.alibaba.fastjson.JSONObject;
import com.stu.market.model.User;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.StringRedisSerializer;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.PrintWriter;

@Component
public class LoginInterceptor implements HandlerInterceptor {
    private static final Logger logger = LoggerFactory.getLogger(LoginInterceptor.class);

    @Autowired
    private RedisTemplate<Object,Object> redisTemplate;

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String token=null;
        Cookie[] cookies= request.getCookies();
        if (cookies != null) {
            for (Cookie cookie:cookies){
                if ("token".equals(cookie.getName())){
                    token=cookie.getValue();
                    break;
                }
            }
        }
        //String account=(String)redisTemplate.opsForValue().get(token);
        String account=null;
        try{
            account=(String)redisTemplate.boundValueOps(token).get();
        }catch (Exception e){
            logger.error(e.getMessage());
        }
        if (account!=null){
            return true;
        }
        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json; charset=utf-8");
        PrintWriter out = null ;
        try{
            JSONObject res = new JSONObject();
            res.put("status","401");
            res.put("msg","用户未登录");
            out = response.getWriter();
            out.append(res.toString());
            return false;
        }
        catch (Exception e){
            e.printStackTrace();
            response.sendError(500);
            return false;
        }
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {

    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {

    }
}
