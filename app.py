from flask import Flask, render_template, request
from logic import Connect, Weather
from visualizations import create_visualizations  # Импортируем функцию

app = Flask(__name__)
api_key = 'Fv4JolXK4AKTAX2FsbEp0JLln58mwQD0'  # Replace with your AccuWeather API key

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        try:
            cities = request.form.getlist('cities[]')
            weather_data = {}

            for city in cities:
                api = Connect(api_key=api_key)
                weather_lst = api.get_weather(city)

                weather_data[city] = []
                for item in weather_lst:
                    item.info = item.validate()
                    weather_data[city].append(item)

            visualizations = create_visualizations(weather_data)  # Создаем визуализации
            return render_template('result.html', weather_data=weather_data, visualizations=visualizations, format={'Day': 'День', 'Night': 'Ночь'})

        except KeyError:
            return render_template('error_message.html', msg='В форме не хватает полей')
        except IndexError:
            return render_template('error_message.html', msg='Город не найден')
        except Exception:
            return render_template('error_message.html', msg='Не удаётся подключиться к API')

    return render_template('input.html')

if __name__ == '__main__':
    app.run()