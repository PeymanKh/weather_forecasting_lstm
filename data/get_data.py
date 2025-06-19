"""
This script use https://open-meteo.com open-source API to get weather data
and save it as csv. Note that any time you run this script, it calculates the
last 10 year and the data will be up to date.

Author: Peyman Kh
Date: 19-06-2025
"""
# Import libraries
from datetime import datetime, timedelta
from meteostat import Point, Daily

# Define Istanbul coordinates
istanbul = Point(41.0082, 28.9784)

# Define time range: from 10 years ago to yesterday
end = datetime.today() - timedelta(days=1)
start = end - timedelta(days=365 * 10)

# Fetch daily weather data
data = Daily(istanbul, start, end)
data = data.fetch()

# Save to CSV
data.to_csv("istanbul_weather_last_10_years.csv")

print("Data saved:", data.shape, "rows")
