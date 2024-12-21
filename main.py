import dash
from dash import html, dcc, Input, Output, State
import requests

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Прогноз погоды"),
    html.Form(id="route-form", children=[
        html.Label(htmlFor="start-point", children="Начальная точка:"),
        dcc.Input(type="text", id="start-point", name="start-point"),
        html.Br(), html.Br(),
        html.Label(htmlFor="end-point", children="Конечная точка:"),
        dcc.Input(type="text", id="end-point", name="end-point"),
        html.Br(), html.Br(),
        html.Button(type="submit", children="Получить прогноз"),
    ]),
    html.Div(id="dash-app"),
])


@app.callback(
    Output("dash-app", "children"),
    [Input("route-form", "n_submit")],
    [State("start-point", "value"), State("end-point", "value")],
)
def update_output(n_submit, start_point, end_point):
    if n_submit is None:
        return ""

    # Здесь будет код для получения данных о погоде с помощью AccuWeather API
    # и построения графиков с помощью Plotly

    return "Данные о погоде для маршрута: {} - {}".format(start_point, end_point)


if __name__ == '__main__':
    app.run_server(debug=True)