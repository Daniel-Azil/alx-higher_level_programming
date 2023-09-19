import unittest
import io
from unittest import mock
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_create_rectangle(self):
        # Test if you can create a rectangle instance
        rectangle = Rectangle(5, 10)
        self.assertIsInstance(rectangle, Rectangle)

    def test_rectangle_attributes(self):
        # Test rectangle attributes after creation
        rectangle = Rectangle(5, 10, 2, 3, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 10)

    def test_area(self):
        # Test the area method
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_update(self):
        # Test updating rectangle attributes
        rectangle = Rectangle(5, 10, 2, 3, 10)
        rectangle.update(7, 8, 9, 11, 12)
        self.assertEqual(rectangle.id, 7)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 9)
        self.assertEqual(rectangle.x, 11)
        self.assertEqual(rectangle.y, 12)

    def test_to_dictionary(self):
        # Test conversion to dictionary
        rectangle = Rectangle(5, 10, 2, 3, 10)
        rectangle_dict = rectangle.to_dictionary()
        expected_dict = {
            "id": 10,
            "width": 5,
            "height": 10,
            "x": 2,
            "y": 3
        }
        self.assertEqual(rectangle_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
