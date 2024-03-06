from observee.weatherData import WeatherData
from observer.display import Display

display1=Display()
display2=Display()

weather_data=WeatherData()

weather_data.add_obervers(display1)
weather_data.add_obervers(display2)

weather_data.set_measurements(65)
weather_data.set_measurements(56)

weather_data.remove_observer(display2)

weather_data.set_measurements(36)
