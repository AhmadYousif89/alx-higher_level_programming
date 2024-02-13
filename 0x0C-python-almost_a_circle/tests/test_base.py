#!/usr/bin/python3
"""Defines the unittests for the base.py module"""
import unittest
from models.base import Base


class Test_initialization(unittest.TestCase):
    """Testing initialization of the Base class."""

    def test_with_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_extra_args(self):
        with self.assertRaises(TypeError):
            Base(1, "extra arg here!")

    def test_with_three_objects(self):
        b1 = Base()
        Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_with_id_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_with_mixed_ids(self):
        b1 = Base()
        Base(20)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_with_public_id(self):
        b = Base(30)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_access_private_prop(self):
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_objects)

    def test_id_str(self):
        self.assertEqual("abc", Base("abc").id)

    def test_id_float(self):
        self.assertEqual(20.5, Base(20.5).id)

    def test_id_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_id_bytes(self):
        self.assertEqual(b'Hi', Base(b'Hi').id)

    def test_id_complex(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_id_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_id_negative_inf(self):
        self.assertEqual(float('-inf'), Base(float('-inf')).id)

    def test_id_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)


class Test_to_json_string(unittest.TestCase):
    """Testing to_json_string method of Base class."""

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_with_extra_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], "extra arg here!")

    def test_with_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_with_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))


class Test_from_json_string(unittest.TestCase):
    """Testing from_json_string method of Base class."""

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_extra_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], "extra arg here!")

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))


class Test_save_to_file(unittest.TestCase):
    """Testing save_to_file method of Base class."""

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_with_extra_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], "extra arg here!")


class Test_load_from_file(unittest.TestCase):
    """Testing load_from_file_method of Base class."""

    def test_load_from_file_extra_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file("extra arg here!")


class Test_save_to_file_csv(unittest.TestCase):
    """Testing save_to_file_csv method of Base class."""

    def test_save_to_file_csv_extra_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv([], "extra arg here!")

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv()


class Test_load_from_file_csv(unittest.TestCase):
    """Testing load_from_file_csv method of Base class."""

    def test_load_from_file_csv_extra_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv("extra arg here!")


class Test_draw(unittest.TestCase):
    """Testing draw method of Base class."""

    def test_draw_no_args(self):
        with self.assertRaises(TypeError):
            Base.draw()

    def test_draw_extra_args(self):
        with self.assertRaises(TypeError):
            Base.draw([], [], "extra arg here!")


if __name__ == '__main__':
    unittest.main()
