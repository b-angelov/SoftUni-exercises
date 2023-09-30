from project.band_members.musician import Musician


class Guitarist(Musician):
    GUITARIST_AVAILABLE_SKILLS = (
        "play metal",
        "play rock",
        "play jazz",
    )

    def learn_new_skill(self, new_skill):
        if new_skill not in self.GUITARIST_AVAILABLE_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."
