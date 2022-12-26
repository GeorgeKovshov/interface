from tkinter import *
#from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Main window")
root.geometry("400x50")#change window size
root.configure(background='green')

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=29A707AF-5222-4FFF-B1CA-87C3745BF84B")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."

#myLabel = Label(root, text=api[0]['ReportingArea'] + " is " + api[0]['Category']['Name'])
myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                background="green")
myLabel.pack()

mainloop()