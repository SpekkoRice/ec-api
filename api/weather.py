import requests
import json

class WeatherObject():
  def __init__(self, data):
    self.__dict__ = json.loads(data)
    # print(data)
    self.cityName = self.getName()
    self.windDirection = self.getWindDirection()
    self.visibility = self.getVisibility()
    self.windSpeed = self.getWindSpeed()
    self.degrees = self.getDegreesCell()

  def getWindSpeed(self):
    if hasattr(self, 'wind'):
      if 'speed' in self.wind:
        return self.wind['speed']
    return "N/A"

  def getWindDirection(self):
    if hasattr(self, 'wind'):
      if 'deg' in self.wind:
        val=int((self.wind['deg']/22.5)+.5)
        arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
        return arr[(val % 16)]
    return "N/A"

  def getVisibility(self):
    if hasattr(self, 'visibility'):
      return self.visibility
    return "N/A"

  def getDegreesCell(self):
    if hasattr(self, 'main'):
      if 'temp' in self.main:
        return self.main['temp']
    return "N/A"
  
  def getName(self):
    if hasattr(self, 'name'):
      return self.name
    return "N/A"
  


class WeatherApi():
  
  def __init__(self, apiUrl, apiKey):
    self.apiKey = apiKey
    self.apiUrl = apiUrl

  def getWeatherDetails(self, postalCode, countryCode="za"):
    print(self.apiKey)
    r = requests.get(self.apiUrl + "?zip=" + postalCode + "," +  countryCode + "&APPID=" + self.apiKey + "&units=metric")
    return WeatherObject(r.content)

  