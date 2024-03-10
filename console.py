#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    """Command interpreter"""
    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def emptyline(self, line):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
