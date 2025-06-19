import requests

def PrintCityTemperature():
    
    city = input("Enter name of a city: ")

    url = "http://api.weatherapi.com/v1/current.json"
    
    params = {
        "key": "c2db1992773e44cbac2175611251806",
        "q": city
    }
    
    response = requests.get(url, params=params)
    
    data = response.json()

    if 'error' in data:

        raise Exception(data['error']['message'])

    print(data['current']['temp_c'])


PrintCityTemperature()
