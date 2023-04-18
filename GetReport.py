import requests
import json
import dotenv
import os

try:
    dotenv.load_dotenv()
    TOKEN = os.getenv("TOKEN")
except FileNotFoundError:
    print("No .env file found")

# GetWordstatReport (WORKS)
link = "https://api.direct.yandex.ru/v4/json/"
params = {
   "method": "GetWordstatReport",
    # Report ID
   "param": 1359201119,
   "token": TOKEN
}

r = requests.post(link, json.dumps(params, ensure_ascii=False).encode('utf8'))
print(r.json())
# assume that you already have an 'r' object that contains the JSON response
response_dict = r.json()
# save the response as a JSON-formatted string to a text file
with open('response.txt', 'w', encoding='utf-8') as f:
    json.dump(response_dict, f, ensure_ascii=False)