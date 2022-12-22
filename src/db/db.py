#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: db.py


from src.config import Config

if Config.database == 'sqlite3':
    import sqlite3 as operator
else:
    import pymysql as operator


class BaseSQL:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, _id: str) -> tuple:
        self.cursor.execute('select * from data where id="%s";' % _id)
        result = self.cursor.fetchone()
        if result is None:
            self.insert(_id)
            return tuple([_id, 0])
        self.update(_id, result[1])
        return result

    def insert(self, _id: str) -> bool:
        self.cursor.execute('insert into data (id, times) values ("%s", 1);' % _id)
        return True

    def update(self, _id: str, times: int) -> bool:
        times += 1
        self.cursor.execute('update data set times=%s where id="%s";' % (times, _id))
        return True

    def query_all(self) -> list:
        self.cursor.execute('select * from data;')
        result = self.cursor.fetchall()
        return result

    def query_image(self, theme: str) -> list:
        self.cursor.execute('select * from %s;' % theme)
        result = self.cursor.fetchall()
        return result


class SQLite(BaseSQL):
    def __init__(self):
        super().__init__()
        if Config.DETA:
            self.conn = operator.connect('/tmp/data.sqlite')
        else:
            self.conn = operator.connect('./src/db/data.sqlite')
        self.cursor = self.conn.cursor()


class MySQL(BaseSQL):
    def __init__(self):
        super().__init__()
        _CONFIG = Config.database.split('@')
        user = _CONFIG[0].split(':')[0]
        pwd = _CONFIG[0].split(':')[1]
        host = _CONFIG[1].split(':')[0]
        port = int(_CONFIG[1].split(':')[1].split('/')[0])
        db = _CONFIG[1].split('/')[1]

        self.conn = operator.connect(user=user,
                                     passwd=pwd,
                                     host=host,
                                     port=port,
                                     database=db)
        self.cursor = self.conn.cursor()
