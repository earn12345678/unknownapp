import unittest
from enrollment_system import EnrollmentSystem, Student, Course, TimeSlot


class EnrollmentSystemTest(unittest.TestCase):
    def setUp(self):
        self.system = EnrollmentSystem()
        self.student = Student(student_id="S1", name="Alice", major="CS")
        self.system.add_student(self.student)

        self.course1 = Course(
            code="CS101",
            title="Intro to CS",
            credits=3,
            capacity=2,
            timeslot=TimeSlot(days="MWF", start_time="09:00", end_time="10:00"),
        )
        self.course2 = Course(
            code="CS201",
            title="Data Structures",
            credits=3,
            capacity=2,
            timeslot=TimeSlot(days="MWF", start_time="09:30", end_time="10:30"),
            prerequisites=["CS101"],
        )

        self.system.add_course(self.course1)
        self.system.add_course(self.course2)

    def test_register_course_success(self):
        result = self.system.register_course("S1", "CS101")
        self.assertTrue(result["success"])
        self.assertIn("CS101", self.student.enrolled_courses)

    def test_register_course_prerequisite_not_completed(self):
        result = self.system.register_course("S1", "CS201")
        self.assertFalse(result["success"])
        self.assertIn("Prerequisite not met", result["message"])

    def test_register_course_time_conflict(self):
        self.system.register_course("S1", "CS101")
        # CS201 has CS101 prereq, mark completed for conflict check
        self.student.completed_courses.append("CS101")

        result = self.system.register_course("S1", "CS201")
        self.assertFalse(result["success"])
        self.assertIn("Schedule conflict", result["message"])

    def test_drop_course_success(self):
        self.system.register_course("S1", "CS101")
        result = self.system.drop_course("S1", "CS101")
        self.assertTrue(result["success"])
        self.assertNotIn("CS101", self.student.enrolled_courses)


if __name__ == "__main__":
    unittest.main()
