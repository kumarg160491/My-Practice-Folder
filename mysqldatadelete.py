#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:54:13 2020

@author: kumarg
"""

import mysql.connector

def delete(id):
    conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='102531@1')
    
    if conn.is_connected():
        print('Connected to Mysql db')
    cursor=conn.cursor()
    str='delete from emp where id=%d '
    args=(id)
    try:
        cursor.execute(str %args)
        conn.commit()
        print('Emp deleted')
    except:
        conn.rollback()
        
empid=int(input('Enter emp id : '))
delete(empid)
    