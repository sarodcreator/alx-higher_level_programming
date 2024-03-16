#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

from sys import argv
import MySQLdb

if __name__ == "__main":
    if len(argv) != 5:
        sys.exit(1)
    db = MySQLdb.connect(host="localhost",
            port=3306, user=argv[1], passwd=argv[2],
            db=argv[3])
    cursor = db.cursor()
    state_name =sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name=%s
    ORDER BY id ASC", (state_name))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    cursor.close()
    db.close()
