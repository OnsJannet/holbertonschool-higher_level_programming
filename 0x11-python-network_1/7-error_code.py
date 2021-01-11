#!/usr/bin/python3
""" a function that Sends a request and display a response """
import requests
from requests.exceptions import HTTPError
    r = requests.get(argv[1])
        if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
