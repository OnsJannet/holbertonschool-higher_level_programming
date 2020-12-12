#!/usr/bin/python3
""" Python x MySQL : Listing data from a database using args """
import MySQLdb
import sys

db = MySQLdb.connect(user=argv[0],
                     passwd=argv[1],
                     db=argv[2])
c = db.cursor()
c.execute("SELECT * FROM states")
for state in c.fetchall():
    print(state)
c.close()
db.close()
