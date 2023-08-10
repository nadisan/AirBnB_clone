#!/usr/bin/python3
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
