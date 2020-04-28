#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pip install MySQL-python
import pymysql

HOST = 'localhost'
USER = 'root'
PASS = ''
DATABASE = 'test'

CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS users(
                    id INT(6) AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    password VARCHAR(50) NOT NULL 
                )"""

DROP_USER_TABLE = "DROP TABLE IF EXISTS `users`"
SHOW_TABLES = "SHOW TABLES"

INSERT_USER = "INSERT INTO users (username,password) VALUES( '{username}', '{password}')"
SELECT_USER = "SELECT username,password FROM users WHERE id={id}"
UPDATE_USER = "UPDATE users SET username={username},password={password} WHERE id={id}"
DELETE_USER = "DELETE FROM users WHERE id={id}"

def runQuery(query):
    try:
        cursor.execute(query)
        connection.commit()
    except:
        connection.rollback()

if __name__ == '__main__':
  try:
    connection = pymysql.connect(HOST,USER,PASS,DATABASE)
    cursor = connection.cursor()

    cursor.execute(DROP_USER_TABLE)
    cursor.execute(CREATE_USER_TABLE)
    
    username = input("Ingrese el username ")
    password = input("Ingrese el password ")

    query = INSERT_USER.format(username=username,password=password)
    runQuery(query)
    
    query = UPDATE_USER.format(username='ruben',password='blades',id=1)
    runQuery(query)

    query = SELECT_USER.format(id=1)
    print(query)
    cursor.execute(query)
    users = cursor.fetchall()
    user = users[0]
    print("username : " + user[1])
    print("password : " + user[2])
    
    query = DELETE_USER.format(id=1)
    runQuery(query)

    """cursor.execute(SHOW_TABLES)
    tables = cursor.fetchall()

    for table in tables:
        print(table)
    """
    connection.close()
  except pymysql.Error as error:
    print(error)