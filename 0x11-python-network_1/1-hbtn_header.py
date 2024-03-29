#!/usr/bin/python3
"""
sends a request to a url and display the value of the header variable
"""


def main():
    """
    the entry to the main program
    """
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            value = response.headers["X-Request-Id"]
    except Exception as e:
        print(e)
    else:
        print(value)


if __name__ == "__main__":
    main()
