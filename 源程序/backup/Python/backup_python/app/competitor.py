#! usr/bin/python3
# -*- coding: utf-8 -*-


import mysql.connector


def getBalance(mydb, matchID, user):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT balance FROM competitor_db WHERE match_id = %s AND wxid = %s", (matchID, user))
    myresult = mycursor.fetchone()
    if myresult == None:
        return 0
    return myresult[0]


def updateBalance(mydb, matchID, user, balance):
    mycursor = mydb.cursor()
    mycursor.execute(
        "UPDATE competitor_db SET balance=%s WHERE match_id = %s AND wxid=%s", (balance, matchID, user))
    mydb.commit()
    if mycursor.rowcount == 0:
        return False
    else:
        return True


def getStockNum(mydb, matchID, user, stockID):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT own_num FROM storage_db WHERE match_id = %s AND wxid = %s AND stock_id = %s", (matchID, user, stockID))
    myresult = mycursor.fetchone()
    if myresult == None:
        return 0
    return int(myresult[0])


def updateStockNum(mydb, matchID, user, stockID, ownNum):
    mycursor = mydb.cursor()
    mycursor.execute(
        "UPDATE storage_db SET own_num=%s WHERE match_id = %s AND wxid = %s AND stock_id = %s", (ownNum, matchID, user, stockID))
    mydb.commit()
    if mycursor.rowcount == 0:
        return False
    else:
        return True
