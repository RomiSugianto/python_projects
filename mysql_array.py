import pymysql
from pymysql import Error
con = pymysql.connect(db="absen", user="root", passwd="",host="localhost",port=3306,autocommit=True)

tempId=input('input id : ')
cur = con.cursor()
sql_select_query = """select nama from siswa where card = %s"""
cur.execute(sql_select_query, (tempId, ))
rows_count = cur.execute(sql_select_query, (tempId, ))
card = cur.fetchall()
tuple(card)
if rows_count > 0:
    print(card)
else:
    print('unrecognized')