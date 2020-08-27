# -*- coding: utf-8 -*-
import pandas as pd

#wczytujemy ramki danych

players_stats_df=pd.read_csv("D:/Bazy_danych/clear_data/players_stats_all.csv")
players_score_df=pd.read_csv("D:/Bazy_danych/clear_data/players_score_all.csv")

players_stats_df.drop(players_stats_df.filter(regex="Unname"),axis=1, inplace=True)
players_score_df.drop(players_score_df.filter(regex="Unname"),axis=1, inplace=True)

players=pd.read_csv("D:/Bazy_danych/raw_data/Players.csv", encoding = "ISO-8859-1")

#tworzymy zgodne ramki danych, aby byli tacy sami zawodnicy w każdej ramce, 


players_nat_list=set(players_stats_df.player).intersection(players.player)


players=players[players['player'].isin(players_nat_list)]

nationality_dict = dict(zip(players['player'], players['nationality']))

# sprawdzamy czy zawodnik jest w ramce z narodowoscią

players_score_df=players_score_df[players_score_df['player'].isin(players_nat_list)]
players_stats_df=players_stats_df[players_stats_df['player'].isin(players_nat_list)]

#wyrzucamy kolumnę rank 

players_stats_df.drop('Rank',axis=1, inplace=True)
players_score_df.drop('Rank',axis=1, inplace=True)

# w ramce danych players_stats_df odzielamy klub od pozycji zawodnika

players_stats_df['position']= players_stats_df.club.str.split(' - ').str[0]
players_stats_df['team']= players_stats_df.club.str.split(' - ').str[1]
players_stats_df['club']= players_stats_df['team']
players_stats_df.drop('team',axis=1, inplace=True)


# Tworzymy tabelę zawodnik zawierającą dane id zawodnika, imię, nazwisko, wiek




player_dict={"id": range(1, 362),
            "name" : players_score_df['player'],
             "age": players_score_df['age'],
             "nationality": players_score_df['player'].map(lambda x: nationality_dict[x]),
             "club":players_score_df['club']}

player=pd.DataFrame(player_dict)
player.reset_index(inplace=True, drop=True)
#tworzymy tabelę club

club_list=list(players_score_df.club.unique())
club_key=list(range(1, len(club_list)+1))
clubs_dict={"id":club_key,
            "club_name":club_list}

clubs=pd.DataFrame(clubs_dict)

#tworzymy tabelę nationality

nat_list=list(player.nationality.unique())
nat_key=list(range(1, len(nat_list)+1))
nat_dict={"id":nat_key,
            "nationality_name":nat_list}

nations=pd.DataFrame(nat_dict)
                                





#kodujemy nationality w tabeli player jako nationality id

nat_map=dict(zip(nat_list,nat_key))
player['nationality']=player['nationality'].map(lambda x: nat_map[x])
player.rename(columns={'nationality':'nationality_id'}, inplace=True)


#kodujemy nationality w tabeli club jako club id

club_map=dict(zip(club_list,club_key))
player['club']=player['club'].map(lambda x: club_map[x])
player.rename(columns={'club':'club_id'}, inplace=True)


#Tworzymy tabelę player_stats



player_stats=players_stats_df[['player','playedgames','playedmins','perfdef','perfattack','perfposs','total']].copy()

#kodujemy player jako player_id

player_map=dict(zip(player.name, player.id))

player_stats['player']=player_stats['player'].map(lambda x: player_map[x])
player_stats.rename(columns={'player':'player_id'}, inplace=True)

#tworzymy tabelę player_score

player_score=players_score_df.drop(['club','age'], axis=1)

#kodujemy player jako player_id

player_score['player']=player_score['player'].map(lambda x: player_map[x])
player_score.rename(columns={'player':'player_id'}, inplace=True)

# z kolumny Apps usuwamy liczby w nawiasach

player_score['Appear']=player_score['Apps'].str.split('(',1).str[0]
player_score['Apps']=player_score['Appear']
player_score.drop('Appear', axis=1, inplace=True)

# w tabeli player score zastępujemy "-" na 0
player_score=player_score.replace('-',0)




player_stats['total'] = player_stats.total.str.replace(',', '.')
player_stats['perfattack'] = player_stats.perfattack.str.replace(',', '.')

player_stats['total']=player_stats['total'].astype(float)
player_stats['perfattack']=player_stats['perfattack'].astype(float)
player_stats['perfdef']=player_stats['perfdef'].astype(float)


for col in ['SpG', 'PS', 'AerialsWon', 'Rating']:
    player_score[col]=player_score[col].astype(float)

for col in ['Apps', 'Goals', 'Assists', 'Yel', 'Red', 'MotM']:
    player_score[col]=player_score[col].astype(int)
    
print(player_stats.info())



player.to_csv('sql_data/player.csv', index=False)
nations.to_csv('sql_data/nations.csv', index=False)
clubs.to_csv('sql_data/clubs.csv', index=False)
player_score.to_csv('sql_data/player_score.csv', index=False)
player_stats.to_csv('sql_data/player_stats.csv', index=False)




