#!/usr/bin/python3

""" A custom module """
import json
import csv


class Base():
    """ A class containing method that counts
        the number of times the class 'Base' is
        instanciated
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor for the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A custom static method that serialises given dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        if list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ A custom method that saves list objescts of serialised
            JSON object to a file
        """
        name_f = cls.__name__ + ".json"
        with open(name_f, "w") as file:
            if list_objs is None:
                json.write("[]")
            else:
                list_dicts = [element.to_dictionary() for element in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ A custom method that returns the list of the
            serialised JSON string
        """
        if json_string is None:
            return []
        if json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ A class method that  that returns an instance with all
            attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                values = cls(1, 1)
            else:
                values = cls(1)
            values.update(**dictionary)
            return values

    @classmethod
    def load_from_file(cls):
        """ A method that returns a list of instances"""
        name_f = str(cls.__name__) + ".json"
        try:
            with open(name_f, "r") as file:
                ls = Base.from_json_string(file.read())
                return [cls.create(**element) for element in ls]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ A custom class method that that serializes and deserializes in CSV
        """
        name_f = cls.__name__ + ".csv"
        with open(name_f, "w", newline="") as csv_file:
            if list_objs is None:
                csv_file.write("[]")
            elif list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    args = ["id", "width", "height", "x", "y"]
                else:
                    args = ["id", "size", "x", "y"]
                input_wr = csv.DictWriter(csv_file, fieldnames=args)
                for element in list_objs:
                    input_wr.writerow(element.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ A custom class method that loads a csv file """
        name_f = cls.__name__ + ".csv"
        try:
            with open(name_f, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    args = ["id", "width", "height", "x", "y"]
                else:
                    args = ["id", "size", "x", "y"]
                ls = csv.DictReader(csv_file, fieldnames=args)
                ls = [dict([arg1, int(arg2)]
                      for arg1, arg2 in ele.items()) for ele in ls]
                return [cls.create(**vv) for vv in ls]

        except IOError:
            return []
