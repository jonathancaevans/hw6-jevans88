import requests
import os
import base64
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

token_url = "https://accounts.spotify.com/api/token"

id = os.getenv("CLIENT_ID")
key = os.getenv("CLIENT_SECRET")

credentials = f"{id}:{key}"
credentials = base64.b64encode(credentials.encode())

data = {
	"grant_type":"client_credentials"
}

headers = {
	"Authorization": f"Basic {credentials.decode()}"
}

response = requests.post(url=token_url, data=data, headers=headers)

base_url = "https://api.spotify.com/v1/browse/new-releases"
access_token = response.json()['access_token']

params = {
     "limit": "10"
}

headers = {
     "Authorization": f"Bearer {access_token}"
}

response = requests.get(
    base_url,
    params=params,
    headers=headers
)

try:
    newSongs = response.json()["albums"]["items"]
    for song in newSongs:
        print(song["name"])
except KeyError:
    print("Couldn't fetch albums!")
