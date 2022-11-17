"""
Unit 3.1.2 Assignment: Classes and OOP

Name: Michael Luo
Date: 2022/11/10
"""
import random


class Student:
    """Represents a very generic student

    Parameters
    ----------
    name : str
        Name of student
    age : int
        Age of student
    """

    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age
        self.current_courses = []
        self.finished_courses = []

    def enroll(self, course: str):
        """Enrolls a student into a course. Updates the current_courses
        attribute.

        Parameters
        ----------
        course : str
            Name of the course
        """
        if course in self.current_courses:
            print("Already enrolled. Not added.")
            return

        self.current_courses.append(course)
        print(f"Successfully enrolled in {course}")

    def finish_course(self, course: str):
        """Simulates 'completing' a course. Removes a course from attribute
        current_courses and adds to finished_courses

        Parameters
        ----------
        course : str
            Name of the course
        """
        if course not in self.current_courses:
            print(f"{self.name} is not enrolled in {course}.")
            return

        self.finished_courses.append(
            self.current_courses.pop(self.current_courses.index(course))
        )
        print(f"Successfully finished {course}, congratulations!")

    def __repr__(self) -> str:
        return f"Name: {self.name}/Age: {self.age}"


class BloomTechStudent(Student):
    """Represents a student at BloomTech, implemented by extending Student

    Parameters
    ----------
    name : str
        Name of student
    age : int
        Age of student
    cohort : str
        Cohort of student eg. DS40
    status : bool, optional
        Active status of student, by default None
    """

    # Attributes
    open_tickets = []

    def __init__(self, name: str, age: int, cohort: str, status: bool = None):

        super().__init__(name, age)
        self.cohort = cohort
        self.status = status

    def create_support_ticket(self, kind: str):
        """Creates support ticket for the student. Adds to attribute
        open_tickets

        Parameters
        ----------
        kind : str
            One of ['academic support', 'general help', 'career coaching']
        """
        self.open_tickets.append(kind)

    def __repr__(self) -> str:
        return super().__repr__() + f"/Cohort: {self.cohort}"

    # class method
    def student_generator(num: int = 1):
        """Generates random BloomTechStudents.

        Parameters
        ----------
        n : int, optional
            # of students to generate, by default 1

        Returns
        -------
        list[BloomTechStudent]
        """
        students = []
        names = ["Michael", "Kelly", "Sophie", "Darius", "TF", "Nihlus"]

        for _ in range(num):
            name = random.choice(names)
            age = random.randint(18, 65)
            cohort = "DS" + str(random.randint(1, 50))
            status = random.randint(0, 1)
            students.append(BloomTechStudent(name, age, cohort, status))

        return students


if __name__ == "__main__":
    # Student testing
    print(
        "\n------------------------Testing student----------------------------"
    )
    a = Student("Bob", 29)
    a.enroll("Data Science")
    print(f"Current courses: {a.current_courses}")
    a.enroll("Data Science")
    a.finish_course("Data Science")
    a.finish_course("Data Science")
    print(f"Finished courses: {a.finished_courses}")

    # BloomTechStudent testing
    print(
        "\n-----------------------Testing BloomTechStudent--------------------"
    )
    b = BloomTechStudent("Alice", 24, "DS42", status=True)
    b.create_support_ticket("Career coaching")
    print(f"Open tickets: {b.open_tickets}")

    # Test class method student_generator() for BloomTechStudent
    print(BloomTechStudent.student_generator(num=5))
