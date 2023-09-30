class DVD:

    MONTHS = ",January,February,March,April,May,June,July,August,September,October,November,December".split(",")

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.is_rented = False
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction

    @staticmethod
    def from_date(id: int, name: str, date: str, age_restriction: int):
        date = list(map(int,date.split(".")))
        dvd = DVD(name, id, date[-1], DVD.MONTHS[date[1]], age_restriction)
        return dvd

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {('not ' if not self.is_rented else '')}rented"
