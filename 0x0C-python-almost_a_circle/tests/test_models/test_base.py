#!/usr/bin/python3


"""
test_base.py - This module contains tests for the Base class.
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_init_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)
        self.assertEqual(b4.id, 3)

    def test_from_json_string_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(Base.from_json_string(json_str), [])

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        Base.save_to_file([b1, b2, b3])
        with open("Base.json", 'r') as file:
            self.assertEqual(
                Base.from_json_string(file.read()),
                [{'id': 1}, {'id': 2}, {'id': 3}]
            )

    def test_create(self):
        r = Rectangle(10, 5, 0, 0, 1)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertNotEqual(r, r2)
        self.assertEqual(r.__dict__, r2.__dict__)

    def test_load_from_file(self):
        r1 = Rectangle(10, 5, 0, 0, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertTrue(isinstance(rectangles, list))
        self.assertEqual(len(rectangles), 2)
        for r in rectangles:
            self.assertTrue(isinstance(r, Rectangle))


if __name__ == '__main__':
    unittest.main()
