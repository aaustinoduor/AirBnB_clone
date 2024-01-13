#!/usr/bin/env python3
"""Acts as the main entry point for the backend
For development and Debugging purposes
"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Creates a command processor instance object."""
    prompt = '(hbnb)'

    def do_help(self, arg):
        """Get help on commands"""
        if arg:
            super().do_help(arg)
            self.stdout.write('\n')
        else:
            self.stdout.write('\n')
            super().do_help(arg)

    def do_quit(self, arg):
        """quits the interpreter"""
        return sys.exit

    def do_EOF(self, arg):
        """Waits for EOF signal"""
        return True

    def do_create(self, arg):
        """Creates a BaseModel instance saves it to json
        and prints the id
        """
        my_obj = BaseModel()
        my_obj.save()  # Save to storage does not work
        print(my_obj.to_dict().get('id'))

    def postloop(self):
        """Checks if the input is from terminal or not"""
        if not sys.stdin.isatty():
            print()
            return

    def emptyline(self):
        """Handles empty lines"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
