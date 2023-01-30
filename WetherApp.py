import requests, datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

API_key = "Your_API_Key" # From: https://home.openweathermap.org/api_keys
Colour = ["#ae74c9", "#d99f2f", "#2d8c94", "#2d7194", "#c97a33", "#2e2a44", "#454549"]

currentDT = datetime.datetime.now()
Hour = (currentDT.hour)
#print(Hour)

if Hour >= 0 and Hour < 5:
    BgColour = Colour[6]
elif Hour >= 5 and Hour < 7:
    BgColour = Colour[0]
elif Hour >= 7 and Hour < 8:
    BgColour = Colour[1]
elif Hour >= 8 and Hour < 13:
    BgColour = Colour[2]
elif Hour >= 13 and Hour < 16:
    BgColour = Colour[3]
elif Hour >= 16 and Hour < 18:
    BgColour = Colour[4]
elif Hour >= 18 and Hour < 21:
    BgColour = Colour[5]
elif Hour >= 21 and Hour < 24:
    BgColour = Colour[6]

root = tk.Tk()
root.geometry("1200x700")
root.configure(bg=BgColour)
root.resizable(False, False)
root.title("Weather App")

def Search(Loc):
    GeoQuery = f"http://api.openweathermap.org/geo/1.0/direct?q={Loc}&limit={1}&appid={API_key}"
    GeoRespone = requests.get(GeoQuery).json()
    Lat, Lon = GeoRespone[0]["lat"], GeoRespone[0]["lon"]
    query = f"https://api.openweathermap.org/data/3.0/onecall?lat={Lat}&lon={Lon}&appid={API_key}&units=metric"
    print(query)
    print(GeoQuery)
    respone = requests.get(query).json()

    Respone = {"Thunderstorm" : "balck", 
                "Drizzle" : "#8bb4c9", 
                "Rain" : "#a1b7c2", 
                "Snow" : "#afd9ee", 
                "Clear" : "#f7f891", 
                "Clouds" : "#747575"
                }

    Current_Weather = respone["current"]["temp"]
    Feels_Like = respone["current"]["feels_like"]
    Min_Temp = respone["daily"][0]["temp"]["min"]
    Max_Temp = respone["daily"][0]["temp"]["max"]
    Icon = respone["current"]["weather"][0]["icon"]
    Weather = respone["current"]["weather"][0]["main"]
    city = GeoRespone[0]["name"]
    country = GeoRespone[0]["country"]
    Sunrise = datetime.datetime.utcfromtimestamp(respone["daily"][0]["sunrise"]).strftime("%H:%M")
    Sunset = datetime.datetime.utcfromtimestamp(respone["daily"][0]["sunset"]).strftime("%H:%M")
    UVI = respone["current"]["uvi"]
    Humidity = respone["current"]["humidity"]
    Wind = respone["current"]["wind_speed"]

    InfoLayoutIMG = PhotoImage(file=f"Assets/{Weather}.png")
    Label(image=InfoLayoutIMG, bg=BgColour, text=Weather).pack()

    Weather_Icon = PhotoImage(file=f"WeatherIcons/{Icon}.png")
    Label(image=Weather_Icon, background=Respone[Weather], ).place(x=440, y=140)

    Label(root, text=f"{Weather}", font=("Myriad Pro", 40), background=Respone[Weather]).place(x=70, y=150)
    current_Weather = tk.Label(root, text=f"{round(Current_Weather)}°C", font=("Myriad Pro", 45), background=Respone[Weather]).place(x=70, y=245)
    FeelsLike = tk.Label(root, text=f"{round(Max_Temp)}° / {round(Min_Temp)}° Feels like {round(Feels_Like)}°C", font=("Myriad Pro", 30), background=Respone[Weather]).place(x=70, y=345)
    tk.Label(root, text=f"{city},{country}", font=("Myriad Pro", 30), background=Respone[Weather]).place(x=70, y=420)

    SunRiseIMG = PhotoImage(file="WeatherIcons/Sunrise.png")
    Label(image=SunRiseIMG, background=Respone[Weather]).place(x=840, y=220)
    Label(root, text=f"{Sunrise}", font=("Myriad Pro", 35), background=Respone[Weather]).place(x=825, y=150)

    SunSetIMG = PhotoImage(file="WeatherIcons/Sunset.png")
    Label(image=SunSetIMG, background=Respone[Weather]).place(x=1030, y=220)
    Label(root, text=f"{Sunset}", font=("Myriad Pro", 35), background=Respone[Weather]).place(x=1015, y=150)

    #3 Extra Info
    UVIndexIMG = PhotoImage(file="WeatherIcons/UVIndex.png")
    Label(image=UVIndexIMG, background=Respone[Weather]).place(x=825, y=360)
    Label(root, text="UV Index", font=("Myriad Pro", 15), background=Respone[Weather]).place(x=825, y=450)

    Label(root, text=f"{2}", font=("Myriad Pro", 15), background=Respone[Weather]).place(x=855, y=485)

    HumidityIMG = PhotoImage(file="WeatherIcons/Humidity.png")
    Label(image=HumidityIMG, background=Respone[Weather]).place(x=942, y=360)
    Label(root, text="Humidity", font=("Myriad Pro", 15), background=Respone[Weather]).place(x=950, y=450)

    Label(root, text=f"{Humidity}%", font=("Myriad Pro", 15), background=Respone[Weather]).place(x=965, y=485)

    WindIMG = PhotoImage(file="WeatherIcons/Wind2.png")
    Label(image=WindIMG, background=Respone[Weather]).place(x=1060, y=360)
    Label(root, text="Wind", font=("Myriad Pro", 15), background=Respone[Weather]).place(x=1075, y=450)

    Label(root, text=f"{round((Wind)*2.237)}mph", font=("Myriad Pro", 15), background=Respone[Weather]).place(x=1075, y=485)


    root.mainloop()

def Get_Value():
    Location = Search_Entry.get()
    Search(Location)

def Layout():
    global Search_Entry

    Search_Bar = PhotoImage(file="Assets/search_bar.png")
    Label(root, image=Search_Bar, bg=BgColour).place(x=800, y=10)

    Search_Entry = StringVar()
    searchEntry = Entry(root, textvariable=Search_Entry, font="arial 30", bg=BgColour, fg="#000", bd=0, width=14).place(x=825, y=17.5)

    Search_img = PhotoImage(file="Assets/SearchIcon.png")
    button = Button(root, image=Search_img, command=Get_Value, borderwidth=0, bg=BgColour, activebackground=BgColour).place(x=1137, y=20)

    mainloop()


Layout()