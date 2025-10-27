from current_temp_API.api import OpenMeteo, OpenWeather

open_meteo_obj = OpenMeteo(52.52, 13.41)
print(str(open_meteo_obj.get_current_temperature()) + " C")

open_weather_obj = OpenWeather(52.52, 13.41, api_token="68201ab01d21b62cb523e0f86f0aa8f3")
print(str(open_weather_obj.get_current_temperature()) + " K")