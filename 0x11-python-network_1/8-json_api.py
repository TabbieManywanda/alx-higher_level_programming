#!/usr/bin/python3
'''takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter
as a parameter'''

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {"q": q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        data = r.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get('id'), data.get('name')))
    except ValueError:
        print("Not a valid JSON")
