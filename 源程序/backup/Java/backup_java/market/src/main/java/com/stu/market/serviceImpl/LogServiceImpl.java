package com.stu.market.serviceImpl;

import com.stu.market.dao.LogDao;
import com.stu.market.model.Log;
import com.stu.market.service.LogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class LogServiceImpl implements LogService {

    @Autowired(required = false)
    private LogDao logDao;

    @Override
    public List<Log> getLog(int limit, int offset) {
        return logDao.getLog(limit,offset);
    }
}
