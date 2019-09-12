package com.stu.market;

import com.stu.market.dao.UserDao;
import com.stu.market.model.User;
import com.stu.market.utils.MarketUtil;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.UUID;

@RunWith(SpringRunner.class)
@SpringBootTest
public class MarketApplicationTests {

    @Autowired(required = false)
    private UserDao userDao;

    @Test
    public void contextLoads() {
        User user =new User();
        user.setAccount("admin");
        String salt= UUID.randomUUID().toString().replace("-","").substring(0,5);
        user.setPassword(MarketUtil.MD5("123456"+salt));
        user.setSalt(salt);
        userDao.addUser(user);

    }

}
