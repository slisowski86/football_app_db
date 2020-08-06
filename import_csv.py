# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:56:28 2020

@author: sliso
"""

import cx_Oracle
import csv

hostname='dbserver.mif.pg.gda.pl'
port=1521
service='ORACLEMIF'

dsn_tns = cx_Oracle.makedsn('dbserver.mif.pg.gda.pl', '1521', service_name='ORACLEMIF') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'SLISOW_P', password='g2D8M', dsn=dsn_tns)

with open("sql_data/players.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    for lines in csv_reader:
       conn.execute(
            "insert into new_location (LOCATION_ID, STREET_ADDRESS, POSTAL_CODE, CITY, STATE_PROVINCE, COUNTRY_ID) values (:1, :2, :3, :4, :5, :6)",
            (lines[0], lines[1], lines[2], lines[3], lines[4], lines[5]))

conn.close()
conn.commit()
conn.close()