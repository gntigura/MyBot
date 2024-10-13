import requests

# Helper function to get weather data
def get_weather(country):
    try:
        # Make a request to OpenWeatherMap API for weather data
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={country}&appid=16aa67d9404a8fde7d88deaa8b2b11ed&units=metric"
        weather_response = requests.get(weather_url).json()
        
        if weather_response['cod'] != 200:
            return None, f"Weather data not found for {country}."

        # Extract relevant weather information
        temperature = weather_response['main']['temp']
        description = weather_response['weather'][0]['description']
        latitude = weather_response['coord']['lat']
        longitude = weather_response['coord']['lon']
        
        # Return weather data and coordinates for time zone lookup
        return {
            'temperature': temperature,
            'description': description,
            'latitude': latitude,
            'longitude': longitude
        }, None
    except Exception as e:
        return None, str(e)

# Helper function to get time zone data
def get_timezone(latitude, longitude):
    try:
        # Make a request to TimeZoneDB API for time zone data
        timezone_url = f"http://api.timezonedb.com/v2.1/get-time-zone?key={TIMEZONEDB_API_KEY}&format=json&by=position&lat={latitude}&lng={longitude}"
        timezone_response = requests.get(timezone_url).json()
        
        if timezone_response['status'] != "OK":
            return None, "Time zone data not found."

        # Extract relevant time zone information
        timezone = timezone_response['zoneName']
        country_time = timezone_response['formatted']
        
        return {
            'timezone': timezone,
            'country_time': country_time
        }, None
    except Exception as e:
        return None, str(e)