'''
CS 3700 - Networking & Distributed Computing - Fall 2024
Instructor: Thyago Mota
Student:
Description: Project 02 - Incidents WS (db initialization)
Observation: RUN IT FROM THE MAIN PROJECT'S FOLDER
'''

import sqlite3
import csv
import os

try: 
    os.makedirs('instance')
except: 
    pass

conn = sqlite3.connect('instance/incidents.db')

with open('src/incidents.sql') as f:
    conn.executescript(f.read())

conn.commit()

# load incidents data
cur = conn.cursor()
count = 0
# TODO #1: populate the incidents table (defined in src/incidents.sql) from data/incidents.csv
pass

sql = 'SELECT COUNT(*) FROM incidents'
cur.execute(sql)
row = cur.fetchone()
print(row[0], 'incidents inserted!')

conn.close()