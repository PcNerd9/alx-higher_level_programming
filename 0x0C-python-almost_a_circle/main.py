#!/usr/bin/python3
""" 15-main """
from models.base import Base

if __name__ == "__main__":

    r1 = Base(8)
    r2 = Base()
    Base.save_to_file([r1, r2])

    with open("Base.json", "r") as file:
        print(file.read())
