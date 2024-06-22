#!/usr/bin/python3
"""
making the databases more handy and useful in comming days
"""
from sys import argv
import MySQLdb

def main():
    """this function will be responisble for listing all the states in the database"""
    db_user = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    db_host = "localhost"
    db_port = 3306
    
    try:
        db = MySQLdb.connect(host = db_host,user=db_user, passwrd=db_password, db= db_name, port=db_port)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY name ASC;")
        querey_result = cur.fetchall()
        for row in querey_result:
            print(row)
        cur.close()
        db.close()

    except Exception:
        pass

if __name__ == "__main__":
    main()