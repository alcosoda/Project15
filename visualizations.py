import plotly.express as px
import pandas as pd

def create_visualizations(weather_data):
    """
    Создает визуализации данных о погоде.

    Args:
        weather_data: Словарь с данными о погоде для каждого города.

    Returns:
        Словарь с визуализациями для каждого города.
    """
    visualizations = {}
    for city, weather in weather_data.items():
        df = pd.DataFrame(weather)
        # Создаем график температуры
        temp_fig = px.line(df, x='date', y='temp_c', title=f'Температура в {city}')
        # Создаем график скорости ветра
        wind_fig = px.line(df, x='date', y='wind', title=f'Скорость ветра в {city}')
        # Создаем график вероятности дождя
        rain_fig = px.line(df, x='date', y='rain', title=f'Вероятность дождя в {city}')
        # Создаем график влажности
        humidity_fig = px.line(df, x='date', y='humidity', title=f'Влажность в {city}')
        # Сохраняем визуализации в словарь
        visualizations[city] = {
            'temp': temp_fig.to_html(),
            'wind': wind_fig.to_html(),
            'rain': rain_fig.to_html(),
            'humidity': humidity_fig.to_html()
        }
    return visualizations