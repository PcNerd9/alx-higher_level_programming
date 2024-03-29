#!/usr/bin/python3
"""
sends a POST request to the passed url and the eamil as a parameter
"""


def main():
    import sys
    import urllib.request
    import urllib.parse

    try:
        email = sys.argv[2]
        url = sys.argv[1]
        data = {"email": email}
        data = urllib.parse.urlencode(data)
        data = data.encode("ascii")
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            print(response.read())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
