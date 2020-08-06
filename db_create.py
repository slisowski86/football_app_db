# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:55:06 2020

@author: sliso
"""

import cx_Oracle

hostname='dbserver.mif.pg.gda.pl'
port=1521
service='ORACLEMIF'

dsn_tns = cx_Oracle.makedsn('dbserver.mif.pg.gda.pl', '1521', service_name='ORACLEMIF') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'SLISOW_P', password='g2D8M', dsn=dsn_tns)

cursor = conn.cursor()

for row in cursor.execute("SELECT player.name, player_score.goals  FROM player, player_score WHERE player.id=player_score.player_id AND player_score.goals>20"):
    print(row)
    
#alter table "SLISOW_P"."PLAYER_SCORE" add constraint PLAYER_FK foreign key("PLAYER_ID") references "PLAYER"("PLAYER_ID")
#alter table "SLISOW_P"."PLAYER_STATS" add constraint  primary key("PLAYER_ID") 
#alter table "SLISOW_P"."PLAYER_STATS" add constraint PLAYER_ID primary key("PLAYER_ID") 
#alter table "SLISOW_P"."PLAYER_STATS" add constraint PLAYER_STATS_FK foreign key("PLAYER_ID") references "PLAYER"("ID")
#alter table "SLISOW_P"."PLAYER" add constraint NATIONS_FK foreign key("NATIONALITY_ID") references "NATIONS"("ID")
    
conn.close()