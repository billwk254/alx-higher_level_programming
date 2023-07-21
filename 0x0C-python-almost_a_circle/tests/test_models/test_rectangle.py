#!/usr/bin/python3


"""
Test module for Rectangle class.
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_inheritance(self):
        """
        Test if Rectangle inherits from Base.
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_attributes(self):
        """
        Test the attributes of Rectangle class.
        """
        r = Rectangle(5, 10, 2, 4, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 1)

    def test_width_type_error(self):
        """
        Test width attribute with non-integer value.
        """
        with self.assertRaises(TypeError):
            r = Rectangle("width", 10)

    def test_width_value_error(self):
        """
        Test width attribute with value less than or equal to 0.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)

    def test_height_type_error(self):
        """
        Test height attribute with non-integer value.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(5, "height")

    def test_height_value_error(self):
        """
        Test height attribute with value less than or equal to 0.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(5, 0)

    def test_x_type_error(self):
        """
        Test x attribute with non-integer value.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "x", 4)

    def test_x_value_error(self):
        """
        Test x attribute with value less than 0.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -2, 4)

    def test_y_type_error(self):
        """
        Test y attribute with non-integer value.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 2, "y")

    def test_y_value_error(self):
        """
        Test y attribute with value less than 0.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 2, -4)

    def test_area(self):
        """
        Test the area method of Rectangle.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """
        Test the display method of Rectangle.
        """
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch("sys.stdout", new=unittest.mock.StringIO()) as output:
            r.display()
            self.assertEqual(output.getvalue(), expected_output)

    def test_str(self):
        """
        Test the __str__ method of Rectangle.
        """
        r = Rectangle(5, 10, 2, 4, 1)
        expected_str = "[Rectangle] (1) 2/4 - 5/10"
        self.assertEqual(str(r), expected_str)

    def test_update_args(self):
        """
        Test the update method with *args.
        """
        r = Rectangle(5, 10, 2, 4, 1)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_kwargs(self):
        """
        Test the update method with **kwargs.
        """
        r = Rectangle(5, 10, 2, 4, 1)
        r.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_args_kwargs(self):
        """
        Test the update method with *args and **kwargs (should prioritize **kwargs).
        """
        r = Rectangle(5, 10, 2, 4, 1)
        r.update(10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)


if __name__ == "__main__":
    unittest.main()
