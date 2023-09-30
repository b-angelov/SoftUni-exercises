from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        enough_capacity = self.__animal_capacity >= len(self.animals) + 1
        enough_budget = self.__budget >= price
        if enough_budget and enough_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif enough_capacity and not enough_budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        remaining_workplaces = len(self.workers) < self.__workers_capacity
        if remaining_workplaces:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [worker for worker in self.workers if worker.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum(worker.salary for worker in self.workers)
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_expenses = sum(animal.money_for_care for animal in self.animals)
        if animals_expenses <= self.__budget:
            self.__budget -= animals_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_count = len(self.animals)
        animals = {}
        for animal in self.animals:
            animals.setdefault(animal.__class__.__name__,[])
            animals[animal.__class__.__name__].append(animal)
        animals_str = ""
        if "Lion" in animals.keys():
            animals_str += f"\n----- {len(animals['Lion'])} Lions:\n" +'\n'.join(str(animal) for animal in animals["Lion"])
        if "Tiger" in animals.keys():
            animals_str += f"\n----- {len(animals['Tiger'])} Tigers:\n" +'\n'.join(str(animal) for animal in animals["Tiger"])
        if "Cheetah" in animals.keys():
            animals_str += f"\n----- {len(animals['Cheetah'])} Cheetahs:\n" +'\n'.join(str(animal) for animal in animals["Cheetah"])
        return f"""You have {animals_count} animals{animals_str}"""


    def workers_status(self):
        workers_count = len(self.workers)
        workers = {}
        for worker in self.workers:
            workers.setdefault(worker.__class__.__name__, [])
            workers[worker.__class__.__name__].append(worker)
        workers_str = ""
        if "Keeper" in workers.keys():
            workers_str += f"\n----- {len(workers['Keeper'])} Keepers:\n" +'\n'.join(str(worker) for worker in workers["Keeper"])
        if "Caretaker" in workers.keys():
            workers_str += f"\n----- {len(workers['Caretaker'])} Caretakers:\n" +'\n'.join(str(worker) for worker in workers["Caretaker"])
        if "Vet" in workers.keys():
            workers_str += f"\n----- {len(workers['Vet'])} Vets:\n" +'\n'.join(str(worker) for worker in workers["Vet"])
        return f"You have {workers_count} workers{workers_str}"

