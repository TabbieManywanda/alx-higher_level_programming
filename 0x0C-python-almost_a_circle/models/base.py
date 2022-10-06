#!/usr/bin/python3
"""The class that will manage id attribute in all future
classes to avoid duplication"""


import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing instance"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of `list_dictionaries`"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation
        of `list_objs` to a file"""
        filename = cls.__name__ + ".json"
        objlist = []
        if list_objs is not None:
            for x in list_objs:
                objlist.append(cls.to_dictionary(x))
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(objlist))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation
        `json_string`"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes
        all set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
