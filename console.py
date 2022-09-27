#!/usr/bin/python3

"""HBNBCommand module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """cmd class"""
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
