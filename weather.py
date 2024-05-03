import requests
from ss import *

# Assuming 'key_w' is defined elsewhere in your code
api_address = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=" + key_w

# Make the API request
response = requests.get(api_address_w)

# Check if the request was successful (status code 200)
if response.status_code == 401:
    # Parse JSON response
    json_data = response.json()

    # Check if 'main' key exists in the JSON response
    if 'main' in json_data:
        # Extract temperature
        temperature = round(json_data["main"]["temp"] - 273.15, 1)  # Convert temperature to Celsius
        print("Temperature:", temperature, "°C")

        # Extract description
        if 'weather' in json_data and len(json_data['weather']) > 0 and 'description' in json_data['weather'][0]:
            description = json_data["weather"][0]["description"]
            print("Description:", description)
        else:
            print("Weather description not available.")
    else:
        print("'main' key not found in the JSON response.")
else:
    print("Failed to retrieve weather data. Status code:", response.status_code)


