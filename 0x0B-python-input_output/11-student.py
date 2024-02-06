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

    def reload_from_json(self, json):
        """
        Replace all attributes of an instance.

        Args:
            json (dict): The key/value pairs to replace the attributes.
        """
        if not isinstance(json, dict):
            raise TypeError(f"{json} is not of type dict")

        for key, value in json.items():
            setattr(self, key, value)


# import os
# import sys


# read_file = __import__('0-read_file').read_file
# save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# if len(sys.argv) < 2:
#     print("Usage: ./11-student.py <path_to_json>")
#     sys.exit(1)
# path = sys.argv[1]

# if os.path.exists(path):
#     os.remove(path)

# student_1 = Student("John", "Doe", 23)
# j_student_1 = student_1.to_json()
# print("Initial student:")
# print(student_1)
# print(type(student_1))
# print(type(j_student_1))
# print(
#     "{} {} {}".format(student_1.first_name,
#                       student_1.last_name, student_1.age)
# )


# save_to_json_file(j_student_1, path)
# read_file(path)
# print("\nSaved to disk")


# print("Fake student:")
# new_student_1 = Student("Fake", "Fake", 89)
# print(new_student_1)
# print(type(new_student_1))
# print(
#     "{} {} {}".format(
#         new_student_1.first_name, new_student_1.last_name, new_student_1.age
#     )
# )


# print("Load dictionary from file:")
# new_j_student_1 = load_from_json_file(path)

# new_student_1.reload_from_json(j_student_1)
# print(new_student_1)
# print(type(new_student_1))
# print(
#     "{} {} {}".format(
#         new_student_1.first_name, new_student_1.last_name, new_student_1.age
#     )
# )
