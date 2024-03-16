
#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ =="'__main__":
    """Function that connects to MySQL server on localhost at port 3306"""

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
    cursor.close()
    db.close()
