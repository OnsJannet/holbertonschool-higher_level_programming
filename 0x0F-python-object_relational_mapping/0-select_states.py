#!/usr/bin/python3
""" Python x MySQL : Listing data from a data base using args """
import MySQLdb
db=MySQLdb.connect(user="mysql username",passwd="mysql password",db="database name")
c=db.cursor()
c.execute("SELECT * FROM states")
for state in c.fetchall():
    print(state)
db.close()
