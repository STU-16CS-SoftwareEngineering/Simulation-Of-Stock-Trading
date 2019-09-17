package com.stu.market.aspect;

import com.stu.market.dao.LogDao;
import com.stu.market.model.Log;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LogAspect {

    @Autowired(required = false)
    private LogDao logDao;

    private static final Logger logger = LoggerFactory.getLogger(LogAspect.class);

    @Before(value = "execution(* com.stu.market.controller.*Controller.*(..))")
    public void beforeMethod(JoinPoint joinPoint) {
        Log log=new Log();
        StringBuilder sb = new StringBuilder();
        log.setOpType(joinPoint.getSignature().getName());
        log.setOpTime(System.currentTimeMillis() / 1000);
        if (!"login".equals(joinPoint.getSignature().getName())){
            for (Object arg : joinPoint.getArgs()) {
                sb.append("arg:" + arg.toString() + " | ");
            }
            log.setOpDetail(sb.toString());
        }
        else{
            log.setOpDetail(null);
        }
        logger.info(joinPoint.getSignature().getName()+" "+sb.toString());
        logDao.addLog(log);
    }
}
