#! usr/bin/python3
# -*- coding: utf-8 -*-


from app import app
from flask import render_template
from flask import request
from app import getaction
from app import ssql

from app import judge

judge.star_judeg()


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def action_index():
    user = {'username': 'visitor'}
    posts = [
        {
            'author': {'username': 'You'},
            'body': 'This page was built on 2018/12/10!'
        },
        {
            'author': {'username': 'Yang'},
            'body': 'What\'s more? 17:00'
        }
    ]
    return render_template('index.html', title='STU', user=user, posts=posts)


@app.route('/<ac>', methods=['POST', 'GET'])
def to_do(ac):
    mydbcon = ssql.SQLink()
    mydb = mydbcon.get_db()  # 这个是数据库连接

    if ac == 'top':
        r = getaction.topstock()
        return r
    elif ac == 'userlogin':
        # 登录
        try:
            user = request.form['user']  # wxid
            psw = request.form['psw']    # 密码
        except:
            pass
        else:
            r = getaction.login(mydb, user, psw)
            return r

    elif ac == 'regist':
        # 注册
        try:
            user = request.form['user']  # weid
            psw = request.form['psw']    # 密码
            heading = request.form['heading']     # 头像
            nickName = request.form['nickname']   # 昵称
        except:
            pass
        else:
            r = getaction.regist(mydb, user, psw, heading, nickName)
            return r

    elif ac == 'getUserInfo':
        # 获取用户个人信息（我的比赛、持仓信息）
        try:
            token = request.form['token']  # token
        except:
            pass
        else:
            r = getaction.getUserInfo(mydb, token)
            return r

    elif ac == 'buy':
        # 买入股票
        try:
            token = request.form['token']           # token
            matchID = request.form['matchid']       # 比赛的id
            stockID = request.form['stockid']       # 股票id
            stockNumber = request.form['stocknum']  # 股票数量
            stockPrice = request.form['price']      # 买入价格
        except:
            pass
        else:
            r = getaction.buyOrder(mydb, token, matchID=matchID, stockID=stockID, buyNum=stockNumber, stockPrice=stockPrice)
            return r

    elif ac == 'sell':
        # 卖出股票
        try:
            token = request.form['token']           # token
            matchID = request.form['matchid']       # 比赛的id
            stockID = request.form['stockid']       # 股票id
            stockNumber = request.form['stocknum']  # 股票数量
            stockPrice = request.form['price']      # 卖出价格
        except:
            pass
        else:
            r = getaction.sellOrder(mydb, token, matchID=matchID, stockID=stockID, sellNum=stockNumber, stockPrice=stockPrice)
            return r

    elif ac == 'rollBackOrder':
        #撤销订单
        try:
            token = request.form['token']# token
            orderID = request.form['orderid']# 订单的id
        except:
            pass
        else:
            r = getaction.rollBackOrder(mydb, token,orderID)
            return r
        return r

    elif ac == 'joinMatch':
        # 报名比赛（）
        try:
            token = request.form['token']           # token
            matchID = int(request.form['matchid'])  # 比赛的id
        except:
            pass
        else:
            r = getaction.joinMatch(mydb, token, matchID)
            return r

    elif ac == 'quitMatch':
        # 退出比赛（）
        try:
            token = request.form['token']           # token
            matchID = int(request.form['matchid'])  # 比赛的id
        except:
            pass
        else:
            r = getaction.quitMatch(mydb, token, matchID)
            return r

    elif ac == 'getMatchInfo':
        # 获取比赛信息
        try:
            token = request.form['token']           # token
            matchID = int(request.form['matchid'])  # 比赛的id
        except:
            pass
        else:
            r = getaction.getMatchInfo(mydb, token, matchID)
            return r

    elif ac == 'getMatchRank':
        # 获取比赛前十名
        try:
            token = request.form['token']           # token
            matchID = int(request.form['matchid'])  # 比赛的id
        except:
            pass
        else:
            r = getaction.getMatchRank(mydb, token, matchID)
            return r

    elif ac == 'getMatchList':
        # 获取比赛列表
        try:
            token = request.form['token']           # token
        except:
            pass
        else:
            r = getaction.getMatchList(mydb, token)
            return r

    elif ac == 'getUserInfo1':
        # 获取用户基本信息
        try:
            token = request.form['token']           # token
        except:
            pass
        else:
            r = getaction.getUserInfo1(mydb, token)
            return r

    elif ac == 'getUserInfo2':
        # 获取用户参加比赛列表
        try:
            token = request.form['token']           # token
        except:
            pass
        else:
            r = getaction.getUserInfo2(mydb, token)
            return r

    elif ac == 'getUserInfo3':
        # 获取用户参加比赛列表
        try:
            token = request.form['token']           # token
            matchID = int(request.form['matchid'])  # 比赛的id
        except:
            pass
        else:
            r = getaction.getUserInfo3(mydb, token,matchID)
            return r

    elif ac == 'getStockInfo':
         # 获取股票信息
        try:
            token = request.form['token']  # token
            stockID = request.form['stockid']  # 股票的id
        except:
            pass
        else:
            r = getaction.getStockInfo(mydb, token,stockID)
            return r

    elif ac == 'getUserOrder':
         # 获取股票信息
        try:
            token = request.form['token']  # token
            ordertype= int(request.form['order_type'])
            orderstatus = int(request.form['order_status'])
            startTime = int(request.form['start'])
            endTime= int(request.form['end'])
        except:
            pass
        else:
            r = getaction.getUserOrder(mydb, token,ordertype,startTime,endTime,orderstatus)
            return r

    elif ac == 'getNews':
         # 获取股票新闻
        page = 0
        try:
            token = request.form['token']  # token
            if "page" in request.form:
                page = int(request.form['page'])
        except:
            pass
        else:
            r = getaction.getStockNews(mydb, token, page)
            return r

    # elif ac == 'getUserOrder':
    #     #查询该用户的所有状态的订单
    #     token = request.form['token']# token
    #     return r

    return '<h3>Bad request.</h3>'
