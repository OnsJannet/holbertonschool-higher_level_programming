#!/usr/bin/python3
""" Python x MySQL : Listing specific data from a database using args """
import MySQLdb
import sys

db = MySQLdb.connect(user=argv[1],
                     passwd=argv[2],
                     db=argv[3])
c = db.cursor()
c.execute("SELECT * FROM states WHERE name LIKE 'N%'")
for state in c.fetchall():
    print(state)
c.close()
db.close()
