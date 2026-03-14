import sys
import requests

def get_weather(city_name):
    # Using Open-Meteo Geocoding API to get coordinates
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    
    try:
        geo_response = requests.get(geocoding_url)
        geo_data = geo_response.json()
        
        if not geo_data.get("results"):
            print(f"City '{city_name}' not found.")
            return

        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        name = location["name"]
        country = location["country"]

        # Fetching weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        current_weather = weather_data["current_weather"]
        temperature = current_weather["temperature"]
        windspeed = current_weather["windspeed"]
        
        print(f"Weather in {name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Speed: {windspeed} km/h")

    except Exception as e:
        print(f"Error fetching weather data: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city_name>")
        return

    city_name = " ".join(sys.argv[1:])
    get_weather(city_name)

if __name__ == "__main__":
    main()
