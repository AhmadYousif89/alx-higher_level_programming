#!/usr/bin/python3
# run with --> py -m tests.general_tests
from models.square import Base, Square, Rectangle

if __name__ == "__main__":
    print("\n---------- 1. Base class ----------\n")

    b1 = Base()
    print(b1.id)
    b2 = Base()
    print(b2.id)
    b3 = Base()
    print(b3.id)
    b4 = Base(12)
    print(b4.id)
    b5 = Base()
    print(b5.id)

    print("\n---------- # 2. First Rectangle ----------\n")

    r1 = Rectangle(10, 2)
    print(r1.id)
    r2 = Rectangle(2, 10)
    print(r2.id)
    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

    print("\n---------- # 3. Validate attributes ----------\n")

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print("\n---------- # 4. Area first ----------\n")

    r1 = Rectangle(3, 2)
    print(r1.area())
    r2 = Rectangle(2, 10)
    print(r2.area())
    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

    print("\n---------- # 5. Display #0 ----------\n")

    r1 = Rectangle(4, 6)
    r1.display()
    print("---")
    r1 = Rectangle(2, 2)
    r1.display()

    print("\n---------- # 6.__str__ ----------\n")

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)
    r2 = Rectangle(5, 5, 1)
    print(r2)

    print("\n---------- # 7. Display #1 ----------\n")

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()
    print("---")
    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

    print("\n---------- 8. Update #0 ----------\n")

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)
    r1.update(89)
    print(r1)
    r1.update(89, 2)
    print(r1)
    r1.update(89, 2, 3)
    print(r1)
    r1.update(89, 2, 3, 4)
    print(r1)
    r1.update(89, 2, 3, 4, 5)
    print(r1)

    print("\n---------- 9. Update #1 ----------\n")

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)
    r1.update(height=1)
    print(r1)
    r1.update(width=1, x=2)
    print(r1)
    r1.update(y=1, width=2, x=3, id=89)
    print(r1)
    r1.update(50, x=1, height=2, y=3, width=4)  # should skip Kwargs
    print(r1)

    print("\n---------- 10. And now, the Square! ----------\n")

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()
    print("---")
    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()
    print("---")
    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

    print("\n---------- 11. Square size ----------\n")

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)
    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    try:
        s1.size = -9
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print("\n---------- 12. Square update ----------\n")

    s1 = Square(5)
    print(s1)
    s1.update(10)
    print(s1)
    s1.update(1, 2)
    print(s1)
    s1.update(1, 2, 3)
    print(s1)
    s1.update(1, 2, 3, 4)
    print(s1)
    s1.update(x=12)
    print(s1)
    s1.update(size=7, y=1)
    print(s1)
    s1.update(size=7, id=89, y=1)
    print(s1)
    s1.update(50, size=4, id=89, y=6)  # should skip the Kwargs
    print(s1)

    print("\n---------- 13. Rectangle instance to dictionary ----------\n")

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

    print("\n---------- 14. Square instance to dictionary ----------\n")

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)

    print("\n---------- 15. Dictionary to JSON string ----------\n")

    s1 = Square(10, 7, 2, id=10)
    s_dictionary = s1.to_dictionary()
    print(s_dictionary)
    print(type(s_dictionary))
    json_dictionary = Base.to_json_string([s_dictionary])
    print(json_dictionary)
    print(type(json_dictionary))

    print("\n----------\n")
    # test multiple dicts
    r1 = Rectangle(10, 7, 2, 8, id=20)
    r_dictionary = r1.to_dictionary()
    print(r_dictionary)
    print(type(r_dictionary))
    all_to_json = Base.to_json_string([r_dictionary, s_dictionary])
    print(all_to_json)
    print(type(all_to_json))

    print("\n---------- 16. JSON string to file ----------\n")

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

    s1 = Square(8, 6, 2)
    s2 = Square(2, 4)
    Square.save_to_file([s1, s2])

    with open("Square.json", "r") as file:
        print(file.read())

    print("\n---------- 17. JSON string to Dictionary ----------\n")

    list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7},
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

    print("\n---------- 18. Dictionary to Instance ----------\n")

    r1 = Rectangle(3, 5, 1)
    print(r1)
    dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**dictionary)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

    print("\n----------\n")

    s1 = Square(6, 3, 8)
    print(s1)
    dictionary = s1.to_dictionary()
    s2 = Square.create(**dictionary)
    print(s2)
    print(s1 is s2)
    print(s1 == s2)

    print("\n---------- 19. File to instances ----------\n")

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

    print("\n---------- 20. JSON ok, but CSV? ----------\n")

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file_csv()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file_csv(list_squares_input)

    list_squares_output = Square.load_from_file_csv()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

    print("\n---------- 21. Let's draw it ----------\n")

    list_rectangles = [
        Rectangle(100, 40),
        Rectangle(90, 110, 30, 10),
        Rectangle(20, 25, 110, 80),
    ]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
