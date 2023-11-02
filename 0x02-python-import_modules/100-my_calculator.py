#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    operator = ['+', '-', '*', '/']
    no_args = len(argv)
    if (no_args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (argv[2] not in operator):
        print(argv[2])
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    result = 0
    match argv[2]:
        case '+':
            result = add(a, b)
        case '-':
            result = sub(a, b)
        case '*':
            result = mul(a, b)
        case '/':
            result = div(a, b)
    print("{} {} {} = {}".format(a, argv[2], b, result))
    exit(0)
