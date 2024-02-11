#!/usr/bin/python3
"""Defines the Base class."""
import json, csv, turtle


class Base:
    """
    Create the Base class.

    Attributes:
    - __nb_objects (int): The number of created objects.
    - id (int): The object identifier
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
        - id (None | int): The object identifier
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dictionaries.

        Args:
        -   list_dictionaries (list): A list of dictionaries.
        """
        if (
            list_dictionaries is None
            or len(list_dictionaries) == 0
            or any(
                len(_dict) == 0 or not isinstance(_dict, dict)
                for _dict in list_dictionaries
            )
        ):
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string.

        Args:
        -   json_string (str): A JSON str representation of a list of dicts.

        Returns:
        -   A deserialized Python list or an empty list otherwise.
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Convert a list of objects to a list of dictionaries
        and write to a file after JSON serialization.

        Args:
        -   list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.json"

        if (
            list_objs is None
            or len(list_objs) == 0
            or any(not isinstance(obj, cls) for obj in list_objs)
        ):
            with open(filename, 'w') as f:
                f.write("[]")
            return

        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())

        with open(filename, 'w') as f:
            f.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantiated from a dictionary of attributes.

        Args:
        -   **dictionary (dict): Key/value pairs of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new = cls(1)
            else:
                new = cls(1, 1)  # type: ignore
            new.update(**dictionary)  # type: ignore
            return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.

        Args:
        -   list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"

        if (
            list_objs is None
            or len(list_objs) == 0
            or any(not isinstance(obj, cls) for obj in list_objs)
        ):
            with open(filename, 'w') as f:
                f.write('[]')
            return

        with open(filename, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            header_written = False  # control the header row
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                # this check ensures that the header row are written only once
                if not header_written:
                    csv_writer.writerow(obj_dict.keys())  # id,width,height,x,y
                    header_written = True
                # this will write the values on each consecutive row
                csv_writer.writerow(obj_dict.values())  # 1,10,7,2,8

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.
        """
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, 'r', newline='') as f:
                list_dicts = [
                    {str(key): int(value) for key, value in _dict.items()}
                    for _dict in csv.DictReader(f)
                ]
                return [cls.create(**_dict) for _dict in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw all the Rectangles and Squares using Turtle graphics.

        Args:
        -   list_rectangles (list): A list of Rectangle instances.
        -   list_squares (list): A list of Square instances.
        """
        # Create a turtle screen
        screen = turtle.Screen()
        screen.bgcolor("white")

        # Create a turtle object
        painter = turtle.Turtle()
        painter.speed(1)
        painter.pensize(2)
        # draw the squares
        for sq in list_squares:
            print(sq)
            painter.color("red")
            painter.penup()
            painter.goto(sq.x, sq.y)
            painter.pendown()
            for _ in range(4):
                painter.forward(sq.size)
                painter.left(90)

        # draw the rectangles
        for rect in list_rectangles:
            print(rect)
            painter.penup()
            painter.goto(rect.x, rect.y)
            painter.pendown()
            for _ in range(2):
                painter.color("indigo")
                painter.forward(rect.width)
                painter.left(90)
                painter.forward(rect.height)
                painter.left(90)

        screen.exitonclick()
