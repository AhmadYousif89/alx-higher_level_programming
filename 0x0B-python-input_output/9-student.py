#!/usr/bin/python3
"""Defines a class named Student."""


class Student:
    """
    Class to represent a student.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts an instance of a Student to a dictionary.

        Parameters:
        - self: The student object.

        Returns:
        A dictionary representing the serialized form of the student.

        Example:
            student = Student("John Doe", 25)

            result = student.to_json()

        ### result: {'first_name': 'John Doe', 'age': 25}
        """
        if not hasattr(self, "__dict__"):
            raise TypeError(f"{self} is not an instance of class Student.")

        json_dict = self.__dict__
        return json_dict


# students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

# for student in students:
#     j_student = student.to_json()
#     print(type(j_student))
#     print(j_student['first_name'])
#     print(type(j_student['first_name']))
#     print(j_student['age'])
#     print(type(j_student['age']))
