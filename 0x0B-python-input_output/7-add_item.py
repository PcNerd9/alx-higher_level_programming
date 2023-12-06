#!/usr/bin/python3

"""
contain only one function
"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import sys
import json


def main():
    """
    add all arguments to a python list and then
    save them to a file
    """
    python_list = load_from_json_file("add_item.json")
    save_to_json_file(python_list + sys.argv[1:], "add_item.json")
    print(load_from_json_file("add_item.json"))

if __name__ == "__main__":
    main()
