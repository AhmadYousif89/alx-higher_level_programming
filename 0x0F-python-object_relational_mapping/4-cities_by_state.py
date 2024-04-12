#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""


def main():
    HOST = "localhost"
    PORT = 3306
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB)
    cur = db.cursor()
    sql = """
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON states.id = cities.state_id
        """
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
