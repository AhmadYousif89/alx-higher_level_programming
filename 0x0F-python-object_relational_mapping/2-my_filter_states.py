#!/usr/bin/python3
"""Lists a specific state from the database hbtn_0e_0_usa"""


def main():
    HOST = "localhost"
    PORT = 3306
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB)
    cur = db.cursor()
    target = sys.argv[4]
    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(target)
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    import MySQLdb
    import sys

    main()
