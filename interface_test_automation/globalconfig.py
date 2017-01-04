#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

from getdb import GetDB
from confighttp import ConfigHttp
from configrunmode import ConfigRunMode

class Global:
    def __init__(self):
        # 读取并配置接口服务器IP，端口等信息
        self.http = ConfigHttp('../http_conf.ini')

        # 读取并配置数据库服务器IP，端口等信息
        self.db1 = GetDB('../db_config.ini', 'DATABASE1')
        self.db2 = GetDB('../db_config.ini', 'DATABASE2')

        # 读取运行模式配置
        self.run_mode_config = ConfigRunMode('../run_case_config.ini')

    def get_http(self):
        return self.http

    # 返回测试数据库连接
    def get_db1_conn(self):
        return self.db1.get_conn()

    # 返回应用数据库连接
    def get_db2_conn(self):
        return self.db2.get_conn()

    # 获取运行模式配置
    def get_run_mode(self):
        return self.run_mode_config.get_run_mode()

    # 获取需要单独运行的用例列表
    def get_run_case_list(self):
        return self.run_mode_config.get_case_list()

    # 释放资源
    def clear(self):
        # 关闭数据库连接
        self.db1.get_conn().close()
        self.db2.get_conn().close()