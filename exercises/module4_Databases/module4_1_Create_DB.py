# Python Flask Essential Training
# Module 3: Database
# Create database

import sqlite3

conn = sqlite3.connect('test2.db')
print("Opened database successfully");

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully");
conn.close()

# db= sqlite3.connect('test.db')
# #db.execute('CREATE TABLE student (name text, rank int)')

# db.execute('INSERT INTO student (name,rank) values (?,?)',('Ally',1))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Belinda',1))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Cherly',1))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Jane',1))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Steve',1))

# db.commit()