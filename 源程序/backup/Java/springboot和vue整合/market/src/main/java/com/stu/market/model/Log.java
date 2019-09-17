package com.stu.market.model;

public class Log {
    private Integer id;
    private String opType;
    private Long opTime;
    private String opDetail;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getOpType() {
        return opType;
    }

    public void setOpType(String opType) {
        this.opType = opType;
    }

    public Long getOpTime() {
        return opTime;
    }

    public void setOpTime(Long opTime) {
        this.opTime = opTime;
    }

    public String getOpDetail() {
        return opDetail;
    }

    public void setOpDetail(String opDetail) {
        this.opDetail = opDetail;
    }
}
