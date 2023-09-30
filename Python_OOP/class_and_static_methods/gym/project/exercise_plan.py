class ExercisePlan:

    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        """duration should be given in minutes"""
        self.id = ExercisePlan.id
        ExercisePlan.id += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

    @staticmethod
    def from_hours(trainer_id:int, equipment_id:int, hours:int):
        return ExercisePlan(trainer_id, equipment_id, hours * 60)

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"