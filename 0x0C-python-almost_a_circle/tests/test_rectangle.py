#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""
import io
import os
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_initialization(unittest.TestCase):
    """Testing the initialization of the Rectangle class."""

    def test_isinstance_of_base(self):
        self.assertIsInstance(Rectangle(8, 2), Base)

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_with_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_with_extra_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_with_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_with_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_with_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_with_five_args(self):
        r = Rectangle(10, 2, 0, 0, 7)
        self.assertEqual(7, r.id)


class Test_property_width(unittest.TestCase):
    """Testing the width attribute for the Rectangle class."""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.5, 1)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_getter(self):
        self.assertEqual(10, Rectangle(10, 2, 3, 9).width)


class Test_property_height(unittest.TestCase):
    """Testing the height attribute for the Rectangle class."""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "height")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 3.5)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_height_getter(self):
        self.assertEqual(2, Rectangle(10, 2, 3, 9).height)


class Test_property_x(unittest.TestCase):
    """Testing the x attribute for the Rectangle class."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "x", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 2.5, 9)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

    def test_x_getter(self):
        self.assertEqual(3, Rectangle(10, 2, 3, 9).x)


class Test_property_y(unittest.TestCase):
    """Testing the y attribute for the Rectangle class."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "y")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 2.5)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)

    def test_y_getter(self):
        self.assertEqual(9, Rectangle(10, 2, 3, 9).y)


class Test_area_method(unittest.TestCase):
    """Testing the (area) method for the Rectangle class."""

    def test_with_extra_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area("extra arg here!")

    def test_with_small_value(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_with_large_value(self):
        r = Rectangle(1_000_000, 1_000_000, 0, 0, 1)
        self.assertEqual(1_000_000_000_000, r.area())


class Test_printing_methods(unittest.TestCase):
    """Testing the (__str__) and (display) methods for the Rectangle class."""

    @staticmethod
    def get_output(rect, method):
        """
        Return the text printed on the stdout stream.

        Args:
        -   rect (Rectangle): The Rectangle object to be printed to stdout.
        -   method (str): The method to run on the rectangle.

        Returns:
        -   The text printed on stdout.
        """
        output = io.StringIO()
        sys.stdout = output
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return output

    # TEST __STR__ METHOD:
    def test_str_with_arg(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.__str__("Print This!")

    def test_str_with_width_height(self):
        r = Rectangle(4, 6)
        res = Test_printing_methods.get_output(r, "print")
        self.assertEqual(f"[Rectangle] ({r.id}) 0/0 - 4/6\n", res.getvalue())

    def test_str_with_width_height_x(self):
        r = Rectangle(5, 5, 1)
        self.assertEqual(f"[Rectangle] ({r.id}) 1/0 - 5/5", r.__str__())

    def test_str_with_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        self.assertEqual(f"[Rectangle] ({r.id}) 2/4 - 1/8", r.__str__())

    def test_str_with_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual(f"[Rectangle] ({r.id}) 2/4 - 13/21", r.__str__())

    def test_str_with_updated_attrs(self):
        r = Rectangle(5, 5, 0, 0)
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual(f"[Rectangle] ({r.id}) 8/10 - 15/1", r.__str__())

    # TEST DISPLAY METHOD:
    def test_with_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display("Print This!")

    def test_with_width_height(self):
        r = Rectangle(2, 3)
        expected = Test_printing_methods.get_output(r, "display")
        self.assertEqual("##\n##\n##\n", expected.getvalue())

    def test_with_width_height_x(self):
        r = Rectangle(3, 2, 1)
        expected = Test_printing_methods.get_output(r, "display")
        self.assertEqual(" ###\n ###\n", expected.getvalue())

    def test_with_width_height_y(self):
        r = Rectangle(4, 5, 0, 1)
        expected = Test_printing_methods.get_output(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, expected.getvalue())

    def test_with_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2)
        expected = Test_printing_methods.get_output(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, expected.getvalue())


class Test_update_args(unittest.TestCase):
    """Testing the (update) method with args for the Rectangle class."""

    def test_with_no_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update()
        expected = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(expected, r.__str__())

    def test_with_None(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(None)
        expected = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(expected, r.__str__())

    def test_with_one_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(50)
        expected = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(expected, r.__str__())

    def test_with_two_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(50, 2)
        expected = f"[Rectangle] ({r.id}) 10/10 - {r.width}/10"
        self.assertEqual(expected, r.__str__())

    def test_with_three_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(50, 2, 3)
        expected = f"[Rectangle] ({r.id}) 10/10 - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_with_four_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(50, 2, 3, 4)
        expected = f"[Rectangle] ({r.id}) {r.x}/10 - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_with_five_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(50, 2, 3, 4, 5)
        expected = f"[Rectangle] ({r.id}) {r.x}/{r.y} - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_with_extra_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(50, 2, 3, 4, 5, 6)
        expected = f"[Rectangle] ({r.id}) {r.x}/{r.y} - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_args_twice(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(50, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 50)
        expected = f"[Rectangle] ({r.id}) {r.x}/{r.y} - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())


class Test_update_Kwargs(unittest.TestCase):
    """Testing (update) method with kwargs for the Rectangle class."""

    def test_with_one_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=5)
        expected = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(expected, r.__str__())

    def test_with_two_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=2, id=50)
        expected = f"[Rectangle] ({r.id}) 10/10 - {r.width}/10"
        self.assertEqual(expected, r.__str__())

    def test_with_three_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=2, height=3, id=50)
        expected = f"[Rectangle] ({r.id}) 10/10 - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_with_four_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=50, width=4, height=2, x=1)
        expected = f"[Rectangle] ({r.id}) {r.x}/10 - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_with_five_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=50, width=4, height=2, x=1, y=5)
        expected = f"[Rectangle] ({r.id}) {r.x}/{r.y} - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_args_twice(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=50, x=1, height=2)
        r.update(y=3, height=15, width=2)
        expected = f"[Rectangle] ({r.id}) {r.x}/{r.y} - {r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_with_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(a=50, b=20)
        expected = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(expected, r.__str__())


class Test_update_args_Kwargs(unittest.TestCase):
    """Testing (update) with args and kwargs for the Rectangle class."""

    def test_args_with_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(50, 2, height=4, y=6)
        expected = f"[Rectangle] ({r.id}) 10/10 - {r.width}/10"
        self.assertEqual(expected, r.__str__())


class Test_to_dictionary_method(unittest.TestCase):
    """Testing to_dictionary method for the Rectangle class."""

    def test_with_arg(self):
        r = Rectangle(8, 2, 4, 1)
        with self.assertRaises(TypeError):
            r.to_dictionary("extra arg here!")

    def test_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(expected, r.to_dictionary())

    def test_equality(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_not_same(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertIsNot(r1, r2)


class Test_create_method(unittest.TestCase):
    """Testing the (create) method for the Rectangle class."""

    def test_create_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", r2.__str__())

    def test_not_same(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_equality(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)


class Test_to_json_string_method(unittest.TestCase):
    """Testing the (to_json_string) method for the Rectangle class."""

    def test_with_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        result = Rectangle.to_json_string([r.to_dictionary()])
        expected = '[{"id": 6, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(result, expected)

    def test_with_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(
            len(Rectangle.to_json_string(list_dicts)) == len(str(list_dicts))
        )


class Test_save_to_file_method(unittest.TestCase):
    """Testing the (save_to_file) method for the Rectangle class."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_with_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_with_empty_array(self):
        expected = Rectangle.save_to_file([])
        self.assertEqual(expected, None)
        with open("Rectangle.json", "r") as f:
            self.assertMultiLineEqual("[]", f.readline())

    def test_with_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            expected = '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}]'
            self.assertMultiLineEqual(expected, f.readline())

    def test_with_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            l1 = '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}, '
            l2 = '{"id": 3, "width": 2, "height": 4, "x": 1, "y": 2}]'
            self.assertMultiLineEqual(l1 + l2, f.readline())


class Test_load_from_file_method(unittest.TestCase):
    """Testing the (load_from_file) method for the Rectangle class."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r.__str__(), str(list_rectangles_output[0]))

    def test_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.__str__(), str(list_rectangles_output[0]))
        self.assertEqual(r2.__str__(), str(list_rectangles_output[1]))

    def test_output_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) is Rectangle for obj in output))

    def test_with_no_input(self):
        output = Rectangle.load_from_file()
        self.assertEqual([], output)


class Test_from_json_string_method(unittest.TestCase):
    """Testing the (from_json_string) method for the Rectangle class."""

    def test_with_one_rectangle(self):
        r_input = [{"id": 50, "width": 10, "height": 4, "x": 7}]
        json_input = Rectangle.to_json_string(r_input)
        output = Rectangle.from_json_string(json_input)
        self.assertEqual(r_input, output)

    def test_with_two_rectangles(self):
        r_input = [
            {"id": 50, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 89, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_input = Rectangle.to_json_string(r_input)
        output = Rectangle.from_json_string(json_input)
        self.assertEqual(r_input, output)

    def test_output_type(self):
        r_input = [{"id": 50, "width": 10, "height": 4}]
        json_input = Rectangle.to_json_string(r_input)
        output = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(output))


class Test_save_to_file_csv_method(unittest.TestCase):
    """Testing the (save_to_file_csv) method for the Rectangle class."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_with_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertMultiLineEqual("id,width,height,x,y\n", f.readline())
            self.assertMultiLineEqual("5,10,7,2,8\n", f.readline())

    def test_with_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertMultiLineEqual("id,width,height,x,y\n", f.readline())
            self.assertMultiLineEqual("5,10,7,2,8\n", f.readline())
            self.assertMultiLineEqual("3,2,4,1,2\n", f.readline())

    def test_with_None(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as f:
            self.assertEqual("[]", f.readline())

    def test_with_empty_list(self):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual("[]", f.readline())

    def test_with_none_cls_object(self):
        Rectangle.save_to_file_csv([{'x': 1, 'y': 1}])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual("[]", f.readline())


class Test_load_from_file_csv_method(unittest.TestCase):
    """Testing the (load_from_file_csv) method for the Rectangle class."""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass

    def test_with_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(r.__str__(), str(list_rectangles_output[0]))

    def test_with_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(r1.__str__(), str(list_rectangles_output[0]))
        self.assertEqual(r2.__str__(), str(list_rectangles_output[1]))

    def test_output_type(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) is Rectangle for obj in output))

    def test_with_no_input(self):
        output = Rectangle.load_from_file_csv()
        self.assertEqual([], output)


if __name__ == "__main__":
    unittest.main()
