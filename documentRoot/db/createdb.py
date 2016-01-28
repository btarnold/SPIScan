#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE SCANS
       (ID INT PRIMARY KEY     NOT NULL,
       FILENAME        TEXT    NOT NULL,
       DPI             INT     NOT NULL,
       USERNOTES       TEXT,
       TIME            TEXT     NOT NULL,
       LOCATION        TEXT     NOT NULL);''')
print "Table created successfully";

conn.close()
