#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:40:32 2020

@author: kumarg
"""

import mysql.connector

conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='102531@1')


if conn.is_connected():
    print('Connected to Mysql db')

cursor=conn.cursor()

try:
    cursor.execute("insert into emp values(3,'gaurav',30000)")
    conn.commit()
    print('Emp added')
except:
    conn.rollback()
    
    
cursor.close()
conn.close()