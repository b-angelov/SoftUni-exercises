from project.album import Album

class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album = [album for album in self.albums if album_name == album.name]
        if not album:
            return f"Album {album_name} is not found."
        album = album[0]
        if album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        albums = '\n'.join(album.details() for album in self.albums)
        return f"""Band {self.name}
 {albums}"""
