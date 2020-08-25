import cx_Oracle
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output, State, MATCH, ALL
import cx_Oracle
import numpy as np
import pandas as pd
import dbmanager as dbcon

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app=dash.Dash(__name__, external_stylesheets=external_stylesheets)
#łączenie z bazą danych

server = app.server
conn=dbcon.db_connect()

cursor=conn.cursor()



players=cursor.execute("SELECT name FROM players ").fetchall()
nationality=cursor.execute("SELECT nationality_name FROM nations").fetchall()
clubs=cursor.execute("SELECT club_name FROM clubs").fetchall()
club_unique=np.unique(clubs)
nationality_unique=np.unique(nationality)

sql_dict={}





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
data_to_report=['Wiek', 'Rozegrane_mecze', 'Rozegrane_minuty', 'Bramki',
                'Asysty', 'Żółte_kartki', 'Czerowne_kartki', 'Strzały_na_mecz', 'Celność_podań(%)',
                'Wygrane_główki', 'Piłkarz_meczu', 'Rating', 'Idealna_defensywa', 'Idealny_atak', 'Idealne_ustawienie',
                'Total']



club_nat_dict={'Narodowość': nationality_unique,
               'Klub': club_unique}


sql_schema_dict={'players':['id', 'name','age','nationality_id','club_id'],
          'nations':['id', 'nationality_name'],
          'clubs':['id', 'club_name'],
          'player_score':['player_id','appearances','mins', 'goals',
                          'assists','yel','red','shots_per_game','pass_score',
                          'aerialswon','man_of_the_match','rating'],
          'player_stats':['player_id','perfdef','perfattack','perfposs','total']}
app.layout = html.Div(children=[
    html.H2(children="Aplikacja Football Score"),
    html.Datalist(
    id='player_suggested',
    children=[html.Option(value=word) for word in players]),

    dcc.Input(id='input_1',
    type='text',
    list='player_suggested',
    value='',
    placeholder='Wpisz imię zawodnika...'),
    html.Button('Szukaj',id='search', n_clicks=0),

    html.Div(id='my_output', style={'display':'none'}),
    html.Table(id='table'),
    html.H3(children="Wybierz dane do raportu"),
    html.H4(children="Narodowość"),
    dcc.Dropdown(id="nations_dd",
                 options=[
                     {'label': i, 'value': i} for i in nationality_unique
                 ],


                 ),
   
    html.Button('Wstaw',id='nations_dd_button', n_clicks=0),
    html.Div(id='nations_out'),
    html.H4(children="Klub"),
    dcc.Dropdown(id="clubs_dd",
                 options=[
                     {'label': i, 'value': i} for i in club_unique
                 ],


                 ),
    html.Button('Wstaw',id='clubs_dd_button', n_clicks=0),
    html.Div(id='clubs_out'),
    html.H4(children="Statystyki"),
    dcc.Dropdown(id="stats_dd",
                 options=[
                     {'label': i, 'value': i} for i in data_to_report
                 ],


                 ),
    html.Button('Wstaw',id='stats_dd_button', n_clicks=0),
    html.Div(id='stats_container'),
    html.Button('Pokaż filtry',id='show_filters', n_clicks=0),
    html.Div(id='filter_table'),
    html.Div(id='stats_table'),
    html.Div(id='sql_table')
    
   

])






@app.callback(Output(component_id='table',component_property='children' ),
              [Input(component_id='search', component_property='n_clicks')],
              [State(component_id='input_1', component_property='value')])


def update_table(n_clicks, value):



    x=value

    name = {'player': x}


    db_execute = cursor.execute("SELECT name,age, nations.nationality_name, clubs.club_name, player_score.* FROM players, nations, clubs, player_score WHERE players.name = :player AND players.nationality_id=nations.id AND players.club_id=clubs.id AND player_score.player_id=players.id",name).fetchall()
    query_result = [dict(line) for line in
                        [zip([column[0] for column in cursor.description], row) for row in db_execute]]
    db_df = pd.DataFrame(query_result)


    data = db_df.to_dict('rows')
    columns = [{"name": i, "id": i, } for i in (db_df.columns)]

    if n_clicks>0:
        return dt.DataTable( data=data, columns=columns)



@app.callback(Output(component_id='nations_out', component_property='children'),
              [Input(component_id='nations_dd_button', component_property='n_clicks')],
              [State(component_id='nations_dd', component_property='value')])


def input_nationality(n_clicks, value):
    if n_clicks>0:
        sql_dict['Narodowość']=str(value)
        return "Wybrana narodowosć: "+ value
    
@app.callback(Output(component_id='clubs_out', component_property='children'),
              [Input(component_id='clubs_dd_button', component_property='n_clicks')],
              [State(component_id='clubs_dd', component_property='value')])


def input_nationality(n_clicks, value):
    if n_clicks>0:
        sql_dict['Klub']=str(value)
        return "Wybrany klub: "+ value

@app.callback(Output(component_id='stats_container', component_property='children'),
              [Input(component_id='stats_dd_button', component_property='n_clicks')],
              [State(component_id='stats_dd', component_property='value')])


def input_stats(n_clicks, value):
    
    new_stats=html.Div(children=[
              html.H4(children='Podaj wartosć'),
              dcc.Dropdown(id='value_sign',
                          options=[
            {'label': 'więcej niż', 'value': '>'},
            {'label': 'równe', 'value': '='},
            {'label': 'mniej niż', 'value': '<'}
        ],),
                dcc.Input(id='stats_value',
                          type='text',
                          value='',
                          
                            placeholder='Wpisz wartosć'),
                

              html.Button('Dodaj', id='stats_values_add_button', n_clicks=0),
              dcc.Input(id='control_2', value=value)

                ])

    if n_clicks > 0:
            
            return new_stats

@app.callback(Output(component_id='stats_table',component_property='children'),
              [Input(component_id='stats_values_add_button', component_property='n_clicks')],
               [State('value_sign','value'),
                State('stats_value','value'),
                State('control_2','value')])

def define_stats_range(n_clicks, value_sign, stats_value, control_2):
    if n_clicks>0:
        sql_dict[control_2]=''.join([value_sign, stats_value])

@app.callback(Output(component_id='filter_table',component_property='children' ),
              [Input(component_id='show_filters', component_property='n_clicks')])
               
              
def show_filters(n_clicks):
    
    filters_df = pd.DataFrame([sql_dict])
    

    data = filters_df.to_dict('rows')
    columns = [{"name": i, "id": i, } for i in (filters_df.columns)]
    
    if n_clicks>0:
        
        return html.Div([dt.DataTable(data=data, columns=columns),
                         html.Button('Podkaż dane', id='show_data_button', n_clicks=0)])

@app.callback(Output(component_id='sql_table',component_property='children' ),
              [Input(component_id='show_data_button', component_property='n_clicks')])  


def show_data(n_clicks):
    
    result = {}
    for k, v in sql_dict.items():
        result[column_dict.get(k, k)] = v
    
    select='SELECT players.name, '
    fromT=' FROM players '
    joinT=' INNER JOIN '
    whereAsk=' WHERE '
   
    tables=[]
    
    joins=[]
    where=[]
    
    query=''
    conditionDict={'nations':'nations.id=players.nationality_id',
               'clubs':'clubs.id=players.club_id',
               'player_score':'players.id=player_score.player_id',
               'player_stats':'players.id=player_stats.playerid'}
               
    for k in sql_schema_dict:
        for v in sql_schema_dict[k]:
            for key in result.keys():
                if key==v:
                    tables.append(k+'.'+v)
                    joins.append('INNER JOIN '+k+' ON '+ conditionDict[k])
                    if k in ['player_score', 'player_stats']:
                        
                        where.append(' '+v+result[v])
                    else:
                        
                        condition=result[v]
                        conditionQuote=f"'{condition}'"
                        where.append(' '+v+'='+conditionQuote)
                    
                        
                        
                    

    joins_unique=np.unique(joins)
    selectedTables=','.join(tables)
    selectedJoins=' '.join(joins_unique)
    selectedWhere=' AND '.join(where)
    allWhere=whereAsk+selectedWhere
    query=select+selectedTables+fromT+selectedJoins+allWhere
    
    db_search_execute = cursor.execute(query).fetchall()
    query_result_search= [dict(line) for line in
                        [zip([column[0] for column in cursor.description], row) for row in db_search_execute]]
    db_df_search = pd.DataFrame(query_result_search)


    data = db_df_search.to_dict('rows')
    columns = [{"name": i, "id": i, } for i in (db_df_search.columns)]

    if n_clicks>0:
        return dt.DataTable(data=data, columns=columns)
    

if __name__ == '__main__':
    app.run_server()

    