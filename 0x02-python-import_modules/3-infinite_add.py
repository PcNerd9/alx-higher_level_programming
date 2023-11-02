#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    total_sum = 0
    total_args = len(argv)
    if (total_args >= 2):
        for i in range(1, total_args):
            total_sum = total_sum + int(argv[i])
    print(total_sum)
