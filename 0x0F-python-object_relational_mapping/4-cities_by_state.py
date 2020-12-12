#!/usr/bin/python3
""" Python x MySQL : Listing data from join tables """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
