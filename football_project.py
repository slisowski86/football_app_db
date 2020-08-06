# -*- coding: utf-8 -*-
"""
Created on Fri May 15 05:45:12 2020

@author: sliso
"""

import pandas as pd


df_players=pd.read_csv("D:/Bazy danych/Projekt/raw_data/Players.csv", sep=",", encoding ='latin-1')
df_players_score=pd.read_csv("D:/Bazy danych/Projekt/raw_data/Players_Score.csv", sep="," , encoding ='latin-1')
df_players_stats=pd.read_csv("D:/Bazy danych/Projekt/raw_data/Players_Stats.csv", sep=",", encoding ='latin-1')

                                                                                                

# W ramkach player_score i player_stats zostawiamy tych samych zawodników


uniq=df_players['player'].nunique()
df_players=pd.DataFrame(df_players[['player', 'nationality']])

player_dict=dict(zip(df_players['player'], df_players['nationality']))


players_list=set(df_players_score.player).intersection(set(df_players_stats.player))

df_players_score_all=df_players_score[df_players_score['player'].isin(players_list)]

df_players_score_all=df_players_score_all.drop_duplicates(['player']).reset_index(drop=True)

df_players_stats_all=df_players_stats[df_players_stats['player'].isin(players_list)]

df_players_stats_all=df_players_stats_all.drop_duplicates(['player']).reset_index(drop=True)

df_players_stats_all.to_csv('players_stats_all.csv')
df_players_score_all.to_csv('players_score_all.csv')