class Trainer:

    id = 1

    def __init__(self, name: str):
        self.id = Trainer.id
        Trainer.id += 1
        self.name = name

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
