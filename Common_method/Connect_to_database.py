# -*- coding:utf-8 -*-
# @Time:  2020/1/6 17:20
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  Connect_to_database.py
# @Software:  PyCharm
from loguru import logger
import time
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
logger.add("E:\\honggetest\\log\\"+today+".log",encoding='utf8',retention='30 days')
from Common_method import read_config
configname = 'Mysql'
config= read_config.ReadConfig(configname)


def Connect(sql,size):
    import warnings
    warnings.simplefilter('ignore',Warning)
    import pymysql as mysqldb
    conn=mysqldb.connect(host=config['host'],port=int(config['port']),user=config['user'],
                         passwd=config['passwd'],db=config['db'],charset=config['charset'])
    logger.debug('连接mysql数据库')
    cursor=conn.cursor()
    logger.debug('创建游标')
    try:
        cursor.execute(sql)
        conn.commit()
        result=cursor.fetchmany(size)
        logger.debug("生成元组" + str(result) + "")
        return result
    except:
        logger.error('有异常出现，请检查sql语句')
        conn.rollback()
    finally:
        conn.close()
        logger.info('关闭数据库连接')


if __name__=='__main__':
    sql='select * from apple'
    size=2
    Connect(sql, size)



