# 🌤Weather Dashboard

A modern weather application built using **Python**, **CustomTkinter**, and the **OpenWeatherMap API**. The application allows users to search for a city and instantly view real-time weather information through an interactive graphical interface.

---

## Project Overview

This project was created to practice working with:

- APIs
- GUI development
- JSON data handling
- Event-driven programming
- Error handling

The application fetches live weather data from the OpenWeatherMap API and displays it in a clean dashboard interface.

---

## Features

- Search weather by city name
- Real-time weather updates
- Dynamic weather icons
- Displays current temperature
- Displays "Feels Like" temperature
- Shows weather condition description
- Shows humidity percentage
- Shows wind speed
- Shows atmospheric pressure
- Displays country code
- Displays current date and time
- Search using Enter key or Search button
- Handles invalid city names gracefully

---

## Technologies Used

- Python
- CustomTkinter
- Requests Library
- OpenWeatherMap API

---

## Functions & Concepts Used

### `get_weather()`

The main function of the application.

Responsibilities:

- Reads city name entered by the user
- Sends a request to the OpenWeatherMap API
- Receives weather data in JSON format
- Extracts required weather information
- Updates the GUI dynamically
- Handles errors when a city is not found

---

### `requests.get()`

Used to send an HTTP request to the weather API.

Example:

```python
response = requests.get(url)
```

This retrieves live weather data from the internet.

---

### `.json()`

Converts API response into a Python dictionary.

```python
data = response.json()
```

This allows easy access to weather details.

---

### `.configure()`

Updates GUI elements dynamically.

Example:

```python
temp_label.configure(text=f"{temp}°C")
```

Used to display live weather information without restarting the application.

---

### `bind()`

Allows the Enter key to trigger a weather search.

Example:

```python
city_entry.bind("<Return>", lambda event: get_weather())
```

Improves user experience.

---

### Exception Handling

Used to prevent the application from crashing.

Example:

```python
try:
    ...
except Exception:
    ...
```

Handles network errors and invalid responses safely.

---

## Weather Information Retrieved

The application fetches:

- Temperature
- Feels Like Temperature
- Humidity
- Wind Speed
- Pressure
- Weather Description
- Country Information

---

## Learning Outcomes

Through this project, I learned:

- How APIs work
- Making HTTP requests in Python
- Parsing JSON responses
- Building GUI applications
- Handling user input
- Event-driven programming
- Error handling and debugging
- Working with external libraries
- Creating real-world Python projects

---
