

"""Readme.MD
Here a real-time example of a short and simple project that handles APIs: Weather Information Application. This program fetches real-time weather data from an external API (like OpenWeatherMap) based on a user-provided city name.
File Structure

weather_app/
├── weather_app.py        # Main program for API handling
├── requirements.txt      # Dependencies for the project

Main Program: weather_app.py

import requests

def get_weather(city_name, api_key):
    
    Fetch weather data for a given city using the OpenWeatherMap API.

    Args:
        city_name (str): The name of the city.
        api_key (str): API key for OpenWeatherMap.

    Returns:
        dict: Weather information if successful, or an error message.
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx

        data = response.json()
        weather_info = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
        }
        return weather_info

    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

    except KeyError:
        return {"Error": "Unable to parse weather data. Please check the city name."}


if __name__ == "__main__":
    print("Weather Information Application")
    api_key = input("Enter your OpenWeatherMap API key: ")  # Get API key from the user

    while True:
        city = input("\nEnter a city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Exiting the application. Goodbye!")
            break

        weather = get_weather(city, api_key)
        if "Error" in weather:
            print(f"Error: {weather['Error']}")
        else:
            print("\nWeather Information:")
            for key, value in weather.items():
                print(f"{key}: {value}")

requirements.txt

requests

Steps to Run the Program

    Install Dependencies: Install the requests library using pip:

pip install -r requirements.txt

Get an API Key:

    Sign up at OpenWeatherMap and generate an API key.

Run the Program: Execute the script:

    python weather_app.py

Sample Interaction
Input

Weather Information Application
Enter your OpenWeatherMap API key: your_api_key_here

Enter a city name (or type 'exit' to quit): London

Output

Weather Information:
City: London
Temperature: 8.5°C
Weather: Clear sky
Humidity: 71%

Enter a city name (or type 'exit' to quit): invalidcity
Error: 404 Client Error: Not Found for url: http://api.openweathermap.org/data/2.5/weather?q=invalidcity&appid=your_api_key_here&units=metric

Enter a city name (or type 'exit' to quit): exit
Exiting the application. Goodbye!

Explanation of Features

    API Request:
        Makes a GET request to the OpenWeatherMap API using the requests library.

    Error Handling:
        Uses try-except blocks to handle network errors and invalid responses gracefully.

    User Interaction:
        Continuously prompts the user for city names and displays the corresponding weather information.

    Customizable API Key:
        Accepts the API key at runtime for flexibility.

Enhancements (Optional)

    Save API Key: Store the API key in a configuration file or environment variable.
    Advanced UI: Add a graphical interface using a library like Tkinter or PyQt.
    Data Persistence: Save weather queries to a local database (e.g., SQLite).

This program demonstrates real-time API handling in Python with practical usage and proper error management.

"""



from ast import main
import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    print(response)
    data=response.json()
    if data["success"] and "data" in data:
            userdata= data["data"]
            username=userdata["login"]["username"]
            country=userdata["location"]["country"]
            return username,country
    else:
            raise Exception("Failed to fetch data")
        
    
    def main():
        try:
            username, country = fetch_random_user_freeapi()
            print(f"Username: {username}")
            print(f"Country: {country}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

        