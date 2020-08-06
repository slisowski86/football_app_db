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


cursor = dbcon.db_connect()



players=cursor.execute("SELECT name FROM players ").fetchall()




app.layout = html.Div(children=[
    html.H2(children="Aplikacja Football Score"),
    html.Datalist(
    id='player_suggested',
    children=[html.Option(value=word) for word in players]),

    dcc.Input(id='input1',
    type='text',
    list='player_suggested',
    value='',
    placeholder='Wpisz imię zawodnika...'),

    html.Button( id='show_player_info', children='Submit'),
    html.Div(id='table')




])



@app.callback(Output(component_id='table',component_property='children' ),
              [Input(component_id='show_player_info', component_property='n_clicks')],
              [State(component_id='input1', component_property='value')])



def update_table(n_clicks, input1 ):





    if n_clicks is not None:
        x = input1
        name = {'player': x}
        db_execute = cursor.execute(
            "SELECT name,age, nations.nationality_name, clubs.club_name, player_score.* FROM players, nations, clubs, player_score WHERE players.name = :player AND players.nationality_id=nations.id AND players.club_id=clubs.id AND player_score.player_id=players.id",
            name).fetchall()
        query_result = [dict(line) for line in
                        [zip([column[0] for column in cursor.description], row) for row in db_execute]]
        db_df = pd.DataFrame(query_result)

        return html.Div([
			dt.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in db_df.columns],
            data=db_df.to_dict("rows"),
            style_cell={'width': '300px',

				'height': '60px',
				'textAlign': 'left'})
			])






if __name__ == '__main__':
    app.run_server()