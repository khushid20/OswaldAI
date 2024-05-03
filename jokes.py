import requests

def joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data['type'] == 'single':
            return data['joke'], ""
        elif response.status_code == 200 and data['type'] == 'twopart':
            return data['setup'], data['delivery']
        else:
            return "No joke found", ""
    except Exception as e:
        print("Error fetching joke:", e)
        return "Error fetching joke", ""
