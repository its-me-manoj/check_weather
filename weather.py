from dotenv import load_dotenv
from pprint import pprint
import requests
import os

#link the env api 
load_dotenv() 

#get the data for the city
def get_weather(city):
    req_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"
    data = requests.get(req_url).json()
    return data

#main function
if __name__ == "__main__":
    city = input("Enter the city : ")
    weather_data = get_weather(city)
    print('\n')
    pprint(weather_data)


