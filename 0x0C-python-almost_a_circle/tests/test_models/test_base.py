#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_creation(self):
        # Test if the id is incremented correctly
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_custom_id(self):
        # Test if the custom id is assigned correctly
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_to_json_string(self):
        data = [{"key": "value"}, {"key2": "value2"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, json.dumps(data))

        result = Base.to_json_string(None)
        self.assertEqual(result, '[]')

        result = Base.to_json_string([])
        self.assertEqual(result, '[]')


if __name__ == '__main__':
    unittest.main()
