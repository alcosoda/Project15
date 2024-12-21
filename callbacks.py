from dash import Input, Output, State
from utils import get_weather_data
from dash import html


def register_callbacks(app):
    @app.callback(
        Output("weather-output", "children"),
        [Input("form-data", "data")],
    )
    def update_output(data):
        if data is None:
            return ""

        start_point = data.get("start_point")
        end_point = data.get("end_point")

        start_weather = get_weather_data(start_point)
        end_weather = get_weather_data(end_point)

        if start_weather and end_weather:
            return html.Div(children=[
                html.H2(children="Прогноз погоды"),
                html.P(children="Начальная точка: {} - Температура: {}°C, Скорость ветра: {} м/с, Осадки: {} мм".format(
                    start_point, start_weather['temperature'], start_weather['wind_speed'],
                    start_weather['precipitation']
                )),
                html.P(children="Конечная точка: {} - Температура: {}°C, Скорость ветра: {} м/с, Осадки: {} мм".format(
                    end_point, end_weather['temperature'], end_weather['wind_speed'], end_weather['precipitation']
                )),
            ])
        else:
            return html.Div(children=[
                html.H2(children="Прогноз погоды"),
                html.P(children="Не удалось получить данные о погоде для указанных городов."),
            ])

    @app.callback(
        Output("form-data", "data"),
        [Input("submit-button", "n_clicks")],
        [State("start-point", "value"), State("end-point", "value")],
    )
    def update_store(n_clicks, start_point, end_point):
        if n_clicks is None:
            return {}
        return {"start_point": start_point, "end_point": end_point}