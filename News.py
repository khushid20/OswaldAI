import requests
from ss import *

api_address = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=" + key
json_data = requests.get(api_address).json()

ar = []

def news():
    if "articles" in json_data:
        for i in range(min(3, len(json_data["articles"]))):
            ar.append("Number " + str(i+1) + ": " + json_data["articles"][i]["title"] + ".")
    else:
        ar.append("No articles found.")
    return ar

# arr = news()
# print(arr)


# 8f150dcd3b1446a193b0d7d5da0f9d42