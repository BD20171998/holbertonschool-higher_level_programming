#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities, states WHERE state_id = \
    states.id AND states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cur.fetchall()

    mylist = []
    for i in rows:
        mylist.append(i[0])

    print(", ".join(mylist))

    cur.close()
    db.close()
