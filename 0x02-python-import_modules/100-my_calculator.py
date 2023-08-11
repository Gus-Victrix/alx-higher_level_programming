#!/usr/bin/python3

if __name__ == '__main__':
    """Make some calcule :
            syntaxe : Usage: ./100-my_calculator.py <a> <operator> <b>"""
    from calculator_1 import add, sub, mul, div
    import sys
    numOfArg = len(sys.argv)
    if numOfArg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
        elif sys.argv[2] == '-':
            print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
