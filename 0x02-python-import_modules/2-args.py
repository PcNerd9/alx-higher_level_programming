#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    no_args = len(argv)
    if no_args == 1:
        print("{} arguments.".format(no_args - 1))
    else:
        if (no_args == 2):
            print("{} argument:".format(no_args - 1))
        else:
            print("{} arguments:".format(no_args - 1))
        for i in range(1, no_args):
            print("{}: {}".format(i, argv[i]))
