import unittest
# from testing.student.student.project.student import Student
from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.student = Student("Harry")

    def test_init(self):
        self.assertEqual(self.student.name, "Harry")
        self.assertEqual(self.student.courses, {})

    def test_enroll(self):
        self.assertEqual(self.student.enroll("Transfiguration", ["Basics of transfiguration"]),"Course and course notes have been added.")
        self.assertEqual(self.student.courses,{"Transfiguration": ["Basics of transfiguration"]})
        self.assertEqual(self.student.enroll("Transfiguration", ["With Professor Minerva McGonagol"]),"Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses,{"Transfiguration": ["Basics of transfiguration", "With Professor Minerva McGonagol"]})
        self.assertEqual(self.student.enroll("Herbology", [],False), "Course has been added.")
        self.assertEqual(self.student.courses,{"Transfiguration": ["Basics of transfiguration", "With Professor Minerva McGonagol"],"Herbology": []})
        self.assertEqual(self.student.enroll("Prophecy", [],"Y"), "Course and course notes have been added.")
        self.assertEqual(self.student.courses,{"Transfiguration": ["Basics of transfiguration", "With Professor Minerva McGonagol"],"Herbology": [],"Prophecy":[]})
        self.assertEqual(self.student.enroll("Potions", None,None), "Course has been added.")
        self.assertEqual(self.student.courses,{"Transfiguration": ["Basics of transfiguration", "With Professor Minerva McGonagol"],"Herbology": [],"Prophecy":[],"Potions":[]})




    def test_add_notes(self):
        with self.assertRaises(Exception) as msg:
            self.student.add_notes("Transfiguration", "Canceled")
        self.assertEqual(str(msg.exception), "Cannot add notes. Course not found.")
        self.assertEqual(self.student.enroll("Transfiguration", ["Basics of transfiguration"]),"Course and course notes have been added.")
        self.assertEqual(self.student.add_notes("Transfiguration", "With Minerva McGonagol"), "Notes have been updated")
        self.assertEqual(self.student.courses,{"Transfiguration": ["Basics of transfiguration", "With Minerva McGonagol"]})

    def test_leave_course(self):
        with self.assertRaises(Exception) as msg:
            self.student.leave_course("Prophecy")
        self.assertEqual(str(msg.exception), "Cannot remove course. Course not found.")
        self.student.enroll("Prophecy", None, None)
        self.assertEqual(self.student.leave_course("Prophecy"), "Course has been removed")


if __name__ == "__main__":
    unittest.main()
