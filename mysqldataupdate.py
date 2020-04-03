#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:33:05 2020

@author: kumarg
"""

import mysql.connector

def update(id):
    conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='102531@1')
    
    if conn.is_connected():
        print('Connected to Mysql db')
    cursor=conn.cursor()
    str="update emp SET id= 3 where id='%d'"
    args=(id)
    try:
        cursor.execute(str % args)
        conn.commit()
        print('Emp updated')
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()   

empid=int(input('Enter emp id : '))
update(empid)
    