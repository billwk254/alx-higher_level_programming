#!/usr/bin/python3
"""
test_rectangle.py - Unit tests for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    TestRectangle - Test cases for the Rectangle class.
    """

    def test_id_assignment(self):
        """
        Test id assignment when 'id' is provided and when 'id' is not provided.
        """
        obj1 = Rectangle(10, 20)
        self.assertEqual(obj1.id, 1)

        obj2 = Rectangle(5, 10, 2, 2, 10)
        self.assertEqual(obj2.id, 10)

    def test_width(self):
        """
        Test width getter and setter.
        """
        obj = Rectangle(5, 10)
        self.assertEqual(obj.width, 5)

        obj.width = 20
        self.assertEqual(obj.width, 20)

        with self.assertRaises(TypeError):
            obj.width = "invalid"

        with self.assertRaises(ValueError):
            obj.width = -5

    def test_height(self):
        """
        Test height getter and setter.
        """
        obj = Rectangle(5, 10)
        self.assertEqual(obj.height, 10)

        obj.height = 15
        self.assertEqual(obj.height, 15)

        with self.assertRaises(TypeError):
            obj.height = "invalid"

        with self.assertRaises(ValueError):
            obj.height = 0

    def test_x(self):
        """
        Test x getter and setter.
        """
        obj = Rectangle(5, 10, 2, 2)
        self.assertEqual(obj.x, 2)

        obj.x = 5
        self.assertEqual(obj.x, 5)

        with self.assertRaises(TypeError):
            obj.x = "invalid"

        # x can be set to negative values
        obj.x = -3
        self.assertEqual(obj.x, -3)

    def test_y(self):
        """
        Test y getter and setter.
        """
        obj = Rectangle(5, 10, 2, 2)
        self.assertEqual(obj.y, 2)

        obj.y = 5
        self.assertEqual(obj.y, 5)

        with self.assertRaises(TypeError):
            obj.y = "invalid"

        # y can be set to negative values
        obj.y = -3
        self.assertEqual(obj.y, -3)

if __name__ == "__main__":
    unittest.main()
