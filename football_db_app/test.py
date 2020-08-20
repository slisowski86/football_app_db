# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 06:47:26 2020

@author: sliso
"""


import numpy as np
import pandas as pd
sql_dict={#'Narodowość':'Poland',
          #'Klub':'Legia',
          'Rozegrane_mecze':'22',
          'Rozegrane_minuty':'21'}





column_dict={ 'Narodowość':'nationality_name',
             'Klub':'club_name',
             'Wiek':'age',
             'Rozegrane_mecze':'appearances',
             'Rozegrane_minuty':'mins',
             'Bramki':'goals',
             'Asysty':'assists',
             'Zółte_kartki':'yel',
             'Czerwone_kartki':'red',
             'Strzały_na_mecz':'shots_per_game',
             'Celność_podań(%)':'pass_score',
             'Wygrane_główki':'aerialswon',
             'Piłkarz_meczu': 'man_of_the_match',
             'Rating':'rating',
             'Idealna_defensywa' : 'perfdef',
             'Idealny_atak':'perfattack',
             'Idealne_ustawienie': 'perfposs',
             'Total':'total'}
data_to_report=['Wiek', 'Rozegrane mecze', 'Rozegrane minuty', 'Bramki',
                'Asysty', 'Żółte kartki', 'Czerowne kartki', 'Strzały na mecz', 'Celność podań(%)',
                'Wygrane główki', 'Piłkarz meczu', 'Rating', 'Idealna defensywa', 'Idealny atak', 'Idealne ustawienie',
                'Total']






sql_schema_dict={'players':['id', 'name','age','nationality_id','club_id'],
          'nations':['id', 'nationality_name'],
          'clubs':['id', 'club_name'],
          'player_score':['player_id','appearances','mins', 'goals',
                          'assists','yel','red','shots_per_game','pass_score',
                          'aerialswon','man_of_the_match','rating'],
          'player_stats':['player_id','perfdef','perfattack','perfposs','total']}

filters_df_sql_test=pd.DataFrame([sql_dict])
filters_df_sql_test.columns=filters_df_sql_test.columns.to_series().map(column_dict)
    
sql_query_dict_test=filters_df_sql_test.to_dict()

select='SELECT name, '
fromT=' FROM players, '
where=' WHERE '
whereStats=' WHERE players.id=id'
conditionDict={'nationality_name':'nations.id=players.nationality_id',
               'club_name':'clubs.id=players.club_id'}

query=''
for k in sql_schema_dict:
    for v in sql_schema_dict[k]:
        
        for key in sql_query_dict_test.keys():
            if key==v:
                if key not in conditionDict.keys():
                    select=select+v+', '
                    fromT=fromT+k+', '
                    where=where+conditionDict[v]+' AND '
                    

query=select+' '+fromT+' '+where
print(query)