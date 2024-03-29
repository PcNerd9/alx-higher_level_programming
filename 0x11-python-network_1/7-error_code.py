#!/usr/bin/python3
"""
sends a requests to a url and display response data
"""


def main():
    import sys
    import requests

    response = requests.get(sys.argv[1])
    if (response.status_code >= 400):
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
