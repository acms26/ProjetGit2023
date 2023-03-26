import dash
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#%% Charger les données
names = ["date","world_population","population_growth_year_to_date"]

df = pd.read_csv('data.csv', delimiter=';', names = names)

df["date"] = pd.to_datetime(df["date"])
df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: x.str.replace(',', '').astype(float)) # convert to float because not possible to convert to int

# Créer une application Dash
app = Dash(__name__)



#%% Figure
#Axe principal zone population
df2 = df[['date',"world_population",'population_growth_year_to_date']].copy()
df2["population_growth"] = df2.population_growth_year_to_date / (df2.world_population - df2.population_growth_year_to_date) * 100
df2["world_population"] = df2["world_population"].apply(lambda x:x*10**-11)

area_trace = go.Scatter(x=df2['date'], y=df2['world_population'],
                        name='World&nbsp;Population',
                        fill='tozeroy',
                        marker_color = '#126C94')

# Taux de croissance de la population
line_trace = go.Scatter(x=df2['date'], y=df2['population_growth'],
                        name='Population Growth year to date (%)',
                        mode='lines',
                        marker_color = '#E90064')

# Axe Y secondaire
invisible_trace = go.Scatter(x=df2['date'], y=[0]*len(df2),
                             mode='markers',
                             name='invisible',
                             marker=dict(color='rgba(0,0,0,0)'),
                             showlegend=False, yaxis='y2', visible=False)


# Combinaison des tracés
fig2 = go.Figure(data=[area_trace, line_trace, invisible_trace])

# Configurer l'axe y secondaire pour l'axe du taux de croissance de la population
fig2.add_trace(go.Scatter(x=df2['date'], y=df2['population_growth'], visible=False, yaxis='y2', showlegend=False))

# Configurer l'aspect des deux axes y
fig2.update_layout(title_text = "Population Growth and World Population",
                  xaxis = dict(title = "Date", showgrid = False),
                  yaxis=dict(title='World Population (trillions)'),
                  yaxis2=dict(title='Pop Growth year to date (%)',
                              overlaying='y',
                              side='right',
                              showgrid = False),
                  font_family = "Rockwell",
                  )
### END Figure###

#%%
app.layout = html.Div(children=[
    html.H1(children='World Population Satistics'),

    html.Div(children = '''
        population and growth population
    '''),
    dcc.Graph(
        id='world-growth-population-graph',

        figure = fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
