import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.oauth2


SPOTIPY_CLIENT_ID = "c51f02461bad485fb5ac426545cb496a"
SPOTIPY_CLIENT_SECRET = "baa931c5d04a460196d634a46a499205"
SPOTIPY_REDIRECT_URI = "http://example.com"




# -----------SPOTIFY API Connect----------#


sp = spotipy.Spotify(auth_manager= SpotifyOAuth(scope="playlist-modify-private", client_id=SPOTIPY_CLIENT_ID,
                                 client_secret=SPOTIPY_CLIENT_SECRET,
                                 redirect_uri=SPOTIPY_REDIRECT_URI,
                                 show_dialog=True,
                                 cache_path="token.txt"
                                 )
                     )

user_id = sp.current_user()["id"]

#----------web scrap part---#

date_to_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date_to_travel}"

response = requests.get(URL)
HTML = response.text

soup = BeautifulSoup(HTML, "html.parser")
all_song_tags = soup.select("li #title-of-a-story")

songs = [song.getText().strip() for song in all_song_tags]
# print(songs)

song_uris =[]
year = date_to_travel.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")
playlist = sp.user_playlist_create(user=user_id, name=f"{date_to_travel} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)