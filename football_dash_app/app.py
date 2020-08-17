import cx_Oracle
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output, State
import cx_Oracle
import numpy as np
import pandas as pd
import dbmanager as dbcon




app=dash.Dash(__name__)
#łączenie z bazą danych


conn=dbcon.db_connect()

cursor=conn.cursor()



players=cursor.execute("SELECT name FROM players ").fetchall()
nationality=cursor.execute("SELECT nationality_name FROM nations").fetchall()
clubs=cursor.execute("SELECT club_name FROM clubs").fetchall()
club_unique=np.unique(clubs)
nationality_unique=np.unique(nationality)

column_dict={'Narodowość': 'nationality_name',
             'Klub':'club_name',
             'Wiek':'age',
             'Rozegrane mecze':'appearances',
             'Rozegrane minuty':'mins',
             'Bramki':'goals',
             'Asysty':'assists',
             'Zółte kartki':'yel',
             'Czerwone kartki':'red',
             'Strzały na mecz':'shots_per_game',
             'Celność podań(%)':'pass_score',
             'Wygrane główki':'aerialswon',
             'Piłkarz meczu': 'man_of_the_match',
             'Rating':'rating',
             'Idealna defensywa' : 'perfdef',
             'Idealny atak':'perfattack',
             'Idealne ustawienie': 'perfposs',
             'Total':'total'}
data_to_report=list(column_dict.keys())
    #['Narodowość', 'Klub', 'Wiek', 'Rozegrane mecze', 'Rozegrane minuty', 'Bramki',
                #'Asysty', 'Żółte kartki', 'Czerowne kartki', 'Strzały na mecz', 'Celność podań(%)',
                #'Wygrane główki', 'Piłkarz meczu', 'Rating', 'Idealna defensywa', 'Idealny atak', 'Idealne ustawienie',
                #'Total']

club_nat_dict={'Narodowość': nationality_unique,
               'Klub': club_unique}
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
    dcc.Dropdown(id="nations_dd",
                 options=[
                     {'label': i, 'value': i} for i in data_to_report
                 ],


                 ),
    html.Button('Wstaw',id='dd_button', n_clicks=0),
    html.Div(id="out1")



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



@app.callback(Output(component_id='out1', component_property='children'),
              [Input(component_id='dd_button', component_property='n_clicks')],
              [State(component_id='nations_dd', component_property='value')])


def update_table_features(n_clicks, value):

    if n_clicks > 0:
        if str(value) in club_nat_dict.keys():

            return html.Div(children=[
              html.H4(children=value),
                html.Datalist(
                    id='nat_club_unique',
                    children=[html.Option(value=word) for word in club_nat_dict.get(value)]),
              dcc.Input(id='input_text',
                        type='text',
                        list='nat_club_unique'),

              html.Button('Dodaj', id='add_button')

                ])
        else:
            return html.Div(children=[
              html.H4(children=value),
                dcc.Input(id='min_value',
                          type='text',
                          value='',
                            placeholder='Wpisz min'),
                dcc.Input(id='max_value',
                          type='text',
                          value='',
                            placeholder='Wpisz max'),

              html.Button('Dodaj', id='add_button')

                ])




if __name__ == '__main__':

    app.run_server()