#!/usr/bin/python3
'''Takes in an argument and displays
all values in the states table where
name matches the argument.'''


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('''SELECT * FROM states WHERE BINARY name = "{}"
                ORDER BY id ASC'''.format(argv[4]))
    fetchdata = cur.fetchall()
    for x in fetchdata:
        print(x)
    cur.close()
    db.close()
