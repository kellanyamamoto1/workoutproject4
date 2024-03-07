# Kellan Yamamoto 
# 28388886
# kellany@uci.edu

import matplotlib.pyplot as plt
import requests, json, urllib
from datetime import datetime, timedelta

class WeatherPlotter:
    def __init__(self, api_key, zipcode, ccode, num_days):
        self.api_key = api_key
        self.zipcode = zipcode
        self.ccode = ccode
        self.num_days = num_days
        
    
    def fetch_weather_data(self):
        url = f"https://api.openweathermap.org/data/2.5/forecast?zip={self.zipcode},{self.ccode}&appid={self.api_key}&units=metric"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data
    
    def plot_temperatures(self, data) -> None:
        dates = []
        temperatures = []
        try: 
            for entry in data['list']:
                date = datetime.fromtimestamp(entry['dt'])
                if date.date() not in dates:
                    dates.append(date.date())
                    temperatures.append(entry['main']['temp'])
                if len(dates) == self.num_days:
                    break
        except KeyError as e:
            print(f"Error: Could not find key in data dictionary: {e}")
            return
        
    
        plt.figure(figsize=(12, 6))
        plt.plot(dates, temperatures, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title(f'Temperature in {self.zipcode} over the next {self.num_days} days')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    api_key = 'ceb8cbc931c2f41301ba4a1548020fd4'
    zipcode = '96797'
    ccode = 'US'
    num_days = 14

    weather_plotter = WeatherPlotter(api_key, zipcode, ccode, num_days)
    weather_data = weather_plotter.fetch_weather_data()
    weather_plotter.plot_temperatures(weather_data)

if __name__ == "__main__":
    main()