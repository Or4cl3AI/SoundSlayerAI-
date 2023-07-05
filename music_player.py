import os
import mpg123

from playlist import current_playlist

current_song = None

def play(index):
    global current_song
    try:
        song = current_playlist[index]
        current_song = song
        player = mpg123.MPG123(song.path)
        player.play()
    except IndexError:
        print("Invalid index. Please try again.")

def stop():
    global current_song
    if current_song:
        player = mpg123.MPG123(current_song.path)
        player.stop()
        current_song = None

def pause():
    global current_song
    if current_song:
        player = mpg123.MPG123(current_song.path)
        player.pause()

def resume():
    global current_song
    if current_song:
        player = mpg123.MPG123(current_song.path)
        player.resume()

def next_song():
    global current_song
    if current_song:
        current_index = current_playlist.index(current_song)
        next_index = (current_index + 1) % len(current_playlist)
        play(next_index)

def previous_song():
    global current_song
    if current_song:
        current_index = current_playlist.index(current_song)
        prev_index = (current_index - 1) % len(current_playlist)
        play(prev_index)
