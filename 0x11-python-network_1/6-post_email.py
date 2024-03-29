#!/usr/bin/python3
"""
sends a post request to url
"""


def main():
    import sys
    import requests

    value = sys.argv[2]
    url = sys.argv[1]
    data = {"email": value}
    response = requests.post(url, data)
    print(response.text)


if __name__ == "__main__":
    main()
