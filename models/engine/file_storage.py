"""
a module with class
"""
from genericpath import exists
import json
from models.base_model import BaseModel


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

        key = '{}.{}'.format(type(obj).__class__.__name__, obj.id)
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
        jsonn = json.dumps(dic_storage)
        with open(self.__file_path, "w") as file_json:
            file_json.write(jsonn)

    def reload(self):
        """
        if __file_path (json file) exits:
            deserialises the json file to __objects
        else:
            does nothing, no exceptions
        """

        # check if __file_path exists
        try:
            if exists(self.__file_path):
                # Note: now the value which a dictionary,
                #  now is deserialised
                with open(self.__file_path) as json_file:
                    obj_dict = json.load(json_file)
                    for key, value in obj_dict.items():
                        # explanation for this!!!
                        obj_dict = eval(value['__class__'])(**value)
                        self.__objects[key] = obj_dict

        except FileNotFoundError:
            return
