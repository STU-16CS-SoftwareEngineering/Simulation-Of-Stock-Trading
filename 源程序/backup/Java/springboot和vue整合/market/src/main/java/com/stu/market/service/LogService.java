package com.stu.market.service;

import com.stu.market.model.Log;
import com.stu.market.utils.JsonResult;

import java.util.List;

public interface LogService {
    public List<Log> getLog(int limit,int offset);
}
