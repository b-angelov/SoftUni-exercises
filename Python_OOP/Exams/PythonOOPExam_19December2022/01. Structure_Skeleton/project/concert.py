
class Concert:

    def __init__(self,genre:str,audience: int,ticket_price: float,expenses: float,place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    def __str__(self):
        return f"{self._genre} concert at {self._place}."

    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, genre: str):
        if genre not in ["Metal","Rock","Jazz"]:
            raise ValueError(f"Our group doesn't play {genre}!")
        self._genre = genre

    @property
    def audience(self):
        return self._audience
    @audience.setter
    def audience(self, audience: int):
        if audience < 1:
            raise ValueError("At least one person should attend the concert!")
        self._audience = audience

    @property
    def ticket_price(self):
        return self._ticket_price
    @ticket_price.setter
    def ticket_price(self, price: float):
        if price < 1:
            raise ValueError("Ticket price must be at least 1.00$!")
        self._ticket_price = price

    @property
    def expenses(self):
        return self._expenses
    @expenses.setter
    def expenses(self, expenses: float):
        if expenses < 0:
            raise ValueError("Expenses cannot be a negative number!")
        self._expenses = expenses

    @property
    def place(self):
        return self._place
    @place.setter
    def place(self,place: str):
        if len(place.strip()) < 2:
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")
        self._place = place

