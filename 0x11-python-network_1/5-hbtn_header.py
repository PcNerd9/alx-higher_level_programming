#!/usr/bin/python3
"""
sends a request to the url and display the value of the variable
"""


def main():
    import sys
    import requests

    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
