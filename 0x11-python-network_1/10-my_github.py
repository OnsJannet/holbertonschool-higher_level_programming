#!/usr/bin/python3
''' a script that display id using Github credentials '''
import requests
from sys import argv

if __name__ == "__main__":

        r = requests.get('https://api.github.com/user', auth=(
            argv[1], argv[2])).json()
        print(r.get('id'))
