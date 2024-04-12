#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
"""where the state name matches the city state id"""


def main():
    HOST = "localhost"
    PORT = 3306
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB)
    cur = db.cursor()
    target = sys.argv[4]
    sql = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        """
    cur.execute(sql, (target,))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        for col in row:
            print(col, end=', ' if i < len(rows) - 1 else '')
    print()

    cur.close()
    db.close()


if __name__ == "__main__":
    import MySQLdb
    import sys

    main()
