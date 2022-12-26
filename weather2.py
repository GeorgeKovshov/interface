from tkinter import *
#from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Main window")
root.geometry("400x50")#change window size

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=29A707AF-5222-4FFF-B1CA-87C3745BF84B")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "#0C0"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff9900"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very Unhealthy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = "#660000"
    root.configure(background=weather_color)
    myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                    background=weather_color)
    myLabel.pack()
except Exception as e:
    api = "Error..."

#myLabel = Label(root, text=api[0]['ReportingArea'] + " is " + api[0]['Category']['Name'])


mainloop()