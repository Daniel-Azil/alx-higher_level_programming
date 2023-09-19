import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_create_square(self):
        # Test if you can create a square instance
        square = Square(5)
        self.assertIsInstance(square, Square)

    def test_square_attributes(self):
        # Test square attributes after creation
        square = Square(5, 2, 3, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 10)

    def test_update_square(self):
        # Test updating square attributes
        square = Square(5, 2, 3, 10)
        square.update(7, 8, 9, 11)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 9)
        self.assertEqual(square.y, 11)

    def test_to_dictionary(self):
        # Test conversion to dictionary
        square = Square(5, 2, 3, 10)
        square_dict = square.to_dictionary()
        expected_dict = {
            "id": 10,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
