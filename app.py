import os
from flask import Flask, request, jsonify, render_template # type: ignore
import requests # type: ignore
from datetime import datetime, timedelta
import pytz # type: ignore
import json
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

API_KEY = "59b7ef44b63ae2fe52bd9715c8a54f3d"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

# Load city names from a JSON file
with open('city_list.json', 'r') as f:
    CITIES = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')  # Remove OPENWEATHERMAP_API_KEY parameter

@app.route('/weather', methods=['GET'])
def get_weather():
    app.logger.debug(f"Received request with args: {request.args}")
    city = request.args.get('city')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if city:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
    elif lat and lon:
        params = {
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'units': 'metric'
        }
    else:
        return jsonify({"error": "City or coordinates are required"}), 400

    try:
        response = requests.get(WEATHER_URL, params=params)
        app.logger.debug(f"API response status code: {response.status_code}")
        app.logger.debug(f"API response content: {response.text}")
        response.raise_for_status()
        
        data = response.json()
        
        # Get timezone offset in seconds
        timezone_offset = data['timezone']
        
        # Calculate current time in the city
        city_time = datetime.utcnow().replace(tzinfo=pytz.UTC) + timedelta(seconds=timezone_offset)
        
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'current_time': city_time.strftime('%Y-%m-%d %H:%M:%S'),
        }
        return jsonify(weather)
    except requests.RequestException as e:
        app.logger.error(f"Error fetching weather data: {str(e)}")
        return jsonify({"error": f"Unable to fetch weather data: {str(e)}"}), 500

@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('q', '').lower()
    suggestions = [city for city in CITIES if query in city.lower()]
    return jsonify(suggestions[:5])  # Return top 5 suggestions

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)