#!/usr/bin/python3
""" a function that Sends a request and display a response """
import requests
from sys import argv
if __name__ == "__main__":
    q = "" if len(argv) == 1 else argv[1]
    data = {'q': q}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=data).json()
        if 'id' in r and 'name' in r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
