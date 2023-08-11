#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print all given argu"""

    numOfArg = len(sys.argv)
    if (numOfArg == 1):
        print("0 arguments.")
    elif numOfArg == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(numOfArg - 1))
        for i in range(1, numOfArg):
            print("{}: {}".format(i, sys.argv[i]))
