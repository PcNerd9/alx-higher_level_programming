#!/usr/bin/python3

from calculator_1 import *
from sys import argv, exit

operator = ['+', '-', '*', '/']
no_args = len(argv)
if (no_args != 4):
    print("Usage: {} <a> operator <b>".format(argv[0]))
    exit(1)
elif (argv[2] not in operator):
    print(argv[2])
    print("Unkown operator. Available operators: +, -, * and /")
    exit(1)

a = int(argv[1])
b = int(argv[3])

match argv[2]:
    case '+':
        result = add(a, b)
    case '-':
        result = sub(a, b)
    case '*':
        result = mul(a, b)
    case '/':
        result = div(a, b)
print("{} + {} = {}".format(a, b, result))
exit(0)
