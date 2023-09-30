from math import ceil


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: [list] = [] #matrtix

    @property
    def photos(self):
        if not self.__photos:
            return [list() for _ in range( self.pages)]
        return self.__photos

    @photos.setter
    def photos(self, value):
        try:
            self.__photos
        except:
            self.__photos = []
        if value and (not len(self.__photos) or len(self.__photos[-1]) == 4):
            self.__photos.append([value])
        elif value and len(self.__photos[-1]) < 4:
            self.__photos[-1].append(value)

    @staticmethod
    def from_photos_count(photos_count: int):
        album = PhotoAlbum(ceil(photos_count / 4))
        return album

    def add_photo(self, label:str):
        if len(self.photos) == self.pages and all(len(page)==4 for page in self.photos):
            return "No more free slots"
        self.photos = label
        return f"{label} photo added successfully on page {len(self.photos)} slot {len(self.photos[-1])}"

    def display(self):
        return '\n'.join(("-"*11) + "\n" + ' '.join("[]" for _ in range(len(self.photos[page]) if page in range(len(self.photos)) else 0 )) for page in range(self.pages)) + f"\n{'-'*11}"


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



