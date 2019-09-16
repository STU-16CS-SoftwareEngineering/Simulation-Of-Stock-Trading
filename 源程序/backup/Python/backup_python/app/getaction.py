#! usr/bin/python3
# -*- coding: utf-8 -*-


from flask import jsonify
import time
import hashlib
import mysql.connector
from app import stock
from app import competitor
from flask import request
from app import ssql
import requests


def dueR(r, v):  # 将字典r的value项改成v的值，并且转成json
    r['value'] = v
    return jsonify(r)


def checkPSW(a, b):  # in：用户名，密码 out：真假 for：检测出密码不正确返回真
    if a == b:
        return False
    else:
        return True


def checkTOKEN(token, mydb):  # in：token,mydb out：wxid for：检测出token的用户id
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT wxid FROM user_db WHERE token = %s", (token,))
        myresult = mycursor.fetchone()
        #mycursor.close()
        # print(myresult)
    except:
        return None
    else:
        if myresult != None:
            return myresult[0]
    return None


def getTimeStamp():  # 获取10位整数时间戳
    return int(time.time())


def getToken(user):  # 加密获取token
    md5 = hashlib.md5()
    token = user + '-' + str(getTimeStamp())
    md5.update(token.encode('utf-8'))
    return md5.hexdigest()


def topstock():
    url = "http://hq.sinajs.cn/format=text&func=StockList.fill1();StockList.refresh();Util.delScriptLoader('0');&list=stock_sh_up_d_10,stock_sh_down_d_10,stock_sz_up_d_10,stock_sz_down_d_10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r.text


def login(mydb, user, password):
    r = {
        'value': 0,
        'token': ''
    }
    # 1： 正常、 -1：密码错误、 -2：封号、 -101：数据库连接失败、 -102：更新token异常、 -103：更新token失败（未注册）
    if checkPSW(user, password):
        return dueR(r, -1)

    # mycon = ssql.SQLink()
    # mydb = mycon.get_db()
    if mydb == None:
        return dueR(r, -101)

    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM blacklist_db WHERE wxid = %s", (user,))
        myresult = mycursor.fetchone()
    except:
        return dueR(r, -102)
    else:
        if myresult == None:
            return dueR(r, -2)
        if myresult[0] > 0:
            return dueR(r, -2)
        #mycursor.close()

    try:
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT count(*) FROM user_db WHERE wxid = %s", (user,))
        myresult = mycursor.fetchone()
    except:
        return dueR(r, -102)
    else:
        if myresult == None:
            return dueR(r, -102)
        if myresult[0] == 0:
            return dueR(r, -103)
        #mycursor.close()

    token = getToken(user)
    try:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE user_db SET token=%s WHERE wxid=%s", (token, user))
        mydb.commit()
        row = mycursor.rowcount
        #mycursor.close()
    except:
        r['value'] = -102
    else:
        if row > 0:
            r['value'] = 1
            r['token'] = token
        else:
            r['value'] = -103
    return jsonify(r)


def regist(mydb, user, password, heading, nick):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：密码错误、 -101：数据库连接失败、 -102：插入异常（重复注册）、 -103：插入失败
    if checkPSW(user,password):
        return dueR(r, -1)
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT count(*) FROM user_db WHERE wxid = %s", (user,))
        myresult = mycursor.fetchone()
    except:
        return dueR(r, -103)
    else:
        if myresult == None:
            return dueR(r, -103)
        if myresult[0] > 0:
            return dueR(r, -102)
        #mycursor.close()
    
    try:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO user_db (wxid, heading, regist_time, nickName) VALUES (%s, %s, %s, %s)", (user, heading, getTimeStamp(), nick))
        mydb.commit()
    except:
        r['value'] = -102
    else:
        if mycursor.rowcount > 0:
            r['value'] = 1
        else:
            r['value'] = -103
    #mycursor.close()
    return jsonify(r)


def buyOrder(mydb, token, matchID, stockID, buyNum, stockPrice):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    try:
        buyNum = int(buyNum)
        balance = competitor.getBalance(mydb, matchID, user)  # 查询余额
        price = int(buyNum) * float(stockPrice) # 需要多少钱
        if balance < price:
            return dueR(r, -2)
        balance -= price
        if competitor.updateBalance(mydb, matchID, user, balance) == False:  # 更新余额
            return dueR(r, -103)
        # 加入订单
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO order_db (order_type, match_id, wxid, creat_time, order_status, stock_id, order_num, price) VALUES ( %s,%s, %s, %s, %s, %s, %s, %s)",
            (1, matchID, user, getTimeStamp(), 1, stockID, buyNum, stockPrice))
        mydb.commit()
        if mycursor.rowcount == 0:
            return dueR(r, -103)
        return dueR(r, 1)
    except:
        return dueR(r, -102)
   


def sellOrder(mydb, token, matchID, stockID, sellNum, stockPrice):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：token错误、 -2：库存不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    try:
        ownNum = competitor.getStockNum(mydb, matchID, user, stockID)  # 查询余额
        sellNum = int(sellNum)
        if ownNum < sellNum:
            return dueR(r, -2)
        ownNum -= sellNum
        if competitor.updateStockNum(mydb, matchID, user, stockID, ownNum) == False:  # 更新余额
            return dueR(r, -103)
        # 加入订单
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO order_db (order_type, match_id, wxid, creat_time, order_status, stock_id, order_num, price) VALUES ( %s,%s, %s, %s, %s, %s, %s, %s)",
            (2, matchID, user, getTimeStamp(), 1, stockID, sellNum, stockPrice))
        mydb.commit()
        if mycursor.rowcount == 0:
            return dueR(r, -103)
        return dueR(r, 1)
    except:
       return dueR(r, -102)

def rollBackOrder(mydb, token, rollBackOrder):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：token错误、 -2：订单id不存在、 -2：订单id已完成或撤回 -101：数据库连接失败、 -102：sql异常、 -102：更新订单失败
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    try:
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT * FROM order_db WHERE wxid=%s AND id=%s AND order_status=1", (user, rollBackOrder))
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -2)
        if myresult[1]>2:
            return dueR(r, -3)
        elif myresult[1]==1: # 撤回买入加钱
            balance = competitor.getBalance(mydb,myresult[8],user) + myresult[6]*myresult[7]
            competitor.updateBalance(mydb,myresult[8],user,balance)
            print('撤回打钱',myresult[8],user,balance)
        elif myresult[1]==2: # 撤回卖出加库存
            stockNum = competitor.getStockNum(mydb,myresult[8],user,myresult[5]) + myresult[6]
            competitor.updateStockNum(mydb,myresult[8],user,myresult[5],stockNum)
            print('撤回加仓',myresult[8],user,stockNum)
        mycursor.execute(
            "UPDATE order_db SET order_status=3  WHERE wxid=%s AND id=%s", (user, rollBackOrder))
        mydb.commit()
        if mycursor.rowcount == 0:
            return dueR(r, -103)
        return dueR(r, 1)
    except:
       return dueR(r, -102)
    return dueR(r, -666)

def getUserInfo(mydb, token):
    r = {
        'value': 0,
        'wxid': ''
    }
    # 1： 正常、 -1：token错误
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    r['wxid'] = user
    r['value'] = 1
    return jsonify(r)


def joinMatch(mydb, token, matchid):
    r = {
        'value': 0
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # get wxid according token
        sql = "SELECT wxid FROM user_db WHERE token = %s"
        val = (token,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        wxid = myresult[0]

        # check match
        sql = "SELECT * FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -4)

        # check wxid - match_id unique
        sql = "SELECT * FROM competitor_db WHERE match_id = %s AND wxid = %s"
        val = (matchid, wxid)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult != None:
            return dueR(r, -3)

        # get init_money from match_db
        sql = "SELECT init_money FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        init_money = myresult[0]

        # add into competitor_db
        sql = "INSERT INTO competitor_db (match_id, wxid, balance) VALUES (%s, %s, %s)"
        val = (matchid, wxid, init_money)
        mycursor.execute(sql, val)
        mydb.commit()

        # # add into storage_db
        # sql = "INSERT INTO storage_db (wxid, match_id, stock_id, own_num, ave_price, lock_num) VALUES (%s, %d, %s, %d, %f, %d)"
        # val = (wxid, matchid, "", 0, 0.0, 0)
        # mycursor.execute(sql, val)
        # mydb.commit()

        return dueR(r, 1)

    except:
        return dueR(r, -102)


def quitMatch(mydb, token, matchid):
    r = {
        'value': 0
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在  -5: 已退出比赛
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # get wxid according token
        sql = "SELECT wxid FROM user_db WHERE token = %s"
        val = (token,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        wxid = myresult[0]

        # check match
        sql = "SELECT * FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -4)

        # delete from competitor_db
        sql = "SELECT * FROM competitor_db WHERE match_id = %s AND wxid = %s"
        val = (matchid, wxid)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -5)

        sql = "DELETE FROM competitor_db WHERE match_id = %s AND wxid = %s"
        val = (matchid, wxid)
        mycursor.execute(sql, val)
        mydb.commit()

        return dueR(r, 1)

    except:
        return dueR(r, -102)


def getMatchInfo(mydb, token, matchid):
    r = {
        'value': 0
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在  -5: 已退出比赛
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()
        # check match
        sql = "SELECT * FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -4)

        r['id'] = myresult[0]
        r['match_name'] = myresult[1]
        r['match_detail'] = myresult[2]
        r['match_rule'] = myresult[3]
        r['start_time'] = myresult[4]
        r['sign_time'] = myresult[5]
        r['end_time'] = myresult[6]
        r['init_money'] = myresult[7]

        #mycursor.close()
        return dueR(r, 1)

    except:
        return dueR(r, -102)


def getMatchList(mydb, token):
    r = {
        'value': 0
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在  -5: 已退出比赛
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # check match
        sql = "SELECT * FROM match_db"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if myresult == []:
            return dueR(r, -4)

        matchlist = []
        for x in myresult:
            tmp = {'id': x[0], 'match_name': x[1]}
            matchlist.append(tmp)

        r['matchlist'] = matchlist

        return dueR(r, 1)

    except:
        return dueR(r, -102)


def getMatchRank(mydb, token, matchid):
    r = {
        'value': 0,
    }

    # 1： 正常、 -1：token错误、 -2：余额不足 -101：数据库连接失败、 -102：sql异常、 -103：sql无效
    # -3: 重复参加比赛  -4: 比赛不存在  -5: 已退出比赛  -6: 暂无参赛人员
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)

    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)

    try:
        mycursor = mydb.cursor()

        # check match
        sql = "SELECT * FROM match_db WHERE id = %s"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult == None:
            return dueR(r, -4)

        # competitor_db sorted by balance
        sql = "SELECT * FROM competitor_db WHERE match_id = %s ORDER BY balance DESC LIMIT 10"
        val = (matchid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if myresult == []:
            return dueR(r, -6)

        ranklist = []
        for x in myresult:
            tmp = {'wxid': x[2], 'balance': x[3]}
            ranklist.append(tmp)

        r['ranklist'] = ranklist

        return dueR(r, 1)
    except:
        return dueR(r, -102)



# 返回用户的基本信息
def getUserInfo1(mydb,token):
    r = {
        'value': 0,
    }
    # 1： 正常、 -1：token错误、 101：数据库链接错误
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    r['wxid'] = user
    r['value'] = 1
    # 从用户的表单中取数据
    mycursor = mydb.cursor()
    sql = "SELECT heading FROM user_db WHERE wxid= %s "
    val = (user,)
    mycursor.execute(sql, val)
    myresult=mycursor.fetchone()
    r['heading'] = myresult[0]

    sql = "SELECT nickName FROM user_db WHERE wxid= %s  "
    val = (user,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    r['nickName'] = myresult[0]

    # 从黑名单表单中判断是否在黑名单
    sql = "SELECT * FROM blacklist_db WHERE wxid= %s  "
    val = (user,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result is None:
        result = 'no'
    else:
        result = 'yes'
    r['inBlackList'] = result
    return dueR(r, 1)



#输出用户参加的所有比赛列表
def getUserInfo2(mydb,token):
    r = {
        'value': 0,
    }
    # 1： 正常、 -1：token错误、 101：数据库链接错误 -2：该用户没有参加任何比赛
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    r['wxid'] = user
    r['value'] = 1
    mycursor = mydb.cursor()
    # 从参赛用户表单中寻找该用户参加的所有比赛
    sql="SELECT match_id FROM competitor_db WHERE wxid= %s "
    val=(user,)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    if result==[]:
        return dueR(r, -2)
    # 所有比赛的id放进一个字典变量里面
    matchidList=[]
    for x in result:
        tmp={'match_id':x[0]}
        matchidList.append(tmp)
    r['joinCompititions']=matchidList
    return dueR(r, 1)


#输出用户关于一个比赛的持仓信息
def getUserInfo3(mydb,token,matchid):
    r = {
        'value': 0,
    }
    # 1： 正常、 -1：token错误、 101：数据库链接错误 -2：没有该用户关于该比赛的持仓信息
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    r['wxid'] = user
    r['value'] = 1
    r['matchid'] = matchid

    # 获得所有持仓信息
    mycursor = mydb.cursor()
    # 从参赛用户表单中寻找该用户参加的所有比赛
    sql = "SELECT * FROM storage_db WHERE wxid= %s AND match_id=%s"
    val = (user,matchid)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    if result==[]:
        return dueR(r, -2)
    storageInfo=[]
    for x in result:
        tmp={'stock_id':x[3],'own_num':x[4],'ave_price':x[5],'lock_num':x[6]}
        storageInfo.append(tmp)
    r['value']=1
    r['stockInfo']=storageInfo
    return dueR(r, 1)


# 用户查询单只股票，返回单只股票信息
def getStockInfo(mydb,token, stockid):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：token错误、 101：数据库链接错误
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    r['value'] = 1
    dm=stock.getStockDM(stockid)
    result=stock.getStockInfo(stockid,dm=dm)

    r['stockInfo'] = result
    return  dueR(r, 1)

#用户查询订单
def getUserOrder(mydb, token,ordertype,startTime,endTime,orderstatus):
    r = {
        'value': 0
    }
    # 1： 正常、 -1：token错误、 101：数据库链接错误
    # mydb = con()
    if mydb == None:
        return dueR(r, -101)
    user = checkTOKEN(token, mydb)
    if user == None:
        return dueR(r, -1)
    r['wxid'] = user
    r['value'] = 1

    mycursor = mydb.cursor()
    sql="SELECT * FROM order_db WHERE wxid= %s AND order_type=%s AND order_status=%s"
    val=(user,ordertype,orderstatus)
    mycursor.execute(sql, val)
    tempList=[]
    result= mycursor.fetchall()
    for x in result:
        tmp={'id':x[0],'order_type':x[1] ,'create_time':x[3],'order_status':x[4],'stock_id':x[5],'order_num':x[6],'price':x[7],'match_id':x[8]}
        tempList.append(tmp)
    #找出符合时间的条目
    finalList=[]

    for x in tempList:
       if x['create_time']>startTime and x['create_time']<endTime:
            finalList.append(x)
    

    #转换成中文
    trans_type={
        1:'买入',
        2:'卖出'
    }
    for x in finalList:
        key=x['order_type']
        x['order_type']=trans_type[key]

    trans_status={
        1:'进行中',
        2:'完成',
        3:'撤回'
    }

    for x in finalList:
        key=x['order_status']
        x['order_status']=trans_status[key]

    r['orderInfo']=finalList

    return dueR(r, 1)
