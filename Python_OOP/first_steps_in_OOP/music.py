class Music:

    def __init__(self,*args: str):
        self.title,self.artist,self.lyrics = args

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

song = Music("Mabungu", "Mabongo", "\nMabun mabun, mabongo\n mabungu ba mabo\nmabu mabu mabango\n mabango mabo lo")
print(song.print_info())
print(song.play())
