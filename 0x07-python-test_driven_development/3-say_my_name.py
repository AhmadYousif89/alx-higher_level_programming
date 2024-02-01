#!/usr/bin/python3
"""Defines a say_my_name function"""


def say_my_name(first_name, last_name=""):
    """
    Generate a string introducing a person with their first and last names.
    Args:
    - first_name (str): The first name of the person.
    - last_name (str, optional): The last name of the person. Defaults to "".
    Returns:
    - str: A string in the format "My name is <first_name> <last_name>".
    Raises:
    - TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    intro = f"My name is {first_name.strip()} {last_name.strip()}"

    print(intro)


# say_my_name("John", "Smith")
# say_my_name("Walter", "White")
# say_my_name("Bob")
# try:
#     say_my_name(12, "White")
# except Exception as e:
#     print(e)
