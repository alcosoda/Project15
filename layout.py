from dash import html, dcc

layout = html.Div(children=[
    html.H1(children="Прогноз погоды"),
    html.Form(id="route-form", children=[
        html.Label(htmlFor="start-point", children="Начальная точка:"),
        dcc.Input(type="text", id="start-point", name="start-point"),
        html.Br(), html.Br(),
        html.Label(htmlFor="end-point", children="Конечная точка:"),
        dcc.Input(type="text", id="end-point", name="end-point"),
        html.Br(), html.Br(),
        html.Button(type="submit", id="submit-button", children="Получить прогноз"),
    ]),
    html.Div(id="weather-output"),
    dcc.Store(id='form-data') # Добавлено
])