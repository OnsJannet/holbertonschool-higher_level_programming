#!/usr/bin/python3
""" a function that fetches a URL """

import urllib.request as request
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}
    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(res.read().decode('utf-8'))
