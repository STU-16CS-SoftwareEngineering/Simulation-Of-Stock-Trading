#! usr/bin/python3
# -*- coding: utf-8 -*-


import mysql.connector


class SQLink:
    db = None
    # db_host = '106.14.197.175'
    db_host = 'localhost'
    db_user = 'root'
    db_passed = 'root'
    db_name = "market"

    """初始化，返回连接id"""
    def __init__(self):
        self.db = mysql.connector.connect(host=self.db_host, user=self.db_user, passwd=self.db_passed, database=self.db_name)

    """返回db对象"""
    def get_db(self):
        return self.db

    """关闭连接"""
    def turn_off(self):
        pass
