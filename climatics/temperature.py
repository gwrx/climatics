import requests

class outside:

    fahrenheit = 0
    weatherData = ''
    timestamp = None

    def __init__(self):
        self.updateWeaterData()

    def __str__(self):
        return 'Fahrenheit: %d, Celsius: %d' % (self.fahrenheit, self.toCelsius())

    def toCelsius(self):
        return self.fahrenheit - 273.15

    def updateWeaterData(self):
        apikey = '1173240003ba1e0408a5ccb5e14d6706'
        location = 'Innsbruck, at'
        urlStart = 'http://api.openweathermap.org/data/2.5/weather?q='
        url = urlStart + location + '&appid=' + apikey
        data = requests.get(url)
        self.weatherData = data.json()
        self.fahrenheit = self.weatherData['main']['temp']





