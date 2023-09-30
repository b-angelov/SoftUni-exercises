from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers  = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []


    def add_customer(self, customer: Customer):
        self.add_to_list(self.customers, customer)


    def add_trainer(self, trainer: Trainer):
        self.add_to_list(self.trainers, trainer)



    def add_equipment(self, equipment: Equipment):
        self.add_to_list(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add_to_list(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        self.add_to_list(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        i = subscription_id - 1
        return '\n'.join(str(info) for info in (self.subscriptions[i],self.customers[i],self.trainers[i],self.equipment[i],self.plans[i]))

    @staticmethod
    def add_to_list(list_: list, object_: object):
        if object_ not in list_:
            list_.append(object_)