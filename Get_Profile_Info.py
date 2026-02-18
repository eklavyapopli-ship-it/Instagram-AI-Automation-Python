import requests
from dotenv import load_dotenv
import os
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
url = "https://graph.instagram.com/v24.0"
resp = requests.get(f"{url}/me?fields=user_id,username,name,account_type,followers_count&access_token={ACCESS_TOKEN}")
print(resp.json())

# Response Format:
# {'user_id': 'ig_usid', 'username': 'ig_username', 'name': 'ID NAME', 'account_type': 'BUSINESS', 'followers_count': 34, 'id': 'instagram_id'}