# -*- coding: utf-8 -*-

# Create By: Kelly Shang
# Create Date: Apr. 2017
# Purpose: main process for import csv to sqlite

import os

from callTree.csv_sqlite.importcsv2sqlite import *
from callTree.csv_sqlite.creattable import *

class CSV2SQLiteMain(object):
    adr = os.path.dirname(os.path.realpath(__file__))+'\csvfiles'

    create_table()

    table_list = ['staff']

    insert_staff = 'staff'
    adr_staff = adr+'\\staff.csv'
    import2sqlite(adr_staff,insert_staff,table_list)

    check_import(insert_staff,table_list)

if __name__ == '__main__':
    CSV2SQLiteMain()
# CSV2SQLiteMain()
