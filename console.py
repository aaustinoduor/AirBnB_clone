#!/usr/bin/env python3
"""Acts as the main entry point for the backend
For development and Debugging purposes
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Creates a command processor instance object."""
    prompt = '(hbnb)'

    def do_help(self, arg):
        """Get help on commands"""
        if arg:
            super().do_help(arg)
        else:
            self.stdout.write('\n')
            super().do_help(arg)

    def do_quit(self, line):
        """quits the interpreter"""
        return sys.exit

    def postloop(self):
        """Checks if the input is from terminal or not"""
        if not sys.stdin.isatty():
            print()
            return

    def emptyline(self):
        """Handles empty lines"""
        return

    def do_EOF(self, line):
        """Waits for EOF signal"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
