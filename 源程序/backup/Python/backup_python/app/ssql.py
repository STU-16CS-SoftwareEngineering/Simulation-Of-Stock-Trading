#! usr/bin/python3
# -*- coding: utf-8 -*-


import mysql.connector


class SQLink:
    db = None
    db_host = '119.23.36.18'
    db_user = 'test_market'
    db_passed = 'GrZFWfSh4GTMRBFy'
    db_name = "test_market"

    """初始化，返回连接id"""
    def __init__(self):
        self.db = mysql.connector.connect(host=self.db_host, user=self.db_user, passwd=self.db_passed, database=self.db_name)

    """返回db对象"""
    def get_db(self):
        return self.db

    """关闭连接"""
    def turn_off(self):
        pass
