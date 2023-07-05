class Song:
    def __init__(self, title, artist, path):
        self.title = title
        self.artist = artist
        self.path = path

class Playlist:
    def __init__(self):
        self.songs = []
        self.current_index = 0

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, index):
        if index < len(self.songs):
            del self.songs[index]

    def get_current_song(self):
        if self.songs:
            return self.songs[self.current_index]
        else:
            return None

    def next_song(self):
        if self.songs:
            self.current_index = (self.current_index + 1) % len(self.songs)
            return self.get_current_song()
        else:
            return None

    def previous_song(self):
        if self.songs:
            self.current_index = (self.current_index - 1) % len(self.songs)
            return self.get_current_song()
        else:
            return None

current_playlist = Playlist()
