import requests
import sys
from datetime import date

def PrintCityTemperature(city):

    url = "http://api.weatherapi.com/v1/current.json"
    
    params = {
        "key": "c2db1992773e44cbac2175611251806",
        "q": city
    }
    
    response = requests.get(url, params=params)
    
    data = response.json()

    if 'error' in data:

        raise Exception(data['error']['message'])

    today = date.today()

    formatted_date = today.strftime("%Y/%d/%m/")

    print(f"Current temperature in {city} on {formatted_date}: {data['current']['temp_c']}C")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: missing arguments")
        sys.exit(1)

    cityInput = sys.argv[1]

    PrintCityTemperature(cityInput)
    
