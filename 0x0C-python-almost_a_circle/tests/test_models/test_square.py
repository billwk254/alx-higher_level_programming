#!/usr/bin/python3
"""
test_square.py - This module contains tests for the Square class.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init_with_args(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 99)

    def test_init_without_args(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        expected_output = "###\n###\n###\n"
        with self.assertLogs() as log:
            s.display()
        self.assertEqual('\n'.join(log.output), expected_output)

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_update(self):
        s = Square(10, 10, 1, 1)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 2)
        self.assertEqual(s.size, 2)
        s.update(89, 2, 3)
        self.assertEqual(s.size, 2)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.x, 4)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual(s.y, 5)
        s.update(id=98)
        self.assertEqual(s.id, 98)
        s.update(id=98, size=3)
        self.assertEqual(s.size, 3)
        s.update(id=98, size=3, x=5)
        self.assertEqual(s.x, 5)
        s.update(id=98, size=3, x=5, y=6)
        self.assertEqual(s.y, 6)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 99)
        s_dict = s.to_dictionary()
        self.assertTrue(isinstance(s_dict, dict))
        self.assertEqual(s_dict, {'id': 99, 'size': 5, 'x': 1, 'y': 2})


if __name__ == '__main__':
    unittest.main()
