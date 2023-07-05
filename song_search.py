import requests
import json

class Song:
    def __init__(self, title, artist, url):
        self.title = title
        self.artist = artist
        self.url = url

def search(song_name):
    base_url = "https://api.songsearch.com/search"
    params = {"q": song_name}
    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    songs = []
    for item in data['results']:
        title = item['title']
        artist = item['artist']
        url = item['url']
        song = Song(title, artist, url)
        songs.append(song)

    return songs
