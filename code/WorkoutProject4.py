# Kellan Yamamoto 
# 28388886
# kellany@uci.edu

import math
import matplotlib
import matplotlib.pyplot as plt
import requests
from datetime import datetime, timedelta

class WeatherPlotter:
    def __init__(self, api_key, city, num_days):
        self.api_key = api_key
        self.city = city
        self.num_days = num_days
        self.base_url = f'http://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.api_key}&units=metric'
    
    def fetch_weather_data(self):
        response = requests.get(self.base_url)
        data = response.json()
        return data
    
    def plot_temperatures(self, data):
        dates = []
        temperatures = []
        for entry in data['list']:
            date = datetime.fromtimestamp(entry['dt'])
            if date.date() not in dates:
                dates.append(date.date())
                temperatures.append(entry['main']['temp'])
            if len(dates) == self.num_days:
                break
        
        plt.figure(figsize=(12, 6))
        plt.plot(dates, temperatures, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title(f'Temperature in {self.city} over the next {self.num_days} days')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    api_key = 'your_api_key_here'
    city = 'Irinve,US'
    num_days = 14

    weather_plotter = WeatherPlotter(api_key, city, num_days)
    weather_data = weather_plotter.fetch_weather_data()
    weather_plotter.plot_temperatures(weather_data)

if __name__ == "__main__":
    main()