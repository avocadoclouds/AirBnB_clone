#!/usr/bin/python3

"""HBNBCommand module"""

import cmd

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """cmd class"""
    prompt = '(hbnb) '
    file = 'file.json'

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
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
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

        elif arg_list[0] != "BaseModel":
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

        elif arg_list[0] != "BaseModel":
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

        if arg_list[0] == "BaseModel" or not arg:
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

        elif arg != "BaseModel":
            print("** class doesn't exist **")

        # check the length of the arg, we are expecting to be 2
        if len(arg_list) == 1:
            print("** instance id missing **")
        else:
            obj_id = arg_list[0] + '.' + arg_list[1]
            data = models.storage.all().get(obj_id)
            if data is None:
                print("** no instance found **")

        if len(arg_list) == 2:
            print('** attribute name missing **')
        elif len(arg_list) == 3:
            print('** value missing **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
