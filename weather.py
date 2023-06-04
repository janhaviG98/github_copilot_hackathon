#Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python.
#Usage: python weather.py <city_name>
#Example: python weather.py "New York"
#make this app into commandline tool in a separate file keep this file as it is

# import required modules
import requests
import streamlit as st
import requests
import json
import sys
import pandas as pd
import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap

#take input for streamlit  

#API key
api_key = "6d7682b743121e3257d5c447616ccc44"


#Base url

base_url = "http://api.openweathermap.org/data/2.5/weather?"

#City name
city_name = st.text_input("Enter city name : ")
#create submit button to fetch data from api
if st.button("Submit"):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    #Get method of requests module
    #return response object
    response = requests.get(complete_url)

    #json method of response object
    #convert json format data into python format data
    x = response.json()
    print(x)
    #Now x contains list of nested dictionaries
    #Check the value of "cod" key is equal to "404", means city is found otherwise city is not found
    if x["cod"] != "404":
        
            #store the value of "main" key in variable y
            y = x["main"]
        
            #store the value corresponding to the "temp" key of y
            current_temperature = y["temp"]
            # convert current_temperature to celcius
            current_temperature = current_temperature - 273.15
        
            #store the value corresponding to the "pressure" key of y
            current_pressure = y["pressure"]
        
            #store the value corresponding to the "humidity" key of y
            current_humidity = y["humidity"]
        
            #store the value of "weather" key in variable z
            z = x["weather"]
        
            #store the value corresponding to the "description" key at the 0th index of z
            weather_description = z[0]["description"]
        

            # create a stream lit table to display the above data. give the table a title "Weather in {city_name}".
            st.title(f"Weather in {city_name}")
            df = pd.DataFrame({"Temperature": [current_temperature], "Pressure": [current_pressure], "Humidity": [current_humidity], "Description": [weather_description]})
            #remove first column of the table
            st.table(df.style.hide_index())
        

                #create a map to display the location of the city. use st.map() function to display the map.
                #st.map() function takes a list of latitudes and longitudes as input.
                #use the latitude and longitude values from the API response to create the map.
        

            coord = x["coord"]
            LAT = coord["lat"]
            LON = coord["lon"]
            #convert LAT and LON to a numeric value
            LAT = float(LAT)
            LON = float(LON)
            #create a dataframe with columns as LAT and LON
            df1 = pd.DataFrame(columns=['lat', 'lon'])
            #append the values of LAT and LON to the dataframe
            df1 = df1.append({'lat': LAT, 'lon': LON}, ignore_index=True)
            st.map(df1)
           
           

    else:
        st.write("City Not Found")


