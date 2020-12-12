#!/usr/bin/python3
""" Python x MySQL : Listing data from a database using case sensitive """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute("SELECT * from states WHERE name LIKE '{}' COLLATE latin1_general_cs\
                ORDER BY states.id".format(argv[4]))
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
