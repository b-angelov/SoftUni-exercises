
class Band:

    def __init__(self, name: str):
        self.name = name
        self.members = []

    def __str__(self):
        return f"{self._name} with {len(self.members)} members."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name: str):
        if not name:
            raise ValueError("Band name should contain at least one character!")
        self._name = name
