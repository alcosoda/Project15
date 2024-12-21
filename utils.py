import requests

def get_weather_data(location, api_key='Fv4JolXK4AKTAX2FsbEp0JLln58mwQD0'):
    # Замените YOUR_API_KEY на ваш API ключ от AccuWeather
    base_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {'apikey': api_key, 'q': location}
    response = requests.get(base_url, params=params)
    if response.status_code == 200 and response.json():  # Добавлена проверка на response.json()
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
    else:
        print(f"Error: {response.status_code} - {response.text}")  # Вывод ошибки в консоль для отладки
        return None
    return None