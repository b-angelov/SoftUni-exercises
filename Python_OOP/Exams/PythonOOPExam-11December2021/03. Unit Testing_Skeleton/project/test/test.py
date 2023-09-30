from unittest import TestCase

from project.team import Team


class TestTeam(TestCase):

    def setUp(self):
        self.team = Team("MyTeam")

    def test_init(self):
        self.assertEqual(self.team.name, "MyTeam")
        self.assertEqual(self.team.members, {})

    def test_name_valid(self):
        self.team.name = "MyGreatTeam"
        self.assertEqual(self.team.name, "MyGreatTeam")

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.team.name = "1541"
        self.assertEqual(str(msg.exception), "Team Name can contain only letters!")
        with self.assertRaises(ValueError) as msg:
            self.team.name = "abaa11"
        self.assertEqual(str(msg.exception), "Team Name can contain only letters!")
        self.assertEqual(self.team.name, "MyTeam")

    def test_add_member(self):
        self.assertEqual(self.team.add_member(Peter=12,John=15,Stephan=5),f"Successfully added: Peter, John, Stephan")
        self.assertEqual(self.team.add_member(Peter=38),f"Successfully added: ")
        self.assertEqual(self.team.members,{"Peter":12,"John":15,"Stephan":5})

    def test_remove_member(self):
        self.team.add_member(Peter=12,John=15,Stephan=5)
        self.assertEqual(self.team.remove_member("John"), "Member John removed")
        self.assertEqual(self.team.remove_member("John"), "Member with name John does not exist")

    def test_gt(self):
        self.team.add_member(Peter=12, John=15, Stephan=5)
        opponent = Team("Those")
        opponent.add_member(Potter=12, Hermione=15, Ronald=5, Luna=11)
        self.assertEqual(self.team > opponent, False)
        self.team.add_member(Malfoy=12, Dudlee=15, Petunia=5)
        self.assertEqual(self.team > opponent, True)

    def test_len(self):
        self.team.add_member(Peter=12, John=15, Stephan=5)
        self.assertEqual(len(self.team), 3)

    def test_add(self):
        hogwarts = Team("Hogwarts")
        hogwarts.add_member(Potter=12, Hermione=15, Ronald=5, Luna=11)
        new_team = self.team + hogwarts
        self.assertEqual(new_team.name, "MyTeamHogwarts")
        self.assertEqual(new_team.members, dict(self.team.members, **hogwarts.members))

    def test_str(self):
        self.team.add_member(Potter=12, Hermione=15, Ronald=5, Luna=11)
        self.assertEqual(str(self.team), """Team name: MyTeam
Member: Hermione - 15-years old
Member: Potter - 12-years old
Member: Luna - 11-years old
Member: Ronald - 5-years old""")

