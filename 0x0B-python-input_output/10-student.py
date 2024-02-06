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

    def to_json(self, attrs=None):
        """
        Converts an instance of a Student to a dictionary.

        Parameters:
        - self: The student object.
        - attrs: List of attributes to include.

        Returns:
        A dictionary representing the serialized form of the student.

        Example:
            person = Person("John Doe", 25)

            result = person.to_json(["first_name"])

        ### result: {'first_name': 'John Doe'}
        """
        if not hasattr(self, "__dict__"):
            raise TypeError(f"{self} is not an instance of class Student.")

        json_dict = self.__dict__
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            json_dict = {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }

        return json_dict


# student_1 = Student("John", "Doe", 23)
# student_2 = Student("Bob", "Dylan", 27)

# j_student_1 = student_1.to_json()
# j_student_2 = student_2.to_json(['first_name', 'age'])
# j_student_3 = student_2.to_json(['middle_name', 'age'])

# print(j_student_1)
# print(j_student_2)
# print(j_student_3)
