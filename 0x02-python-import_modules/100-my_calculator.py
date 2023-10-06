#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    operator = {
            '*': mul,
            '+': add,
            '-': sub,
            '/': div
            }
    length = len(sys.argv)
    if length - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] not in operator:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            func = operator[sys.argv[2]]
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[3])
            result = func(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(int(num1, sys.argv[2], num2, result)))
    exit(0)
