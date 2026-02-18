import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
url = 'https://graph.instagram.com/v24.0/me/messages'
payload = {
           "recipient":{
               "id":"IG_USID"
           },
           "message":{
              "text":"hey i am eklavya"
           }
        }


json_payload = json.dumps(payload)


headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",  'Content-Type': 'application/json'
}



response = requests.post(url, data=json_payload, headers=headers)

# Check the response
print(f"Status Code: {response.status_code}")
print("\nRAW TEXT:\n", response.text)


try:
    data = response.json()
    print("\nJSON:\n", json.dumps(data, ensure_ascii=False, indent=2))
except Exception as e:
    print("\nNot JSON:", e)


# To get the recipient user id, You have to first establish the webhook with Meta Developer Account using ngrok to expose your localhost url to the network