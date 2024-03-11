#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    __class = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

    def do_help(self, line):
        """Show help message"""
        super().do_help(line)

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            instance = storage.get_object_by_id(class_name, instance_id)
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            instance = storage.get_object_by_id(class_name, instance_id)
            if instance:
                storage.delete_object(instance)
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = eval(arg).__name__
                filtered_objs = [str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name]
                print(filtered_objs)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id (BaseModel or User)"""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = eval(args[0]).__name__
            if class_name == "User":
                class_name = "models.user.User"
            instance_id = args[1]
            instance = storage.get_object_by_id(class_name, instance_id)

            if instance:
                if len(args) < 4:
                    if len(args) == 2:
                        print("** instance id missing **")
                    elif len(args) == 3:
                        print("** attribute name missing **")
                else:
                    attr_name = args[2]
                    attr_value_str = args[3]

                    # Check if the attribute name is valid
                    if not hasattr(instance, attr_name):
                        print("** attribute doesn't exist **")
                        return

                    # Cast the attribute value to the attribute type
                    attr_type = type(getattr(instance, attr_name))
                    try:
                        attr_value = attr_type(attr_value_str.strip('"'))
                        setattr(instance, attr_name, attr_value)
                        instance.save()
                    except ValueError:
                        print("** invalid value **")
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = eval(arg).__name__
            if class_name == "User":
                class_name = "models.user.User"
            count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == class_name)
            print(count)
        except NameError:
            print("** class doesn't exist **")

      
if __name__ == '__main__':
    HBNBCommand().cmdloop()

