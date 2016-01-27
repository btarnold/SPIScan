#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('../db/test.db')
print "Opened database successfully";


# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
data= cgi.FieldStorage()

# Get data from fields
salary = argv[0]
id = argv[1]
print salary
print id
conn.execute("UPDATE COMPANY set SALARY = "+salary+" where ID="+id)
conn.commit
print "Total number of rows updated :", conn.total_changes

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()
