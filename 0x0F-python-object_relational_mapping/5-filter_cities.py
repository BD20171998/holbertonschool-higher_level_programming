#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities, states WHERE state_id = \
    states.id AND states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))

    i = 1
    allrecs = cur.rowcount
    rows = cur.fetchall()

    for row in rows:
        if i == allrecs:
            print("{}".format(row[0]))
            break

        print("{}, ".format(row[0]), end="")
        i += 1

    cur.close()
    db.close()
