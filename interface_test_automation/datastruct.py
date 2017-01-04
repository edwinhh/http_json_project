#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

# 定义结构体
class DataStruct:
    '''于接收读取的测试数据,记录要写入测试报告的数据'''
    def __init__(self):
        self.case_id = 0       #用例ID
        self.http_method = ''  #接口http方法
        self.request_name = '' #接口ming
        self.request_url = ''  #接口请求url
        self.request_param = ''#请求参数
        self.test_method = ''  #测试方法
        self.test_desc = ''    #测试(用力)描述
        self.result = ''       #测试结果
        self.reason = ''       #失败原因



