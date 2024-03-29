#!/usr/bin/python3
"""
sends a request to the url and display the pody of the response
"""


def main():
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode("utf-8"))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
