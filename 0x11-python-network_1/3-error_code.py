#!/usr/bin/python3
""" a function that fetches a URL """

import urllib.request as request
import urllib.error as error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(request.Request(argv[1])) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
            print("Error code: {}".format(err.code))
