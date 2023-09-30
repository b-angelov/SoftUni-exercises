class Shop:

    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items
        self.get_items_count = lambda: len(self)

    def __len__(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
