import plotly.express as px
import pandas as pd

def create_visualizations(weather_data):
    visualizations = {}
    for city, weather in weather_data.items():
        df = pd.DataFrame(weather)
        temp_fig = px.line(df, x='date', y='temp_c', title=f'Температура в {city}')
        wind_fig = px.line(df, x='date', y='wind', title=f'Скорость ветра в {city}')
        rain_fig = px.line(df, x='date', y='rain', title=f'Вероятность дождя в {city}')
        humidity_fig = px.line(df, x='date', y='humidity', title=f'Влажность в {city}')
        visualizations[city] = {
            'temp': temp_fig.to_html(),
            'wind': wind_fig.to_html(),
            'rain': rain_fig.to_html(),
            'humidity': humidity_fig.to_html()
        }
    return visualizations