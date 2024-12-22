from ipyleaflet import Map, Marker, Polyline
import requests

def create_map(cities, api_key):
    city_coordinates = {}
    for city in cities:
        coordinates = get_coordinates(city, api_key)  # Изменяем вызов функции
        if coordinates:
            city_coordinates[city] = coordinates

    if city_coordinates:
        m = Map(center=list(city_coordinates.values())[0], zoom=5)

        for city, coordinates in city_coordinates.items():
            marker = Marker(location=coordinates, title=city)
            m.add_layer(marker)

        locations = list(city_coordinates.values())
        if len(locations) > 1:
            polyline = Polyline(locations=locations, color="red", weight=3)
            m.add_layer(polyline)

        return m
    else:
        return None

def get_coordinates(city, api_key):
    """Получает координаты города от AccuWeather API."""
    headers = {'apikey': api_key}
    url = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={api_key}&q={city}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return (data['Latitude'], data['Longitude'])
    return None