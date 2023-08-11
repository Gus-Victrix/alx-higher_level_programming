#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Add all the given argu"""

    numOfArgu = len(sys.argv)
    if numOfArgu == 1:
        print('0')
    else:
        sum = 0
        for i in range(1, numOfArgu):
            sum += int(sys.argv[i])
        print("{:d}".format(sum))
