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
        html.Button(type="submit", id="submit-button", children="Получить прогноз"),  # Изменение
    ]),
    html.Div(id="dash-app"),
])


def get_weather_data(location, api_key='YOUR_API_KEY'):
    # Замените YOUR_API_KEY на ваш API ключ от AccuWeather
    base_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {'apikey': api_key, 'q': location}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        location_key = response.json()[0]['Key']

        forecast_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}"
        forecast_params = {'apikey': api_key, 'metric': True}
        forecast_response = requests.get(forecast_url, params=forecast_params)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()['DailyForecasts'][0]
            return {
                'temperature': forecast_data['Temperature']['Maximum']['Value'],
                'wind_speed': forecast_data['Day']['Wind']['Speed']['Value'],
                'precipitation': forecast_data['Day']['TotalLiquid']['Value'],
            }
    return None


@app.callback(
    Output("dash-app", "children"),
    [Input("submit-button", "n_clicks")],  # Изменение
    [State("start-point", "value"), State("end-point", "value")],
)
def update_output(n_clicks, start_point, end_point):
    if n_clicks is None:
        return ""

    start_weather = get_weather_data(start_point)
    end_weather = get_weather_data(end_point)

    return html.Div(children=[
        html.H2(children="Прогноз погоды"),
        html.P(children="Начальная точка: {} - Температура: {}°C, Скорость ветра: {} м/с, Осадки: {} мм".format(
            start_point, start_weather['temperature'], start_weather['wind_speed'], start_weather['precipitation']
        )),
        html.P(children="Конечная точка: {} - Температура: {}°C, Скорость ветра: {} м/с, Осадки: {} мм".format(
            end_point, end_weather['temperature'], end_weather['wind_speed'], end_weather['precipitation']
        )),
    ])


if __name__ == '__main__':
    app.run_server(debug=True)