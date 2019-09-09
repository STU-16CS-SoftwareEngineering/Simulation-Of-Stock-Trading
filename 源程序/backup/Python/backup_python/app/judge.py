#! usr/bin/python3
# -*- coding: utf-8 -*-
import time, threading
import mysql.connector
from app import stock, ssql
from app import competitor
# 说明https://blog.csdn.net/simon803/article/details/7784682

count = 0
# mydb = None

def checkOrder():
    # global mydb
    mydbcon = ssql.SQLink()
    mydb = mydbcon.get_db()
    global count
    localtime = time.localtime()  # time.struct_time(tm_year=2018, tm_mon=12, tm_mday=18, tm_hour=20, tm_min=17, tm_sec=25, tm_wday=1, tm_yday=352, tm_isdst=0)
    nowHour = localtime.tm_hour
    nowMin = localtime.tm_min
    #nowHour = 10
    #nowMin = 12
    if nowHour>0 and nowHour<8: # 取消冻结
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM storage_db WHERE lock_num>0")
        myresult = mycursor.fetchall()
        for x in myresult:
            ownNum = x[4] + x[6]
            mycursor.execute("UPDATE storage_db SET own_num=%s,lock_num=0 WHERE id=%s",(ownNum, x[0]))
            print('取消冻结', 'id:', x[1] ,ownNum)
        mydb.commit()
    elif (nowHour>=9 and nowHour<12) or (nowHour>=13 and nowHour<=15): # 开市了[9,12)\[13.15]
        if nowHour==9 and nowMin<30: # < 9:30
            return
        if nowHour==11 and nowMin>30: # > 11:30
            return
        sti = stock.getStockInfo('000001', dm='sh')
        if sti[30] != time.strftime("%Y-%m-%d", time.localtime()):
            return
        count += 1
        print('交易撮合心跳<', count, '>', time.time())
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM order_db WHERE order_status=1")
        myresult = mycursor.fetchall()
        #print(myresult)
        for x in myresult:
            mycursor.execute("UPDATE order_db SET order_status=2 WHERE id=%s",(x[0],)) # 完成委托
            mydb.commit()
            if x[1]==1:#买入
                sti = stock.getStockInfo(x[5])
                if int(sti[20]) == 0: # 涨停板
                    continue
                if float(sti[4]) > x[7]: # 价格高于买入价
                    continue
                mycursor.execute("SELECT * FROM storage_db WHERE match_id=%s AND stock_id=%s AND wxid=%s",(x[8], x[5], x[2])) # 读库存信息
                myresult = mycursor.fetchone()
                if myresult == None:
                    mycursor.execute("INSERT INTO storage_db (wxid,match_id,stock_id,own_num,ave_price,lock_num) VALUES (%s,%s,%s,%s,%s,%s)",(x[2],x[8],x[5],0,x[7],x[6])) 
                    print('增加仓库',x[2],x[5],x[7],x[6])
                else:
                    avePrice = ((myresult[4]+myresult[6])*myresult[5]+x[7]*x[6])/(myresult[4]+myresult[6]+x[6])
                    lockNum = myresult[6]+x[6]
                    mycursor.execute("UPDATE storage_db SET ave_price=%s,lock_num=%s WHERE wxid=%s AND match_id=%s AND stock_id=%s",(avePrice,lockNum,x[2],x[8],x[5]))
                    print('更新仓库',x[2],x[5],avePrice,lockNum)
                mydb.commit()

            elif x[1]==2:#卖出
                sti = stock.getStockInfo(x[5])
                if int(sti[10]) == 0: # 跌停板
                    continue
                if float(sti[4]) < x[7]: # 价格低于卖出价
                    continue
                balance = competitor.getBalance(mydb, x[8], x[2])
                balance += x[7]*x[6]
                competitor.updateBalance(mydb, x[8], x[2], balance)
                print('卖出打钱',x[2],x[5],balance)


def judgeloop(): # 判官
    while True:
        checkOrder()
        time.sleep(30)


def star_judeg(): # 开始线程
    # global mydb
    # mydb = dbcon
    t = threading.Thread(target=judgeloop, name='Judge')
    t.start()

#checkOrder()
#print(stock.getStockInfo('000001'))
