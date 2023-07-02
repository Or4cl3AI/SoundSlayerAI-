```python
import requests
from lyrics_finder import get_lyrics

class Chatbot:
    def __init__(self):
        self.commands = {
            "lyrics": self.get_song_lyrics,
        }

    def handle_command(self, user_input):
        command = user_input.split()[0]
        if command in self.commands:
            self.commands[command](user_input[len(command):].strip())
        else:
            print("Sorry, I didn't understand that command.")

    def get_song_lyrics(self, song_name):
        lyrics = get_lyrics(song_name)
        if lyrics:
            print(lyrics)
        else:
            print("Sorry, I couldn't find the lyrics for that song.")

if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        user_input = input("Enter a command: ")
        if user_input == "quit":
            break
        chatbot.handle_command(user_input)
```