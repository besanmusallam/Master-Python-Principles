# API : Application Programming Interface

"""
is a set of commands, functions, protocols, and objects
that programmers can use to create software or interact with
and external system.

your program  |API|  External System

API Request -> To get the data

response codes:
- 404 : does not exist
- 1XX : Hold on
- 2XX : Success (200)
- 3XX : you dont have access
- 4XX : smth is wrong (404)
- 5XX : Server Issue
"""

import requests
import datetime


# ISS API

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code != 200:
    raise Exception("Bad response from ISS API")

# equivilant to

response.raise_for_status()

##################

data = response.json()
print(data['iss_position']["longitude"])


## Sunset and Sunrise API
# check the API documentation
LATITUDE = 31.963158
LONGITUDE = 35.930359

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    # "formatted": 0   # off
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise)

time_now = datetime.datetime.now()

print(time_now)