#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

import unittest
from test_interface_case import TestInterfaceCase
from datastruct import DataStruct

global test_data
test_data = DataStruct()

class  RunCase:
    '''运行测试用例'''

    def __init__(self):
        pass

    # 运行测试用例函数
    def run_case(self, runner, run_mode, run_case_list, db1_conn, db2_conn, http):
        global test_data
        if 1 == run_mode:  # 运行全部用例
            db1_cursor = db1_conn.cursor()
            # 获取用例个数
            db1_cursor.execute('SELECT count(case_id)  FROM test_data')
            test_case_num = db1_cursor.fetchone()[0]
            db1_cursor.close()

            # 循环执行测试用例
            for case_id in range(1, test_case_num+1):
                 db1_cursor = db1_conn.cursor()
                 db2_cursor = db2_conn.cursor()
                 db1_cursor.execute('SELECT http_method, request_name, request_url, request_param, test_method, test_desc '
                                      'FROM test_data WHERE case_id = %s',(case_id,))
                 # 记录数据
                 tmp_result = db1_cursor.fetchone()
                 test_data.case_id = case_id
                 test_data.http_method = tmp_result[0]
                 test_data.request_name = tmp_result[1]
                 test_data.request_url = tmp_result[2]
                 test_data.request_param = tmp_result[3]
                 test_data.test_method = tmp_result[4]
                 test_data.test_desc = tmp_result[5]
                 test_data.result = ''
                 test_data.reason = ''
                 try:
                     query = ('INSERT INTO test_result(case_id, http_method, request_name, request_url,'
                              'request_param, test_method, test_desc, result, reason) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)')

                     data = (test_data.case_id,test_data.http_method,test_data.request_name, test_data.request_url,
                             test_data.request_param, test_data.test_method, test_data.test_desc,
                             test_data.result, test_data.reason)
                     db1_cursor.execute(query, data)
                     db1_cursor.execute('commit')
                 except Exception as e:
                     # 回滚
                     print('%s' % e)
                     db1_cursor.execute('rollback')

                 test_suite = unittest.TestSuite()
                 test_suite.addTest(TestInterfaceCase(test_data.test_method, test_data, http, db1_cursor, db2_cursor))
                 runner.run(test_suite)
                 db1_cursor.close()
                 db2_cursor.close()
        else:   # 运行部分用例
            # 循环执行测试用例
            for case_id in run_case_list:
                 db1_cursor = db1_conn.cursor()
                 db2_cursor = db2_conn.cursor()
                 db1_cursor.execute('SELECT http_method, request_name, request_url, request_param, test_method, test_desc '
                                      'FROM test_data WHERE case_id = %s',(case_id,))
                 # 记录数据
                 tmp_result = db1_cursor.fetchone()
                 test_data.case_id = case_id
                 test_data.http_method = tmp_result[0]
                 test_data.request_name = tmp_result[1]
                 test_data.request_url = tmp_result[2]
                 test_data.request_param = tmp_result[3]
                 test_data.test_method = tmp_result[4]
                 test_data.test_desc = tmp_result[5]
                 test_data.result = ''
                 test_data.reason = ''

                 try:
                     query = ('INSERT INTO test_result(case_id, http_method, request_name, request_url,'
                              'request_param, test_method, test_desc, result, reason) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)')

                     data = (test_data.case_id,test_data.http_method,test_data.request_name, test_data.request_url,
                             test_data.request_param, test_data.test_method, test_data.test_desc,
                             test_data.result, test_data.reason)
                     db1_cursor.execute(query, data)
                     db1_cursor.execute('commit')
                 except Exception as e:
                     # 回滚
                     print('%s' % e)
                     db1_cursor.execute('rollback')
                 test_suite = unittest.TestSuite()
                 test_suite.addTest(TestInterfaceCase(test_data.test_method, test_data, http, db1_cursor, db2_cursor))
                 runner.run(test_suite)
                 db1_cursor.close()