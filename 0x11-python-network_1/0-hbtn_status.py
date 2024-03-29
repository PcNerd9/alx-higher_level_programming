#!/usr/bin/python3
"""
fetchs the url and print the response in a particular format
"""


def main():
    """
    the main program
    """
    import urllib.request

    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        the_page = response.read()
        utf8_content = the_page.decode("utf-8")

    print("Body response:")
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
    print("\t- utf8 content: {}".format(utf8_content))


if __name__ == "__main__":
    main()
