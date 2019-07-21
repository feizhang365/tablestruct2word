# -*- encoding: utf-8 -*- #
__author__ = 'FeiZhang 81597228@qq.com'
__date__ = '2019-07-18'

import pymysql


class MyConn:
    """
    Mysql connection
    """
    def __init__(self, config):
        self.conn = pymysql.connect(host=config['host'],
                                    port=config['port'],
                                    user=config['user'],
                                    password=config['password'],
                                    db=config['db'])

    def close(self):
        self.conn.close()