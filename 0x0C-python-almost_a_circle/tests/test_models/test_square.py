#!/usr/bin/python3
"""
Test module for Square class.
"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_inheritance(self):
        """
        Test if Square inherits from Rectangle.
        """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_attributes(self):
        """
        Test the attributes of Square class.
        """
        s = Square(5, 2, 4, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 1)

    def test_size_type_error(self):
        """
        Test size attribute with non-integer value.
        """
        with self.assertRaises(TypeError):
            s = Square("size")

    def test_size_value_error(self):
        """
        Test size attribute with value less than or equal to 0.
        """
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_str(self):
        """
        Test the __str__ method of Square.
        """
        s = Square(5, 2, 4, 1)
        expected_str = "[Square] (1) 2/4 - 5"
        self.assertEqual(str(s), expected_str)

    def test_update(self):
        """
        Test the update method of Square.
        """
        s = Square(5, 2, 4, 1)
        s.update(10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 4)

        s.update(20, 10)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 4)

        s.update(30, 15, 3)
        self.assertEqual(s.id, 30)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

        s.update(40, 20, 5, 7)
        self.assertEqual(s.id, 40)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 7)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of Square.
        """
        s = Square(5, 2, 4, 1)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 4}
        self.assertDictEqual(s_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
