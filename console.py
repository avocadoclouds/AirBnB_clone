#!/usr/bin/python3

"""HBNBCommand module"""

import cmd

import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """cmd class"""
    prompt = '(hbnb) '
    file = 'file.json'
    classes = ['BaseModel', 'User', 'State',
               'Review', 'City', 'Place', 'Amenity']
    # needs another argument to see what action to be taken

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, arg: str):
        """"""
        return super().do_help(arg)

    def do_EOF(self, arg):
        """Exits the program."""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        # return super().emptyline()
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg + "()")
            # remember this saves instances
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        # arg contains the spaces too, so we need to remove them
        # we need to format the arg to be a proper array
        if type(arg) == str:
            arg_list = arg.split(" ")
        else:
            arg

        if not arg:
            print("** class name missing **")
            return

        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return

        # check the length of the arg, we are expecting to be 2
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        else:
            obj_id = arg_list[0] + '.' + arg_list[1]
            data = models.storage.all().get(obj_id)
            if data is None:
                print("** no instance found **")
                return

            else:
                return print(data)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        if type(arg) == str:
            arg_list = arg.split(" ")
        else:
            arg

        if not arg:
            print("** class name missing **")
            return

        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return

        # check the length of the arg, we are expecting to be 2
        elif len(arg_list) < 2:
            print("** instance id missing **")
            return

        else:
            obj_id = arg_list[0] + '.' + arg_list[1]
            data = models.storage.all().get(obj_id)
            if data is None:
                print("** no instance found **")
                return
            else:
                models.storage.all().pop(obj_id)
                data = models.storage.all().get(obj_id)
                if data is None:
                    models.storage.save()
                    # return print("deleted")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        * The printed result must be a list of strings
        """
        if type(arg) == str:
            arg_list = arg.split(" ")
        else:
            arg

        obj_list = []

        # if arg is None:
        #     data = models.storage.all()
        #     for key in data:
        #         # obj_list.append(str(data[key]))
        #         print([str(data[key])])

        if arg_list[0] in self.classes or not arg:
            data = models.storage.all()
            for key, value in data.items():
                key = key.split('.')[0]  # this doesnt id part
                if key == arg:
                    obj_list.append(str(value))
                    print(obj_list)
                else:
                    obj_list.append(str(value))
                    print(obj_list)
        else:
            print("** class doesn't exist **")

            # if obj["__class__"] == "BaseModel":
            #     obj_list.append(obj)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """

        if type(arg) == str:
            arg_list = arg.split(" ")
        else:
            arg

        if not arg:
            print("** class name missing **")
            return

        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return

        # check the length of the arg, we are expecting to be 2
        elif len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_id = arg_list[0] + '.' + arg_list[1]
        data = models.storage.all().get(obj_id)
        if data is None:
            print("** no instance found **")
            return

        if len(arg_list) == 2:
            print('** attribute name missing **')
            return
        elif len(arg_list) == 3:
            print('** value missing **')
            return

        """here starts the updating part"""

        # this helps remove the double qoutes from arguments, when entered
        value = eval(arg_list[3])
        setattr(data, arg_list[2], value)
        models.storage.save()

        # value = getattr(data, arg_list[2])
        # if value is None:
        #     data.arg_list[2] = arg_list[3]
        # else:
        #     if hasattr(data, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
