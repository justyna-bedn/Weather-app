import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio

# pio.renderers.default = "browser"
#
# x = [1,2,3,4,5]
# y1 = [10,15,13,20,17]
# y2 = [3,7,4,9,6]
#
# produkty = ["A","B","C","D"]
# wyniki = [12,19,7,15]
#
# oceny = [2,4,5,2,3,4,5,4,3,2,3,4,5]
#
# etykiety = ["Python","Java","C++","Javascript"]
# wartosci = [40,25,15,20]
#
# # Tworzenie układu dashboardu
# fig = make_subplots(
#     rows=3, cols=2,
#     specs=[
#         [{"type": "xy"}, {"type": "xy"}],
#         [{"type": "xy"}, {"type": "xy"}],
#         [{"type": "domain"}, None]  # pie chart
#     ],
#     subplot_titles=("Line", "Bar", "Scatter", "Histogram", "Pie")
# )
#
# # LINE
# fig.add_trace(
#     go.Scatter(x=x, y=y1, mode="lines+markers", name="Line"),
#     row=1, col=1
# )
#
# # BAR
# fig.add_trace(
#     go.Bar(x=produkty, y=wyniki, orientation="h", name="Bar"),
#     row=1, col=2
# )
#
# # SCATTER
# fig.add_trace(
#     go.Scatter(x=x, y=y2, mode="markers", name="Scatter"),
#     row=2, col=1
# )
#
# # HISTOGRAM
# fig.add_trace(
#     go.Histogram(x=oceny, nbinsx=4, name="Histogram"),
#     row=2, col=2
# )
#
# # PIE
# fig.add_trace(
#     go.Pie(labels=etykiety, values=wartosci, name="Pie"),
#     row=3, col=1
# )
#
# # Layout
# fig.update_layout(
#     title="Dashboard Plotly",
#     height=900,
#     showlegend=False
# )
#
# fig.show()

import dash
from dash import dcc, html
# import plotly.express as px
#
# # Dane
# x = [1,2,3,4,5]
# y1 = [10,15,13,20,17]
# y2 = [3,7,4,9,6]
#
# produkty = ["A","B","C","D"]
# wyniki = [12,19,7,15]
#
# oceny = [2,4,5,2,3,4,5,4,3,2,3,4,5]
#
# etykiety = ["Python","Java","C++","Javascript"]
# wartosci = [40,25,15,20]
#
# # Wykresy
# fig_line = px.line(x=x, y=y1, title="Trend", markers=True)
# fig_bar = px.bar(x=produkty, y=wyniki, title="Produkty")
# fig_scatter = px.scatter(x=x, y=y2, title="Relacja")
# fig_hist = px.histogram(x=oceny, nbins=4, title="Oceny")
# fig_pie = px.pie(names=etykiety, values=wartosci, title="Języki")
#
# # Dashboard
# app = dash.Dash(__name__)
#
# app.layout = html.Div(
#     style={"fontFamily": "Arial", "backgroundColor": "#f5f7fa"},
#     children=[
#         html.H1("Mój Dashboard", style={"textAlign": "center"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_line),
#             dcc.Graph(figure=fig_bar),
#         ], style={"display": "flex"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_scatter),
#             dcc.Graph(figure=fig_hist),
#         ], style={"display": "flex"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_pie)
#         ])
#     ]
# )
#
# if __name__ == "__main__":
#     app.run(debug=True)

godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
wyniki = [40, 50, 55, 60, 70, 75, 85]

fig = px.scatter(
    x=godziny_nauki,
    y=wyniki,
    title="Zależność wyniku egzaminu od czasu nauki",
    labels={'x': 'Godziny nauki', 'y': 'Wynik egzaminu'}
)

fig.show()

#zadanie 5

jezyki = ["Python", "JavaScript", "Java", "C++", "Go"]
udzial = [35, 30, 15, 10, 10]

fig = px.pie(
    values=udzial,
    names=jezyki,
    title="Języki programowania w projekcie",
    color_discrete_sequence=px.colors.sequential.RdBu # Zmiana palety kolorów
)

fig.show()

#zadanie 6

dzien = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
temperatura = [18, 20, 19, 23, 25, 22, 21]

fig = px.line(
    x=dzien,
    y=temperatura,
    labels={'x': 'Dzień', 'y': 'Stopnie Celsjusza'},
    markers=True
)

fig.show()