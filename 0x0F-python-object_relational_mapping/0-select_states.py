#!/usr/bin/python3
'''Script that lists all states from database hbtn_0e_0_usa'''


import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    dc = conn.cursor()
    dc.execute("SELECT * FROM states ORDER BY id ASC")
    fetchdata = dc.fetchall()
    for x in fetchdata:
        print(x)
    dc.close()
    conn.close()
