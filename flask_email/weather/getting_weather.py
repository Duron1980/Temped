import requests


def get_weather(city: str, api_id: str):
    """Get weather to city name"""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}&units=metric'
    response = requests.get(url)

    if response.status_code != 200:
        message = f'openweathermap.org returned non-200 code. Actual code is: {response.status_code},' \
                  f' message is: {response.json()["message"]}'
        raise RuntimeError(message)

    return response.json()


def determine_temperature(city: dict):
    """Determine temperature"""
    temperature = city['main']['temp']
    return f'warm' if temperature > 20 else 'cold'


def main(city_name: str, id: str):
    """Main controller"""
    city = get_weather(city_name, id)
    weather_condition = determine_temperature(city)
    temperature = city['main']['temp']
    return f'It is {weather_condition}, temperature is {temperature}'


ID = '0107cbd8cd431b1dbff7f14411b36127'
print(main('Tokyo', ID))
