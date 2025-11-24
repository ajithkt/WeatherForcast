import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("API_KEY")

def getdata(place,forcasted_days):
    url= f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:forcasted_days * 8]
    return filtered_data

if __name__ == "__main__":
    print(getdata("tokyo", 1))