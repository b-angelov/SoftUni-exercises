import unittest

# from project.student_report_card import StudentReportCard
from student_report_card import StudentReportCard



class TestStudentReportCard(unittest.TestCase):

    def setUp(self) -> None:
        self.card = StudentReportCard("Michael O'Conner", 11)

    def test_init(self):
        self.assertEqual(self.card.student_name, "Michael O'Conner")
        self.assertEqual(self.card.school_year, 11)
        self.assertEqual(self.card.grades_by_subject, {})

    def test_student_name_valid(self):
        self.assertEqual(self.card.student_name, "Michael O'Conner")
        self.card.student_name = "James O'Brian"
        self.assertEqual(self.card.student_name, "James O'Brian")

    def test_student_name_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.card.student_name = ''
        self.assertEqual(str(msg.exception), "Student Name cannot be an empty string!")
        self.assertEqual(self.card.student_name,"Michael O'Conner")

    def test_school_year_valid(self):
        self.assertEqual(self.card.school_year, 11)
        self.card.school_year = 1
        self.assertEqual(self.card.school_year, 1)
        self.card.school_year = 12
        self.assertEqual(self.card.school_year, 12)

    def test_school_year_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.card.school_year = 0
        self.assertEqual(str(msg.exception), "School Year must be between 1 and 12!")
        self.assertEqual(self.card.school_year,11)
        with self.assertRaises(ValueError) as msg:
            self.card.school_year = 13
        self.assertEqual(str(msg.exception), "School Year must be between 1 and 12!")
        self.assertEqual(self.card.school_year, 11)

    def test_add_grade(self):
        self.assertEqual(self.card.add_grade("Big Bang Theory", 2), None)
        self.assertIn("Big Bang Theory",self.card.grades_by_subject)
        self.assertIn(2,self.card.grades_by_subject["Big Bang Theory"])
        self.assertEqual(self.card.grades_by_subject, {"Big Bang Theory": [2]})
        self.assertEqual(self.card.add_grade("Other Theories", 3), None)
        self.assertEqual(self.card.add_grade("Other Theories", 2), None)
        self.assertEqual(self.card.grades_by_subject,{"Big Bang Theory": [2], "Other Theories": [3,2]})

    def test_average_grade_by_subject(self):
        self.card.add_grade("Big Bang Theory", 2)
        self.card.add_grade("Big Bang Theory", 6)
        self.card.add_grade("Other Theories", 3)
        self.assertEqual(self.card.average_grade_by_subject(), """Big Bang Theory: 4.00
Other Theories: 3.00""")

    def test_average_grade_for_all_subjects(self):
        self.card.add_grade("Big Bang Theory", 2)
        self.card.add_grade("Big Bang Theory", 6)
        self.card.add_grade("Other Theories", 3)
        self.assertEqual(self.card.average_grade_for_all_subjects(), "Average Grade: 3.67")

    def test_repr(self):
        self.card.add_grade("Big Bang Theory", 2)
        self.card.add_grade("Big Bang Theory", 6)
        self.card.add_grade("Other Theories", 3)
        self.assertEqual(repr(self.card), """Name: Michael O'Conner
Year: 11
----------
Big Bang Theory: 4.00
Other Theories: 3.00
----------
Average Grade: 3.67""")

if __name__ == "__main__":
    unittest.main()
