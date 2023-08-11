#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    """Print the content of hidden_4, exect name start with '__'"""

    for name in dir(hidden_4):
        if (name[0] != '_') and (name[1] != '_'):
            print("{:s}".format(name))
