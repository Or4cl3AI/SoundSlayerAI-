```python
import music_player
import song_search
import vocal_remover
import chatbot
import playlist

def main():
    while True:
        command = input("Enter command: ")
        if command.startswith("play"):
            index = int(command.split(" ")[1])
            music_player.play(index)
        elif command.startswith("search"):
            song_name = command.split(" ", 1)[1]
            song_search.search(song_name)
        elif command.startswith("vocals"):
            song_path = command.split(" ", 1)[1]
            vocal_remover.vocals(song_path)
        elif command.startswith("What are the lyrics to"):
            song_name = command.split(" ", 5)[5]
            chatbot.get_lyrics(song_name)
        elif command == "quit":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
```