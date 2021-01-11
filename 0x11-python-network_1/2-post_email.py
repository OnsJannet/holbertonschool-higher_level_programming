#!/usr/bin/python3
""" a function that fetches a URL """

import urllib.request as request
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {'email' : argv[2]}
    data = parse.urlencode(data)
    data = data.encode('ascii')
    r = request.Request(url, data)
    with request.urlopen(r) as response:
        print(response.read().decode('utf-8'))
