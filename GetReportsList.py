import requests
import json
import dotenv
import os

try:
    dotenv.load_dotenv()
    TOKEN = os.getenv("TOKEN")
except FileNotFoundError:
    print("No .env file found")

# GetWordstatReportList (WORKS)
link = "https://api.direct.yandex.ru/v4/json/"
params = {
   "method": "GetWordstatReportList",
   "param": {},
   "token": TOKEN
}
r = requests.post(link, json.dumps(params, ensure_ascii=False).encode('utf8'))
print(r.json())