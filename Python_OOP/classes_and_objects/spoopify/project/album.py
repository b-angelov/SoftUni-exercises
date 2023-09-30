from project.song import Song


class Album:

    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song = [song for song in self.songs if song.name == song_name]
        if not song:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        song = song[0]
        self.songs.remove(song)
        return f"Removed song {song.name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs = '\n'.join(f"== {song.get_info()}" for song in self.songs)
        return f"""Album {self.name}
{songs}\n"""

