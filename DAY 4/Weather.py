import customtkinter as ctk
import requests
from datetime import datetime

# ---------------- APP SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Weather Dashboard")
app.geometry("500x700")
app.resizable(False, False)

# ---------------- WEATHER FUNCTION ---------------- #

def get_weather():

    city = city_entry.get()

    api_key = "YOUR_API_KEY"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:

        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) != "200":
            condition_label.configure(text="City Not Found")
            return

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        description = data["weather"][0]["description"]
        country = data["sys"]["country"]

        current_time = datetime.now().strftime("%d %b %Y | %I:%M %p")

        # Dynamic Weather Icons

        if "cloud" in description.lower():
            icon_label.configure(text="☁️")

        elif "rain" in description.lower():
            icon_label.configure(text="🌧️")

        elif "clear" in description.lower():
            icon_label.configure(text="☀️")

        elif "snow" in description.lower():
            icon_label.configure(text="❄️")

        elif "thunder" in description.lower():
            icon_label.configure(text="⛈️")

        else:
            icon_label.configure(text="🌤️")

        temp_label.configure(text=f"{temp}°C")
        condition_label.configure(text=description.title())

        city_label.configure(
            text=f"{city.title()}, {country}"
        )

        date_label.configure(
            text=current_time
        )

        feels_like_label.configure(
            text=f"Feels Like: {feels_like}°C"
        )

        humidity_label.configure(
            text=f"💧 Humidity\n{humidity}%"
        )

        wind_label.configure(
            text=f"🌬 Wind\n{wind} km/h"
        )

        pressure_label.configure(
            text=f"📊 Pressure\n{pressure} hPa"
        )

    except Exception as e:
        print("ERROR:", e)
        condition_label.configure(text="Error Fetching Data")

# ---------------- TITLE ---------------- #

title = ctk.CTkLabel(
    app,
    text="🌤 Weather Dashboard",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

# ---------------- SEARCH BAR ---------------- #

search_frame = ctk.CTkFrame(app)
search_frame.pack(pady=10, padx=20, fill="x")

city_entry = ctk.CTkEntry(
    search_frame,
    placeholder_text="Enter City Name",
    width=300,
    height=40
)
city_entry.pack(side="left", padx=10, pady=10)

city_entry.bind(
    "<Return>",
    lambda event: get_weather()
)

search_btn = ctk.CTkButton(
    search_frame,
    text="Search",
    command=get_weather,
    width=120,
    height=40
)
search_btn.pack(side="right", padx=10)

# ---------------- WEATHER CARD ---------------- #

weather_card = ctk.CTkFrame(
    app,
    corner_radius=20
)
weather_card.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

# Weather Icon

icon_label = ctk.CTkLabel(
    weather_card,
    text="🌤️",
    font=("Arial", 70)
)
icon_label.pack(pady=(20, 10))

# Temperature

temp_label = ctk.CTkLabel(
    weather_card,
    text="--°C",
    font=("Arial", 50, "bold")
)
temp_label.pack()

# Weather Description

condition_label = ctk.CTkLabel(
    weather_card,
    text="Weather Condition",
    font=("Arial", 22)
)
condition_label.pack(pady=10)

# City Name

city_label = ctk.CTkLabel(
    weather_card,
    text="City Name",
    font=("Arial", 18)
)
city_label.pack()

# Date & Time

date_label = ctk.CTkLabel(
    weather_card,
    text="",
    font=("Arial", 14)
)
date_label.pack(pady=5)

# Feels Like

feels_like_label = ctk.CTkLabel(
    weather_card,
    text="Feels Like: --°C",
    font=("Arial", 16)
)
feels_like_label.pack(pady=5)

# ---------------- DETAILS ---------------- #

details_frame = ctk.CTkFrame(weather_card)
details_frame.pack(pady=30)

humidity_label = ctk.CTkLabel(
    details_frame,
    text="💧 Humidity\n--%"
)
humidity_label.grid(row=0, column=0, padx=20, pady=20)

wind_label = ctk.CTkLabel(
    details_frame,
    text="🌬 Wind\n-- km/h"
)
wind_label.grid(row=0, column=1, padx=20, pady=20)

pressure_label = ctk.CTkLabel(
    details_frame,
    text="📊 Pressure\n-- hPa"
)
pressure_label.grid(row=0, column=2, padx=20, pady=20)

# ---------------- RUN APP ---------------- #

app.mainloop()