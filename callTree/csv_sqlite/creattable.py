# -*- coding: utf-8 -*-

# Create By: Kelly Shang - 商轲
# Create Date: Apr. 2017
# Purpose: Create database and table

import os
import sqlite3

adrDB = os.path.dirname(os.path.realpath(__file__))+'\\calltree.db'
def create_table():
    conn = sqlite3.connect(adrDB)
    cur = conn.cursor()

    cur.execute('''DROP TABLE IF EXISTS staff''')

    cur.execute('''CREATE TABLE staff (
    staff_id   INTEGER PRIMARY KEY
                       UNIQUE
                       NOT NULL,
    staff_name VARCHAR NOT NULL,
    phone      VARCHAR,
    report_to  VARCHAR REFERENCES staff (staff_name)
                       DEFAULT None
    )''')

def insert_data(table,t):
    conn = sqlite3.connect(adrDB)
    cur = conn.cursor()

    if table == 'staff':
        cur.execute('''INSERT INTO {} VALUES (?,?,?,?)'''.format(table),t)
    else:
        print('Insert failed!')
    conn.commit()
    cur.close()
    conn.close()

def check_import(table, table_list):
    conn = sqlite3.connect(adrDB)
    cur = conn.cursor()
    count = 0

    if table in table_list:
        count = len((list(cur.execute('''select * from {}'''.format(table)))))
        #print(count)
    else:
        print('No such table: ' + table)

    if count > 0:
        print('There are '+ str(count) + ' records of data in '+table +' table!')
    else:
        print('No data been insert into '+table+' table!')


if __name__ == '__main__':
    create_table()