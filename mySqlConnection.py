#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:50:07 2019

@author: pi
"""

import pymysql
class MySqlConnection:
    def connect(self):    
        db = pymysql.connect("localhost","dark","root","m1" )
        cursor = db.cursor()
        return db,cursor    