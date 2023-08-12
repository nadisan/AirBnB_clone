#!/usr/bin/python3
"""This HBNBCommand class"""
import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel
from shlex import split
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(line: str):
    """Splits lines by spaces"""
    args = shlex.split(line)
    return args, len(args)


class HBNBCommand(cmd.Cmd):
    """ A program that contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D or Ctrl+Z."""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, line):
        """
        Creates a new BaseModel instance,
        saves it to the JSON file and prints the id
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
            string = line + "()"
            instance = eval(string)
            print(instance.id)
            instance.save()
        except Exception as e:
            print("** class doesn't exist **")

    def help_quit(self):
        ''' help_quit '''
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """help_EOF"""
        print("End of File command: exit the program\n")

    def do_show(self, line):
        """Prints an instance as a string based on the class and id"""
        className_line = line.split()
        if len(className_line) == 0:
            print("** class name missing **")
            return
        elif className_line[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        elif len(className_line) == 2:
            instance = className_line[0] + "." + className_line[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class and id"""
        className_line = line.split()
        if len(className_line) == 0:
            print("** class name missing **")
            return
        elif className_line[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        elif len(className_line) == 2:
            instance = className_line[0] + "." + className_line[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        className_line = shlex.split(arg)
        obj_list = []
        if len(className_line) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif className_line[0] in HBNBCommand.classes.keys():
            for key in models.storage.all():
                if className_line[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class name, id, attribute & value"""
        className_line = line.split()
        staticArray = ["id", "created_at", "updated_at"]
        objects = models.storage.all()
        if not line:
            print("** class name missing **")
        elif className_line[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        else:
            instance = className_line[0] + "." + className_line[1]
            if instance not in models.storage.all():
                print("** no instance found **")
            elif len(className_line) < 3:
                print("** attribute name missing **")
            elif len(className_line) < 4:
                print("** value missing **")
            elif className_line[2] not in staticArray:
                ojb = objects[instance]
                ojb.__dict__[className_line[2]] = className_line[3]
                ojb.updated_at = datetime.now()
                ojb.save()
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }


if __name__ == '__main__':
    HBNBCommand().cmdloop()
