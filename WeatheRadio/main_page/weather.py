import urllib.request
import json
from datetime import datetime


def get_city_weather(lat, lon):


    current_month = datetime.now().month

    if(current_month >= 1 and current_month < 3 or current_month >= 12):
        season = "Winter"
    elif(current_month >=3 and current_month < 6):
        season = "Spring"
    elif(current_month >= 6 and current_month < 9):
        season = "Summer"
    else:
        season = "Autumn"



    api_key = "ff3262a9295b14ffe11569d5c9d32caa"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    main_url = base_url+"lat="+str(lat)+"&lon="+str(lon)+"&appid="+api_key

    try:
        JSONdata = urllib.request.urlopen(main_url).read()
        basic_desc = str(json.loads(JSONdata)["weather"][0]["main"])
    except:
        print("error!!")
        basic_desc="clear"

    
    current_hour = datetime.now().hour

    if(current_hour >=20 or current_hour < 5):
        day_status = "Night"
    elif(current_hour >=5 and current_hour < 12):
        day_status = "Morning"
    elif(current_hour >=12 and current_hour < 17):
        day_status = "Noon"
    else:
        day_status = "Evening"

    full_data_list = [season, basic_desc, day_status]
    return [season, basic_desc, day_status]



def getCoords():
    API_KEY = "0f95f695eedd4451882d0c3f69658bcb"
    geolocURL = "https://api.ipgeolocation.io/ipgeo?apiKey="+API_KEY
    try:
        JSONdata = urllib.request.urlopen(geolocURL).read()
        lat, lon = str(json.loads(JSONdata)["latitude"]), str(json.loads(JSONdata)["longitude"])
    except:
        print("error")
        lat, lon = "59.909", "10.744" 
    return [lat, lon]