#!/usr/bin/python3
'''Script that lists all states from database hbtn_0e_0_usa'''


import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(host="localhost", port="3306", user="sys.argv[1]",
                            passwd="sys.argv[2]", db="sys.argv[3]")
    dbase_cursor = dbase.cursor()
    dbase_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    fetchdata = dbase_cursor.fetchall()
    for x in fetchdata:
        print(x)
    dbase_cursor.close()
    dbase.close()
