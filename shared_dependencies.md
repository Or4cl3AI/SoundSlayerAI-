Shared Dependencies:

1. Python 3: All the files are written in Python and require Python 3 to run.

2. mpg123: This is a dependency used for playing mp3 files. It is used in "main.py" and "music_player.py".

3. requests: This library is used to make HTTP requests. It is used in "song_search.py" and "lyrics_finder.py" to fetch song data and lyrics respectively.

4. ffmpeg: This library is used for audio processing. It is used in "vocal_remover.py" to remove vocals from songs.

5. Function Names: 
   - "play(index)": Used in "main.py" and "music_player.py" to play a song.
   - "search(song_name)": Used in "main.py" and "song_search.py" to search for a song.
   - "vocals(song_path)": Used in "main.py" and "vocal_remover.py" to remove vocals from a song.
   - "quit()": Used in "main.py" to quit the app.
   - "get_lyrics(song_name)": Used in "chatbot.py" and "lyrics_finder.py" to fetch song lyrics.

6. Data Schemas: 
   - Song: A data schema representing a song. It is used in "song_search.py", "music_player.py", "playlist.py", and "vocal_remover.py".
   - Playlist: A data schema representing a playlist. It is used in "playlist.py" and "music_player.py".

7. Message Names: 
   - "song_search_result": A message sent from "song_search.py" to "main.py" containing the search results.
   - "lyrics_result": A message sent from "lyrics_finder.py" to "chatbot.py" containing the lyrics of a song.

8. Exported Variables: 
   - "current_song": A variable in "music_player.py" that is exported to "main.py" to keep track of the currently playing song.
   - "current_playlist": A variable in "playlist.py" that is exported to "main.py" and "music_player.py" to keep track of the current playlist.