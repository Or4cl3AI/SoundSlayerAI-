import requests
import json

def get_lyrics(song_name):
    base_url = "https://api.lyrics.ovh/v1/"
    complete_url = base_url + song_name
    response = requests.get(complete_url)
    data = response.json()

    if 'lyrics' in data:
        return data['lyrics']
    else:
        return "Lyrics not found for this song."

if __name__ == "__main__":
    song_name = input("Enter the song name: ")
    print(get_lyrics(song_name))
