#!/usr/bin/python3
""" a function that fetches a URL """

import urllib.request
from sys import argv
if __name__ == "__main__":
    with urllib.request.urlopen(urllib.request.Request(argv[1])) as response:
        print(response.headers.get('X-Request-Id'))
