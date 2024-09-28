#!/usr/bin/python3
"""
sendsa POST requests to a url with a letter as a parameter
"""


def main():
    import sys
    import requests
    
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": sys.argv[1]}
    response = requests.post(url, data)

    try:
        json_data = response.json()
        if json_data:
            for key, value in json_data.items():
                print("[{}] {}".format(key, value))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
   
