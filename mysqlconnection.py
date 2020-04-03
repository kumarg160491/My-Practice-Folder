# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='102531@1')


if conn.is_connected():
    print('Connected to Mysql db')

cursor=conn.cursor()
cursor.execute('select * from emp')
rows=cursor.fetchall()
print('Total number of records',cursor.rowcount)

for row in rows:
    print(row)
    
cursor.close()   
conn.close()
    
