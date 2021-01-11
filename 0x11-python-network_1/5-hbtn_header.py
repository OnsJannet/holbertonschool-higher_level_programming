#!/usr/bin/python3
""" a function that fetches a URL """
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get((argv[1])
    print(r.headers['X-Request-Id'])
