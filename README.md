# Flask Weather Application

This is a Dockerized Flask application that allows users to enter the name of any city and get the current day's weather information. The application uses the OpenWeatherMap API to fetch weather data.

## Features

- **City Input**: A text input field for entering the city name.
- **Submit Button**: A button to submit the city name and fetch the weather information.
- **Weather Display**: Shows the current temperature, weather conditions (e.g., clear, cloudy, rainy), and other relevant information.

## Project Structure
 ├── app.py ├── Dockerfile ├── requirements.txt ├── templates │ └── index.html ├── static │ └── styles.css ├── tests │ └── test_app.py └── docker-compose.yml

 
## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Build the Docker image:
```docker-compose build```
3. Run the Docker container:
```docker-compose up```

The application should now be running at http://localhost:5000.

Running Unit Tests
To run the unit tests, use the following command:
```docker-compose run app pytest tests```

Dockerfile
```bash
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python3", "app.py"]
```

docker-compose.yml
```bash
version: '3.8'

services:
  app:
    build: .
    command: python3 app.py
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - PYTHONPATH=/app
```

Usage
Navigate to the application: Open your web browser and go to http://localhost:5000.
Enter a city name: Type the name of a city into the input field and click the "Get Weather" button.
View the weather information: The current weather information for the entered city will be displayed.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
OpenWeatherMap API for providing the weather data.
Flask for the web framework.
Docker for containerization.
