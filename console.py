#!/usr/bin/python3

"""HBNBCommand module"""

# import cmd

# import models
# from models.base_model import BaseModel
# from models.user import User
# from models.amenity import Amenity
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State

# from models.engine.file_storage import FileStorage


# class HBNBCommand(cmd.Cmd):
#     """cmd class"""
#     prompt = '(hbnb) '
#     file = 'file.json'
#     classes = ['BaseModel', 'User', 'State',
#                'Review', 'City', 'Place', 'Amenity']
#     # needs another argument to see what action to be taken

#     def do_quit(self, arg):
#         """Quit command to exit the program"""
#         return True

#     def do_help(self, arg: str):
#         """"""
#         return super().do_help(arg)

#     def do_EOF(self, arg):
#         """Exits the program."""
#         return True

#     def emptyline(self):
#         """an empty line + ENTER shouldnt execute anything"""
#         # return super().emptyline()
#         pass

#     def do_create(self, arg):
#         """
#         Creates a new instance of BaseModel,
#         saves it (to the JSON file) and prints the id
#         """
#         if not arg:
#             print("** class name missing **")
#         elif arg not in self.classes:
#             print("** class doesn't exist **")
#         else:
#             obj = eval(arg + "()")
#             # remember this saves instances
#             obj.save()
#             print(obj.id)

#     def do_show(self, arg):
#         """
#         Prints the string representation of an instance
#         based on the class name and id
#         """
#         # arg contains the spaces too, so we need to remove them
#         # we need to format the arg to be a proper array
#         if type(arg) == str:
#             arg_list = arg.split(" ")
#         else:
#             arg

#         if not arg:
#             print("** class name missing **")
#             return

#         elif arg_list[0] not in self.classes:
#             print("** class doesn't exist **")
#             return

#         # check the length of the arg, we are expecting to be 2
#         if len(arg_list) < 2:
#             print("** instance id missing **")
#             return
#         else:
#             obj_id = arg_list[0] + '.' + arg_list[1]
#             data = models.storage.all().get(obj_id)
#             if data is None:
#                 print("** no instance found **")
#                 return

#             else:
#                 return print(data)

#     def do_destroy(self, arg):
#         """
#         Deletes an instance based on the class name and id
#         (save the change into the JSON file).
#         """
#         if type(arg) == str:
#             arg_list = arg.split(" ")
#         else:
#             arg

#         if not arg:
#             print("** class name missing **")
#             return

#         elif arg_list[0] not in self.classes:
#             print("** class doesn't exist **")
#             return

#         # check the length of the arg, we are expecting to be 2
#         elif len(arg_list) < 2:
#             print("** instance id missing **")
#             return

#         else:
#             obj_id = arg_list[0] + '.' + arg_list[1]
#             data = models.storage.all().get(obj_id)
#             if data is None:
#                 print("** no instance found **")
#                 return
#             else:
#                 models.storage.all().pop(obj_id)
#                 data = models.storage.all().get(obj_id)
#                 if data is None:
#                     models.storage.save()
#                     # return print("deleted")

#     def do_all(self, arg):
#         """
#         Prints all string representation of all instances
#         based or not on the class name. Ex: $ all BaseModel or $ all
#         * The printed result must be a list of strings
#         """
#         if type(arg) == str:
#             arg_list = arg.split(" ")
#         else:
#             arg

#         obj_list = []

#         # if arg is None:
#         #     data = models.storage.all()
#         #     for key in data:
#         #         # obj_list.append(str(data[key]))
#         #         print([str(data[key])])

#         if arg_list[0] in self.classes or not arg:
#             data = models.storage.all()
#             for key, value in data.items():
#                 key = key.split('.')[0]  # this doesnt id part
#                 if key == arg:
#                     obj_list.append(str(value))
#                     print(obj_list)
#                 else:
#                     obj_list.append(str(value))
#                     print(obj_list)
#         else:
#             print("** class doesn't exist **")

#             # if obj["__class__"] == "BaseModel":
#             #     obj_list.append(obj)

#     def do_update(self, arg):
#         """
#         Updates an instance based on the class name and
#         id by adding or updating attribute
#         """

#         if type(arg) == str:
#             arg_list = arg.split(" ")
#         else:
#             arg

#         if not arg:
#             print("** class name missing **")
#             return

#         elif arg_list[0] not in self.classes:
#             print("** class doesn't exist **")
#             return

#         # check the length of the arg, we are expecting to be 2
#         elif len(arg_list) < 2:
#             print("** instance id missing **")
#             return

#         obj_id = arg_list[0] + '.' + arg_list[1]
#         data = models.storage.all().get(obj_id)
#         if data is None:
#             print("** no instance found **")
#             return

#         if len(arg_list) == 2:
#             print('** attribute name missing **')
#             return
#         elif len(arg_list) == 3:
#             print('** value missing **')
#             return

#         """here starts the updating part"""

#         # this helps remove the double qoutes from arguments, when entered
#         value = eval(arg_list[3])
#         setattr(data, arg_list[2], value)
#         models.storage.save()

#         # value = getattr(data, arg_list[2])
#         # if value is None:
#         #     data.arg_list[2] = arg_list[3]
#         # else:
#         #     if hasattr(data, arg)

#     # this does all the commands
#     def default(self, line):
#         """
#         Recieves class name + . + command + ()
#         """
#         if '.' in line:
#             arg_list = line.split(".")
#             className = arg_list[0]
#             a = arg_list[1].split("()")
#             b = a[0].split("(")
#             method = b[0]
#             if len(b) > 1:
#                 if "'" in b[1]:
#                     c = b[1].split("'")
#                     argument = c[1]
#                 elif '"' in b[1]:
#                     c = b[1].split('"')
#                     argument = c[1]
#                 if len(c) > 3:
#                     if c[3] is not None:
#                         attribute = c[3]

#                     if c[4] != ',':
#                         z = c[4].split(')')
#                         y = z[0].split(', ')
#                         value = y[1]
#                         if len(value) > 0:
#                             print(value)

#                         else:
#                             value = '"' + c[5] + '"'
#                             print(value)

#             if className in self.classes:
#                 if method == 'all':
#                     self.do_all(className)
#                 if method == "count":
#                     data = models.storage.all()
#                     dataKeys = data.keys()
#                     onlyKeys = []
#                     for key in dataKeys:
#                         keys = key.split(".")
#                         onlyKeys.append(keys[0])
#                     count = 0
#                     for key in onlyKeys:
#                         if key == className:
#                             count = count + 1
#                     # return or print outside the loop
#                     print(count)
#                 if method == "show":
#                     self.do_show(className + ' ' + argument)
#                 if method == "destroy":
#                     self.do_destroy(className + ' ' + argument)
#                 if method == "update":
#                     self.do_update(className + ' ' + argument +
#                                    ' ' + attribute + ' ' + value)


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity


from models import storage


class HBNBCommand(cmd.Cmd):
    '''creating a console'''
    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'City': City, 'Place': Place, 'Review': Review, 'Amenity': Amenity}

    def do_help(self, line):
        ''''List available commands with "help" or detailed help with "help cmd" '''
        if not line:

            print('Documented commands (type help <topic>):\n'
                  '========================================\n'
                  'EOF  help  quit\n')

        if line == 'quit':
            print('Quit command to exit the program')
            print(line)
        else:
            print(line)

    def emptyline(self):
        '''does nothing on an empty line + ENTER'''
        pass

    def do_quit(self, line):
        '''quits console'''
        return True

    def do_EOF(self, line):
        '''quits console'''
        return True

    def do_create(self, line):
        '''
            creates instances of classes, then saves it in json
            Ex: $ create BaseModel
        '''
        '''
            line is a list of args.
            line = [classname, id]
            line[0] = c
            line[1] = l
            For this reason, we need to parse the line
        '''
        commands = line.split(' ')  # list with all the args passed
        key = commands[0]  # classname

        if not key:
            print('** class name missing **')

        elif key not in self.classes.keys():
            print('** class doesn\'t exist **')

        else:
            className = self.classes[key]
            obj = className()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        ''' 
            Prints the string representation of an instance based on the class name and id
            Ex: $ show BaseModel 1234-1234-1234.
        '''
        commands = line.split(' ')  # list with all the args passed
        key = commands[0]  # classname

        if not key:
            print('** class name missing **')

        elif key not in self.classes.keys():
            print('** class doesn\'t exist **')

        elif len(commands) < 2:
            print('** instance id missing **')

        else:
            idd = commands[1]
            classnameId = key + '.' + idd
            all_objs = storage.all()

            if classnameId not in all_objs.keys():
                print('** no instance found **')
            else:
                for k, v in all_objs.items():
                    if k == classnameId:
                        print(v)

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """

        commands = line.split(' ')
        key = commands[0]
        if not key:
            allObjList = []
            all_objs = storage.all()
            for obj, v in all_objs.items():
                allObjList.append(f"{v}")
            print(allObjList)

        else:

            objList = []
            key = commands[0]
            if key not in self.classes.keys():
                print('** class doesn\'t exist **')

            all_objs = storage.all()
            for k, v in all_objs.items():
                classname_Id = k.split('.')
                classname = classname_Id[0]
                if classname == key:
                    objList.append(f'{v}')
            print(objList)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        commands = line.split(' ')  # list with all the args passed
        key = commands[0]  # classname

        if not key:
            print('** class name missing **')

        elif key not in self.classes.keys():
            print('** class doesn\'t exist **')

        elif len(commands) < 2:
            print('** instance id missing **')

        else:
            idd = commands[1]
            classnameId = key + '.' + idd
            all_objs = storage.all()

            if classnameId not in all_objs.keys():
                print('** no instance found **')
            else:

                del all_objs[classnameId]
                storage.save()

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        commands = line.split(' ')
        key = commands[0]

        if not key:
            print('** class name missing **')

        elif key not in self.classes:
            print('** class doesn\'t exist **')

        elif len(commands) < 2:
            print('** instance id missing **')

        elif len(commands) < 3:
            print('** attribute name missing **')

        elif len(commands) < 4:
            print('** value missing **')

        else:
            idd = commands[1]
            attr = commands[2]
            val = commands[3].strip('"')

            classnameId = key + '.' + idd
            all_objs = storage.all()

            if classnameId not in all_objs.keys():
                print('** no instance found **')
            else:
                for k, v in all_objs.items():
                    if k == classnameId:
                        setattr(v, attr, val)
                        storage.save()

    def default(self, line):
        args = line.split('.')
        key = args[0]
        methodID = args[1].split('(')
        method = methodID[0]
        idd = methodID[1].removesuffix(')').removeprefix('"').removesuffix('"')

        noIdMethods = {'all': self.do_all, 'create': self.do_create}

        idMethods = {'show': self.do_show,
                     'destroy': self.do_destroy}

        update = {'update': self.do_update}

        if key in self.classes:

            if method in idMethods:
                if idd:
                    for k, v in idMethods.items():
                        if k == method:
                            linee = key + ' ' + idd
                            v(linee)

            elif method in noIdMethods:
                for k, v in noIdMethods.items():
                    if k == method:
                        v(key)

            elif method == 'count':
                all_objs = storage.all()
                clsNameList = []
                for k, v in all_objs.items():
                    classname = k.split('.')[0]
                    clsNameList.append(classname)
                c = clsNameList.count(key)
                print(c)

            else:
                # update method
                idAttrVal = methodID[1].split(',')  # this is a list now
                idd = idAttrVal[0].replace('"', '')
                attr = idAttrVal[1].replace(' "', '').removesuffix('"')
                val = idAttrVal[2].replace(' "', '')
                val = val.replace('")', '')
                v = update[method]
                linee = key + ' ' + idd + ' ' + attr + ' ' + val
                v(linee)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
