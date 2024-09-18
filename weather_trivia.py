import requests # type: ignore

def get_weather_data(api_key, city):
    url = f"https://api.example.com/weather?city={city}&apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 500:
            print(f"500 Internal Server Error: The weather API is currently experiencing issues. Please try again later.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred while fetching weather data: {err}")
    return None

# Usage
weather_data = get_weather_data("your_api_key", "New York")
if weather_data:
    # Process the weather data
    pass
else:
    print("Unable to fetch weather data. Please try again later.")

# Make sure the function is defined and spelled correctly
def get_trivia():
    # Function implementation
    pass

# If it's supposed to be inside a class, make sure it's properly defined
class WeatherTrivia:
    def get_trivia(self):
        # Method implementation
        pass
