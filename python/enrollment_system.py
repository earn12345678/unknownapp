from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class TimeSlot:
    days: str
    start_time: str  # "HH:MM"
    end_time: str    # "HH:MM"

    def overlaps(self, other: "TimeSlot") -> bool:
        if not self.days or not other.days:
            return False

        if not self._share_days(self.days, other.days):
            return False

        self_start = self._to_minutes(self.start_time)
        self_end = self._to_minutes(self.end_time)
        other_start = self._to_minutes(other.start_time)
        other_end = self._to_minutes(other.end_time)

        if -1 in (self_start, self_end, other_start, other_end):
            return False

        return self_start < other_end and other_start < self_end

    @staticmethod
    def _share_days(d1: str, d2: str) -> bool:
        a = d1.upper()
        b = d2.upper()
        tokens = ["TH", "M", "T", "W", "F", "S", "U"]
        for token in tokens:
            if token in a and token in b:
                return True
        return False

    @staticmethod
    def _to_minutes(time_text: str) -> int:
        try:
            h, m = time_text.split(":")
            return int(h) * 60 + int(m)
        except Exception:
            return -1


@dataclass
class Student:
    student_id: str
    name: str
    major: str
    enrolled_courses: List[str] = field(default_factory=list)
    completed_courses: List[str] = field(default_factory=list)

    def is_enrolled(self, course_code: str) -> bool:
        return course_code in self.enrolled_courses

    def has_completed(self, course_code: str) -> bool:
        return course_code in self.completed_courses

    def enroll(self, course_code: str) -> bool:
        if self.is_enrolled(course_code):
            return False
        self.enrolled_courses.append(course_code)
        return True

    def drop(self, course_code: str) -> bool:
        if not self.is_enrolled(course_code):
            return False
        self.enrolled_courses.remove(course_code)
        return True


@dataclass
class Course:
    code: str
    title: str
    credits: int
    capacity: int
    timeslot: Optional[TimeSlot] = None
    prerequisites: List[str] = field(default_factory=list)
    enrolled_students: List[str] = field(default_factory=list)

    def is_full(self) -> bool:
        return len(self.enrolled_students) >= self.capacity

    def enroll_student(self, student_id: str) -> bool:
        if self.is_full() or student_id in self.enrolled_students:
            return False
        self.enrolled_students.append(student_id)
        return True

    def remove_student(self, student_id: str) -> bool:
        if student_id not in self.enrolled_students:
            return False
        self.enrolled_students.remove(student_id)
        return True


class EnrollmentSystem:
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}

    def add_student(self, student: Student) -> bool:
        if not student or student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        return True

    def add_course(self, course: Course) -> bool:
        if not course or course.code in self.courses:
            return False
        self.courses[course.code] = course
        return True

    def register_course(self, student_id: str, course_code: str) -> Dict[str, object]:
        student = self.students.get(student_id)
        if student is None:
            return {"success": False, "message": f"Student not found: {student_id}"}

        course = self.courses.get(course_code)
        if course is None:
            return {"success": False, "message": f"Course not found: {course_code}"}

        if student.is_enrolled(course_code):
            return {"success": False, "message": f"Already enrolled in {course_code}."}

        if course.is_full():
            return {"success": False, "message": f"Course {course_code} is full."}

        for prereq in course.prerequisites:
            if not student.has_completed(prereq):
                return {
                    "success": False,
                    "message": f"Prerequisite not met: {prereq} is required for {course_code}."
                }

        for enrolled_code in student.enrolled_courses:
            enrolled_course = self.courses.get(enrolled_code)
            if enrolled_course and enrolled_course.timeslot and course.timeslot:
                if enrolled_course.timeslot.overlaps(course.timeslot):
                    return {
                        "success": False,
                        "message": f"Schedule conflict: {course_code} conflicts with {enrolled_code}."
                    }

        if not course.enroll_student(student_id):
            return {"success": False, "message": "Failed to enroll for unknown reason."}

        student.enroll(course_code)
        return {"success": True, "message": f"Enrolled in {course_code} ({course.title})."}

    def drop_course(self, student_id: str, course_code: str) -> Dict[str, object]:
        student = self.students.get(student_id)
        if student is None:
            return {"success": False, "message": f"Student not found: {student_id}"}

        course = self.courses.get(course_code)
        if course is None:
            return {"success": False, "message": f"Course not found: {course_code}"}

        if not student.is_enrolled(course_code):
            return {"success": False, "message": f"Not enrolled in {course_code}."}

        student.drop(course_code)
        course.remove_student(student_id)
        return {"success": True, "message": f"Dropped {course_code} ({course.title})."}
