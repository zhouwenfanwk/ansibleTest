import pymysql
from pymongo import MongoClient

sql = ''
host_sql = ''
user = ''
passwd = ''

host_mon = ''
db_name = ''
col_name =''

def get_mysql(sql, host, user, passwd):
    conn = pymysql.connect(host=host_sql, user=user, passwd=passwd)
    # 获取游标
    cursor = conn.cursor()
    # 执行
    cursor.execute(sql)
    resTuple = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()

    return resTuple

def get_mongo(host, db_name, col_name):

    client = MongoClient(host)
    db = client[db_name]
    col = db[col_name]
    data_set = col.find({},{})

    return data_set

def data_check(mysql_db, mongo_db):
    pass
