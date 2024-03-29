#!/usr/bin/python3
"""
fetches a url using request library
"""


def main():
    import requests
    import sys

    response = requests.get("https://alx-intranet.hbtn.io/status")
    response.encoding = "utf-8"
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
