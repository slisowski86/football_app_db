# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:59:12 2020

@author: sliso
"""

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:10:10 2020

@author: sliso
"""
import cx_Oracle
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import psycopg2
import numpy as np
import pandas as pd



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash(__name__, external_stylesheets=external_stylesheets)

dsn_tns = cx_Oracle.makedsn('dbserver.mif.pg.gda.pl', '1521',
                                service_name='ORACLEMIF')




#psycopg2.connect(DATABASE_URL, sslmode='require')


players=[]
nationality=[]
clubs=[]
score=[]
stats=[]

try:
    conn = cx_Oracle.connect(user=r'SLISOW_P', password='g2D8M', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM players")
    players=cursor.fetchall()
    cursor.execute("SELECT nationality_name FROM nations")
    nationality=cursor.fetchall()
    cursor.execute("SELECT club_name FROM clubs")
    clubs=cursor.fetchall()
    cursor.execute("Select * FROM player_score")
    
    score = [desc[0] for desc in cursor.description]
    cursor.execute("Select * FROM player_stats")
    
    stats = [desc[0] for desc in cursor.description]
    conn.commit()
    
    cursor.close()
except cx_Oracle.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
    



club_unique=list(np.unique(clubs))
nationality_unique=list(np.unique(nationality))
club_unique.append('All')
nationality_unique.append('All')

score.remove('PLAYER_ID')
stats.remove('PLAYER_ID')
score = [element.lower() for element in score]
stats = [element.lower() for element in stats]
score.append('All')
stats.append('All')




app.layout = html.Div(children=[
    
   
    html.H2(children="Aplikacja Football Stats", style={"background-color":"tomato"}),
    html.H3(children="Wyszukaj statystyki według imienia i nazwiska zawodnika", style={'border-style':'solid'}),
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
    html.H3(children="Wyszukaj zawodników", style={'border-style':'solid'}),
    html.H4(children="Wiek"),
    dcc.Dropdown(id='age_value_sign',
                          options=[
                              
            {'label': 'more_than', 'value': '>'},
            {'label': 'equal', 'value': '='},
            {'label': 'less_than', 'value': '<'},
            {'label': 'All', 'value': 'All'}
        ],
        placeholder="wybierz filtr",
        style={'width':'40%'}),
    dcc.Input(id='age_value',
                          type='text',
                          value='',
                          
                            placeholder='Wpisz wartosć'),
    html.Button('Wstaw',id='age_button', n_clicks=0),
    html.H4(children="Narodowość"),
    dcc.Dropdown(id="nations_dd",
                 options=[
                     {'label': i, 'value': i} for i in nationality_unique
                 ],
                 placeholder="wybierz narodowosć",
                 style={'width':'40%'}


                 ),
    
    html.Button('Wstaw',id='nations_dd_button',n_clicks=0),
        
    html.H4(children="Klub"),
    dcc.Dropdown(id="clubs_dd",
                 options=[
                     {'label': i, 'value': i} for i in club_unique
                 ],
                 placeholder="wybierz klub",
                 style={'width':'40%'}


                 ),
    html.Button('Wstaw',id='clubs_dd_button', n_clicks=0),
    
    html.H4(children="Punktacja"),
    dcc.Dropdown(id="score_dd",
                 options=[
                     {'label': i, 'value': i} for i in score
                 ],
                 placeholder="wybierz",
                 style={'width':'40%'}


                 ),
    dcc.Dropdown(id='score_value_sign',
                          options=[
            {'label': 'more_than', 'value': '>'},
            {'label': 'equal', 'value': '='},
            {'label': 'less_than', 'value': '<'}
        ],
        placeholder="wybierz filtr",
        style={'width':'40%'}),
    
    
    dcc.Input(id='score_value',
                          type='text',
                          value='',
                          
                            placeholder='Wpisz wartosć'),
    html.Button('Wstaw',id='score_dd_button', n_clicks=0),
    html.H4(children="Statystyki"),
    dcc.Dropdown(id="stats_dd",
                 options=[
                     {'label': i, 'value': i} for i in stats
                 ],
                 placeholder="wybierz filtr",
                 style={'width':'40%'}

                 ),
    dcc.Dropdown(id='stats_value_sign',
                          options=[
            {'label': 'more_than', 'value': '>'},
            {'label': 'equal', 'value': '='},
            {'label': 'less_than', 'value': '<'}
        ],),
    
    
    dcc.Input(id='stats_value',
                          type='text',
                          value='',
                          
                            placeholder='Wpisz wartosć'),
    html.Button('Wstaw',id='stats_dd_button', n_clicks=0),
    html.Div(id='score_container'),
    html.Div(id='score_table'),
    
    
    dt.DataTable(id='filters_table', columns=[{'id':'tabela', 'name':'tabela'},
                                                {'id':'filtr', 'name':'filtr'},
                                              {'id':'dane', 'name':'dane'}], data=[],
                                     row_deletable=True
                                     ),
    
    html.Button('Pokaż dane',id='show_data_button', n_clicks=0),
    html.Div(id='sql_table'),
    
    
   

])





@app.callback(Output(component_id='table',component_property='children' ),
              [Input(component_id='search', component_property='n_clicks')],
              [State(component_id='input_1', component_property='value')])


def update_table(n_clicks, value):
    
    
    db_execute=[]

    name={'player':value}

    query_result=[]

    

    if n_clicks>0:
        try:
            conn = cx_Oracle.connect(user=r'SLISOW_P', password='g2D8M', dsn=dsn_tns)
            cursor = conn.cursor()
            cursor.execute("SELECT name,age, nations.nationality_name, clubs.club_name, player_score.* FROM players, nations, clubs, player_score WHERE players.name = :player AND players.nationality_id=nations.id AND players.club_id=clubs.id AND player_score.player_id=players.id" ,name)
            db_execute=cursor.fetchall()
            query_result = [dict(line) for line in
                        [zip([column[0] for column in cursor.description], row) for row in db_execute]]
            conn.commit()
        
            cursor.close()
        except cx_Oracle.DatabaseError as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
       
        db_df = pd.DataFrame(query_result)
   

        data = db_df.to_dict('rows')
        columns = [{"name": i, "id": i, } for i in (db_df.columns)]
        return dt.DataTable( data=data, columns=columns)





                        
@app.callback(Output('filters_table', 'data'),
               
              [Input('age_button', 'n_clicks'),
                Input('nations_dd_button', 'n_clicks'),
               Input('clubs_dd_button', 'n_clicks'),
               Input('score_dd_button', 'n_clicks'),
               Input('stats_dd_button', 'n_clicks')],
              [State('age_value_sign', 'value'),
               State('age_value', 'value'),
               State('nations_dd', 'value'),
               State('clubs_dd', 'value'),
               State('score_dd', 'value'),
               State('score_value_sign', 'value'),
               State('score_value', 'value'),
               State('stats_dd', 'value'),
               State('stats_value_sign', 'value'),
               State('stats_value', 'value'),
               
               State('filters_table', 'data')])
               

def update_filters(age_button, nations_dd_button, clubs_dd_button, score_dd_button, stats_dd_button, age_sign, value_age,  value_nations, value_club, score_name,score_sign, score_value, stats_name,stats_sign, stats_value , existing_data):
    ctx = dash.callback_context
    
    button_id=''
    
    if not ctx.triggered:
        
        button_id=''
    
    else:
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
        if button_id=='age_button':
            
            existing_data.append({'tabela':'players',
                                    'filtr':'age',
                                 'dane':str(age_sign)+value_age})
        
        elif button_id=='nations_dd_button':
            
            existing_data.append({'tabela':'nations',
                                    'filtr':'nationality_name',
                                 'dane':value_nations})
        
        elif button_id=='clubs_dd_button':
           
            existing_data.append({'tabela':'clubs',
                                    'filtr':'club_name',
                                 'dane':value_club})
            
        elif button_id=='score_dd_button':
           
            existing_data.append({'tabela':'player_score',
                                    'filtr':score_name,
                                 'dane':str(score_sign)+score_value})
            
        elif button_id=='stats_dd_button':
           
             existing_data.append({'tabela':'player_stats',
                                 'filtr':stats_name,
                                 'dane':str(stats_sign)+stats_value})
             
   
       
    return  existing_data


@app.callback(Output('age_value', 'disabled'),
               
              [Input('age_value_sign','value')])


def disable_age_value(value):
    
    if value=='All':
        return True

@app.callback(Output('score_value_sign', 'disabled'),
               
              [Input('score_dd','value')])



def disable_dd_score(value):
    
    if value=='All':
        return True
                
    
    
@app.callback(Output('stats_value_sign', 'disabled'),
               
              [Input('stats_dd','value')])


def disable_dd_stats(value):
    
    if value=='All':
        
        return True
    
@app.callback(Output('score_value', 'disabled'),
              
              [Input('score_dd','value')])



def disable_score_input(value):
    
    if value=='All':
        return True
                
    
    
@app.callback(Output('stats_value', 'disabled'),
               
              [Input('stats_dd','value')])


def disable_statsinput(value):
    
    if value=='All':
        
        return True
                
@app.callback(Output('sql_table','children'),
              [Input('show_data_button','n_clicks'),
               Input('filters_table','data')])

def show_data(n_clicks, data):
    constraintDict={'nations':'nations.id=players.nationality_id',
               'clubs':'clubs.id=players.club_id',
               'player_score':'players.id=player_score.player_id',
               'player_stats':'players.id=player_stats.player_id',
               'players':'age'}
    sql_dict={}
    tables=[]
    joins=[]
    whereConditions=[]
    db_search_execute=[]
    query_result_search=[]
    query=''
    select="SELECT players.name,"
    fromQuery=" FROM players "
    join=" INNER JOIN "
    on=" ON "
    where=""
    
    
    if n_clicks>0:
        
        
        
        for d in data:
            for k in d.keys():
                sql_dict[d[list(d)[0]]]=[{d[list(d)[1]]: d[list(d)[2]]}]
        
        for k  in sql_dict.keys():
            for v in sql_dict[k]:
                for key in v.keys():
                    if k=='players':
                        if v[key]=='All':
                            tables.append(str(k)+'.'+str(key))
                            joins.append(' ')
                            where=''
                        else:
                            tables.append(str(k)+'.'+str(key))
                            joins.append(' ')
                            where=' WHERE '
                            whereConditions.append(str(key)+v[key])
                    elif k=='player_score':
                        if key=='All':
                            
                            tables.append(str(k)+'.*')
                            joins.append(join+ str(k) + on + constraintDict[k])
                            
                    
                        else:
                            tables.append(str(k)+'.'+str(key))
                            joins.append(join+ str(k) + on + constraintDict[k])
                            whereConditions.append(str(key)+v[key])
                            where=' WHERE '
                    elif k=='player_stats':
                        if key=='All':
                            
                            tables.append(str(k)+'.*')
                            joins.append(join+ str(k) + on + constraintDict[k])
                            
                    
                        else:
                            tables.append(str(k)+'.'+str(key))
                            joins.append(join+ str(k) + on + constraintDict[k])
                            whereConditions.append(str(key)+v[key])
                            where=' WHERE '
                    elif k=='clubs':
                        if v[key]=='All':
                            tables.append(str(k)+'.'+str(key))
                            joins.append(join+ str(k) + on + constraintDict[k])
                            
                        else:
                            tables.append(str(k)+'.'+str(key))
                            joins.append(join+ str(k) + on + constraintDict[k])
                            condition=v[key]
                            conditionQuote=f"'{condition}'"
                            whereConditions.append(str(key)+'='+conditionQuote)
                            where=' WHERE '
                    elif k=='nations':
                        if v[key]=='All':
                            tables.append(str(k)+'.'+str(key))
                            joins.append(join+ str(k) + on + constraintDict[k])
                            
                        else:
                            tables.append(str(k)+'.'+str(key))
                            joins.append(join+ str(k) + on + constraintDict[k])
                            condition=v[key]
                            conditionQuote=f"'{condition}'"
                            whereConditions.append(str(key)+'='+conditionQuote)
                            where=' WHERE '
                   
                        
                    
        if len(tables)>0:
            selectedTables=', '.join(tables)
            selectedJoins=''.join(joins)
            selectedWhere= ' AND '.join(whereConditions)
            query=select+selectedTables+fromQuery+selectedJoins+where+selectedWhere
       
            try:
                conn = cx_Oracle.connect(user=r'SLISOW_P', password='g2D8M', dsn=dsn_tns)
                cursor = conn.cursor()
                cursor.execute(query)
                db_search_execute=cursor.fetchall()
                query_result_search= [dict(line) for line in
                        [zip([column[0] for column in cursor.description], row) for row in db_search_execute]]
                conn.commit()
        
                cursor.close()
            except cx_Oracle.DatabaseError as error:
                print(error)
            finally:
                if conn is not None:
                        conn.close()
            db_df_search = pd.DataFrame(query_result_search)


            data = db_df_search.to_dict('records')
            columns = [{"name": i, "id": i, } for i in (db_df_search.columns)]
        
        
            return html.Div(children=[html.A(html.Button('Nowe wyszukiwanie'),href='/'),
                                      html.H6(children="Twoje zapytanie: "+query),
                                      dt.DataTable(data=data, columns=columns)])
        
        else:
            html.Div(children=[html.A(html.Button('Nowe wyszukiwanie'),href='/'),
                               html.H6(children="Brak danych")])
                               
        
if __name__ == '__main__':
    app.run_server()