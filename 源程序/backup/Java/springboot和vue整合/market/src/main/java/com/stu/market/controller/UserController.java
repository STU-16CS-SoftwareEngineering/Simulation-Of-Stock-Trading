package com.stu.market.controller;

import com.stu.market.model.User;
import com.stu.market.service.UserService;
import com.stu.market.serviceImpl.UserServiceImpl;
import com.stu.market.utils.JsonResult;
import com.stu.market.utils.MarketUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

@RestController
public class UserController {
    private static final Logger logger = LoggerFactory.getLogger(UserController.class);

    @Autowired
    private UserServiceImpl userService;

    @PostMapping("/login")
    public JsonResult login(@RequestParam("account") String account, @RequestParam("password") String password,
                            HttpServletResponse response) {
        try {
            HashMap<String, Object> map = userService.getUser(account);
            User user = (User) map.get("user");
            if (user == null) {
                return new JsonResult(200, "用户不存在", null);
            }
            if (MarketUtil.MD5(password + user.getSalt()).equals(user.getPassword())) {
                if (map.containsKey("token")) {
                    Cookie cookie = new Cookie("token", map.get("token").toString());
                    cookie.setPath("/");
                    cookie.setMaxAge(3600 * 24 * 5);
                    response.addCookie(cookie);
                }
                return new JsonResult(200, "登录成功", null);
            } else {
                return new JsonResult(200, "用户名或密码错误", null);
            }
        } catch (Exception e) {
            logger.error("登录异常" + e.getMessage());
            return new JsonResult(500, "服务器内部错误", null);
        }
    }

    @GetMapping("/logout")
    public JsonResult logout(@CookieValue("token") String token, HttpServletResponse response) {
        userService.logout(token);
        Cookie cookie = new Cookie("token", "");
        cookie.setMaxAge(0);
        response.addCookie(cookie);
        return new JsonResult(200, "注销成功", null);
    }

    @GetMapping("/getAccount")
    public JsonResult getAccount(HttpServletRequest request) {
        String token=null;
        HashMap<String,Object> map=null;
        Cookie[] cookies=request.getCookies();
        if (cookies!=null){
            for (Cookie cookie:cookies) {
                if ("token".equals(cookie.getName())){
                    token=cookie.getValue();
                    break;
                }
            }
            String account = userService.getAccount(token);
            map=new HashMap<>();
            map.put("account",account);
        }
        return new JsonResult(200, "ok", map);
    }

}
