#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argv_len = len(sys.argv)
    if argv_len == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operators = {"+": add, "-": sub, "*": mul, "/": div}

        if sys.argv[2] not in list(operators.keys()):
            sys.exit("Unknown operator. Available operators: +, -, * and /")
        else:
            print("{} {} {} = {}".format(a, sys.argv[2], b, operators[sys.argv[2]](a, b)))
    else:
        sys.exit("Usage: ./100-my_calculator.py <a> <operator> <b>")
