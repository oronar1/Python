import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from bs4 import BeautifulSoup

client_ID = "Your client ID"
client_secret = "Your client ID"
playlist_ID = "Your Playlist ID"
date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")
URL_REDIRECT = "http://example.com"
URL = f"https://www.billboard.com/charts/hot-100/{date}"


def remove_values_from_list(list, val):
    return [value for value in list if value != val]


response = requests.get(URL)
top100_html = response.text

soup = BeautifulSoup(top100_html, "html.parser")

top100_songs = soup.find_all(name="h3", class_="u-letter-spacing-0021", id="title-of-a-story")
top100_artists = soup.find_all(name="span", class_="u-letter-spacing-0021")
top100_songs = [title.text.strip() for title in top100_songs]
top100_artists = [title.text.strip() for title in top100_artists]
top100_songs = remove_values_from_list(top100_songs, 'Songwriter(s):')
top100_songs = remove_values_from_list(top100_songs, 'Producer(s):')
top100_songs = remove_values_from_list(top100_songs, 'Imprint/Promotion Label:')


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_ID,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username='Your Spotify username',
    )
)
user_id = sp.current_user()['id']

song_uris = []
year = date.split("-")[0]
print("Adding songs to buffer... ")
for song in top100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify. Skipped")
print("Finished to build the list of songs.\n")

playlist_ID = sp.user_playlist_create(user_id,
                                   f"{date} Billboard 100",
                                   public=False,
                                   collaborative=False,
                                   description=f"Top 100 songs for {date}")["id"]


sp.playlist_add_items(playlist_ID,
                          song_uris,
                          position=None)
