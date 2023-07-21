#!/usr/bin/python3


"""
test_rectangle.py - This module contains tests for the Rectangle class.
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init_with_args(self):
        r = Rectangle(10, 5, 1, 2, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 99)

    def test_init_without_args(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with self.assertLogs() as log:
            r.display()
        self.assertEqual('\n'.join(log.output), expected_output)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)
        r.update(id=98)
        self.assertEqual(r.id, 98)
        r.update(id=98, width=3)
        self.assertEqual(r.width, 3)
        r.update(id=98, width=3, height=4)
        self.assertEqual(r.height, 4)
        r.update(id=98, width=3, height=4, x=5)
        self.assertEqual(r.x, 5)
        r.update(id=98, width=3, height=4, x=5, y=6)
        self.assertEqual(r.y, 6)

    def test_to_dictionary(self):
        r = Rectangle(10, 5, 1, 2, 99)
        r_dict = r.to_dictionary()
        self.assertTrue(isinstance(r_dict, dict))
        self.assertEqual(r_dict, {'id': 99, 'width': 10, 'height': 5, 'x': 1, 'y': 2})


if __name__ == '__main__':
    unittest.main()
