#!/usr/bin/python3
"""
a module with class
"""
import json
from os import path

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    a class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    # private attributes
    __file_path = "file.json"
    __objects = {}  # {BaseModel.12: value, BaseModel.10: value}

    # public methods

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets the obj in __objects
        with the key <obj class name>.id
        """

        # we are formating the key to be the objs'class name
        # and the id
        # to achieve that we need to find the type of obj,
        # type(obj) will return to the class which the obj belongs to
        # then we need the name of the class
        # then we need the id of the obj
        # finally we need to add the edited key to __objects ->
        # with the value of obj

        # key = '{}.{}'.format(type(obj).__name__, obj.id)
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (__file_path)
        """

        # This won't work:
        """
        jsonn = json.dumps(self.__objects)
        with open(self.__file_path, "w") as f:
            f.write(jsonn)
        """

        # Note: the 'value' of the key in dictionery
        #      here is an instance of class and
        #      we can't serialise an instance so, we need to generate
        #      a dictionary of that instance using the method .to_dict
        #      then we assign the dictionary back to the key, then
        #      we serialise the file.

        dic_storage = {}
        for key, value in self.__objects.items():
            dic_storage[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as file_json:
            file_json.write(json.dumps(dic_storage))

    def reload(self):
        """
        if __file_path (json file) exits:
            deserialises the json file to __objects
        else:
            does nothing, no exceptions
        """

        # check if __file_path exists
        if path.exists(self.__file_path):
            # Note: now the value which a dictionary,
            #  now is deserialised

            with open(self.__file_path, 'r', encoding="utf-8") as f:

                """
                '**' takes a dict and extracts its contents
                and passes them as parameters to a function.
                Take this function for example:

                def func(a=1, b=2, c=3):
                    print a
                    print b
                    print b
                Now normally you could call this function like this:
                    func(1, 2, 3)
                But you can also populate a dictionary with
                those parameters stored like so:
                    params = {'a': 2, 'b': 3, 'c': 4}
                Now you can pass this to the function:
                    func(**params) ** means kwargs
                """

                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    # self.__objects[k] = eval(v['__class__'])(**v) <-- this works
                    self.__objects[k] = BaseModel(**v) # wanted to see if this works too
