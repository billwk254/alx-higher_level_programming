#!/usr/bin/python3

"""
test_base.py - Unit tests for the Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    TestBase - Test cases for the Base class.
    """

    def test_id_assignment(self):
        """
        Test id assignment when 'id' is provided and when 'id' is not provided.
        """
        obj1 = Base(10)
        self.assertEqual(obj1.id, 10)

        obj2 = Base()
        self.assertEqual(obj2.id, 1)

    def test_documentation(self):
        """
        Test if the Base class and its methods are documented properly.
        """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)

if __name__ == "__main__":
    unittest.main()
