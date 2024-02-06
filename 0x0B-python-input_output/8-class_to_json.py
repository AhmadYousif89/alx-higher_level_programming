#!/usr/bin/python3
"""Defines the class_to_json function."""


def class_to_json(obj):
    """
    Converts an instance of a class to a dict
    suitable for JSON serialization.

    Parameters:
    - obj: An instance of a class with serializable attributes.

    Returns:
    A dictionary representing the serialized form of the object.

    Example:
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        person = Person("John Doe", 25)

        result = class_to_json(person)

        print(result)
    ### Output: {'name': 'John Doe', 'age': 25}
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError(f"{obj} is not an instance of a class")

    attributes = obj.__dict__
    serialized_dict = {}

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_dict[key] = value

    return serialized_dict


# Example 1:
# class MyClass:
#     """My class"""

#     def __init__(self, name):
#         self.name = name
#         self.number = 0

#     def __str__(self):
#         return "[MyClass] {} - {:d}".format(self.name, self.number)


# m = MyClass("John")
# m.number = 89
# print(type(m))
# print(m)

# mj = class_to_json(m)
# print(type(mj))
# print(mj)


# Example 2:
# class MyClass:
#     """My class"""

#     score = 0

#     def __init__(self, name, number=4):
#         self.__name = name
#         self.number = number
#         self.is_team_red = (self.number % 2) == 0

#     def win(self):
#         self.score += 1

#     def lose(self):
#         self.score -= 1

#     def __str__(self):
#         return "[MyClass] {} - {:d} => {:d}".format(
#             self.__name, self.number, self.score
#         )


# m = MyClass("John")
# m.win()
# print(type(m))
# print(m)

# mj = class_to_json(m)
# print(type(mj))
# print(mj)
