#!/usr/bin/python3
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    """Command interpreter"""
    def do_EOF(self, line):
        """ EOF command to exit the program """
        print()
        return True
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def emptyline(self, line):
        """ print nothing on empty line """
        pass
    def do_help(self, arg):
        """Show help message"""
        super().do_help(arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
