#!/usr/bin/python3
"""Defines unittests for models/square.py"""
import io
import os
import sys
import unittest
from models.base import Base
from models.square import Square


class Test_initialization(unittest.TestCase):
    """Testing initialization of the Square class."""

    def test_isinstance_of_Base(self):
        self.assertIsInstance(Square(1), Base)

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_with_extra_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_with_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_with_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_with_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_with_four_args(self):
        s = Square(10, 2, 0, 7)
        self.assertEqual(7, s.id)


class Test_property_size(unittest.TestCase):
    """Testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.5)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)


class Test_property_x(unittest.TestCase):
    """Testing the x attribute for the Square class."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "x", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2.5, 9)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_x_getter(self):
        self.assertEqual(2, Square(10, 2, 3).x)


class Test_property_y(unittest.TestCase):
    """Testing the y attribute for the Square class."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "y")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 2.5)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 5, -1)

    def test_y_getter(self):
        self.assertEqual(3, Square(10, 2, 3).y)


class Test_area_method(unittest.TestCase):
    """Testing the area method of the Square class."""

    def test_with_extra_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area("extra arg here!")

    def test_with_small_value(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_with_large_value(self):
        s = Square(1_000_000, 0, 0, 1)
        self.assertEqual(1_000_000_000_000, s.area())


class Test_printing_methods(unittest.TestCase):
    """Testing __str__ and display methods for the Square class."""

    @staticmethod
    def get_output(sq, method):
        """
        Return the text printed on the stdout stream.

        Args:
        -   sq (Square): The Square object to be printed to stdout.
        -   method (str): The method to run on the square.

        Returns:
        -   The text printed on stdout.
        """
        output = io.StringIO()
        sys.stdout = output
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return output

    # TEST __STR__ METHOD:
    def test_str_with_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__("Print This!")

    def test_str_with_size(self):
        s = Square(4)
        output = Test_printing_methods.get_output(s, "print")
        expected = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(expected, output.getvalue())

    def test_str_method_size_x(self):
        s = Square(5, 5)
        expected = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(expected, s.__str__())

    def test_str_method_size_x_y(self):
        s = Square(7, 4, 22)
        expected = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(expected, s.__str__())

    def test_str_method_size_x_y_id(self):
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", s.__str__())

    def test_str_with_updated_attrs(self):
        s = Square(5, 0, 0)
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual(f"[Square] ({s.id}) 8/10 - 15", s.__str__())

    # TEST DISPLAY METHOD:
    def test_with_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display("Print This!")

    def test_with_size(self):
        s = Square(2)
        capture = Test_printing_methods.get_output(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_with_size_x(self):
        s = Square(3, 1)
        capture = Test_printing_methods.get_output(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_with_size_y(self):
        s = Square(3, 0, 1)
        capture = Test_printing_methods.get_output(s, "display")
        display = "\n###\n###\n###\n"
        self.assertEqual(display, capture.getvalue())

    def test_with_size_x_y(self):
        s = Square(2, 3, 2, 1)
        capture = Test_printing_methods.get_output(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())


class Test_update_args(unittest.TestCase):
    """Testing update args method of the Square class."""

    def test_with_no_args(self):
        s = Square(10, 10, 10)
        s.update()
        expected = f"[Square] ({s.id}) 10/10 - 10"
        self.assertEqual(expected, s.__str__())

    def test_with_None(self):
        s = Square(10, 10, 10)
        s.update(None)
        expected = f"[Square] ({s.id}) 10/10 - 10"
        self.assertEqual(expected, s.__str__())

    def test_with_one_arg(self):
        s = Square(10, 10, 10)
        s.update(50)
        expected = f"[Square] ({s.id}) 10/10 - 10"
        self.assertEqual(expected, s.__str__())

    def test_with_two_args(self):
        s = Square(10, 10, 10)
        s.update(50, 2)
        expected = f"[Square] ({s.id}) 10/10 - {s.size}"
        self.assertEqual(expected, s.__str__())

    def test_with_three_args(self):
        s = Square(10, 10, 10)
        s.update(50, 2, 3)
        expected = f"[Square] ({s.id}) {s.x}/10 - {s.size}"
        self.assertEqual(expected, s.__str__())

    def test_with_four_args(self):
        s = Square(10, 10, 10)
        s.update(50, 2, 3, 4)
        expected = f"[Square] ({s.id}) {s.x}/{s.y} - {s.size}"
        self.assertEqual(expected, s.__str__())

    def test_with_extra_args(self):
        s = Square(10, 10, 10)
        s.update(50, 2, 3, 4, 5)
        expected = f"[Square] ({s.id}) {s.x}/{s.y} - {s.size}"
        self.assertEqual(expected, s.__str__())

    def test_args_twice(self):
        s = Square(10, 10, 10)
        s.update(50, 2, 3, 4)
        s.update(4, 3, 2, 89)
        expected = f"[Square] ({s.id}) {s.x}/{s.y} - {s.size}"
        self.assertEqual(expected, s.__str__())


class Test_update_kwargs(unittest.TestCase):
    """Testing update kwargs method for the Square class."""

    def test_with_one_arg(self):
        s = Square(10, 10, 10)
        s.update(id=5)
        expected = f"[Square] ({s.id}) 10/10 - 10"
        self.assertEqual(expected, s.__str__())

    def test_with_two_args(self):
        s = Square(10, 10, 10)
        s.update(size=2, id=2)
        expected = f"[Square] ({s.id}) 10/10 - 2"
        self.assertEqual(expected, s.__str__())

    def test_with_three_args(self):
        s = Square(10, 10, 10)
        s.update(y=1, size=3, id=89)
        expected = f"[Square] ({s.id}) 10/1 - 3"
        self.assertEqual(expected, s.__str__())

    def test_with_four_args(self):
        s = Square(10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        expected = f"[Square] ({s.id}) 1/3 - 4"
        self.assertEqual(expected, s.__str__())

    def test_args_twice(self):
        s = Square(10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        expected = f"[Square] ({s.id}) 15/3 - 2"
        self.assertEqual(expected, s.__str__())

    def test_with_wrong_keys(self):
        s = Square(10, 10, 10)
        s.update(a=50, b=20)
        expected = f"[Square] ({s.id}) 10/10 - 10"
        self.assertEqual(expected, s.__str__())


class Test_update_args_Kwargs(unittest.TestCase):
    """Testing (update) with args and kwargs for the Square class."""

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10)
        s.update(50, 2, y=6)
        expected = f"[Square] ({s.id}) 10/10 - {s.size}"
        self.assertEqual(expected, s.__str__())


class Test_to_dictionary_method(unittest.TestCase):
    """Testing to_dictionary method of the Square class."""

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary("extra arg here!")

    def test_output(self):
        s = Square(10, 2, 1, 1)
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(expected, s.to_dictionary())

    def test_equality(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_not_same(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)


class Test_create_method(unittest.TestCase):
    """Testing create method for the Square class."""

    def test_create_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", s2.__str__())

    def test_not_same(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_equality(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class Test_to_json_string_method(unittest.TestCase):
    """Testing the (to_json_string) method for the Square class."""

    def test_with_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Square.to_json_string([s.to_dictionary()])) == 39)

    def test_with_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Square.to_json_string(list_dicts)) == 78)


class Test_save_to_file_method(unittest.TestCase):
    """Testing the (save_to_file) method for the Square class."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_with_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_with_empty_array(self):
        expected = Square.save_to_file([])
        self.assertEqual(expected, None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.readline())

    def test_with_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            expected = '[{"id": 8, "size": 10, "x": 7, "y": 2}]'
            self.assertMultiLineEqual(expected, f.readline())

    def test_with_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            l1 = '[{"id": 8, "size": 10, "x": 7, "y": 2}, '
            l2 = '{"id": 3, "size": 8, "x": 1, "y": 2}]'
            self.assertMultiLineEqual(l1 + l2, f.readline())


class Test_load_from_file_method(unittest.TestCase):
    """Testing the (load_from_file) method for the Square class."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_one_square(self):
        s = Square(5, 1, 3, 3)
        Square.save_to_file([s])
        list_squares_output = Square.load_from_file()
        self.assertEqual(s.__str__(), str(list_squares_output[0]))

    def test_two_squares(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(s1.__str__(), str(list_squares_output[0]))
        self.assertEqual(s2.__str__(), str(list_squares_output[1]))

    def test_output_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) is Square for obj in output))

    def test_with_no_input(self):
        output = Square.load_from_file()
        self.assertEqual([], output)


class Test_from_json_string_method(unittest.TestCase):
    """Testing the (from_json_string) method for the Square class."""

    def test_with_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_with_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7},
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_output_type(self):
        s_input = [{"id": 50, "size": 4}]
        json_input = Square.to_json_string(s_input)
        output = Square.from_json_string(json_input)
        self.assertEqual(list, type(output))


class Test_save_to_file_csv_method(unittest.TestCase):
    """Testing the (save_to_file_csv) method for the Square class."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

    def test_with_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertMultiLineEqual("id,size,x,y\n", f.readline())
            self.assertMultiLineEqual("8,10,7,2\n", f.readline())

    def test_with_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertMultiLineEqual("id,size,x,y\n", f.readline())
            self.assertMultiLineEqual("8,10,7,2\n", f.readline())
            self.assertMultiLineEqual("3,8,1,2\n", f.readline())

    def test_with_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_with_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_with_none_cls_object(self):
        Square.save_to_file_csv([{'x': 1, 'y': 1}])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())


class Test_load_from_file_csv_method(unittest.TestCase):
    """Testing the (load_from_file_csv) method for the Square class."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_with_one_square(self):
        s = Square(5, 1, 3, 3)
        Square.save_to_file_csv([s])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(s.__str__(), str(list_squares_output[0]))

    def test_with_two_squares(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(s2.__str__(), str(list_squares_output[1]))

    def test_output_type(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) is Square for obj in output))

    def test_with_no_input(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)


if __name__ == "__main__":
    unittest.main()
