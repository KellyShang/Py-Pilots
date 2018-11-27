# -*- coding: utf-8 -*-

# Create By: Kelly Shang
# Create Date: Apr. 2017
# Purpose: import data in the list which loaded from csv to sqlite database

from callTree.csv_sqlite.importcsv import *
from callTree.csv_sqlite.importcsv2sqlite import *
from callTree.csv_sqlite.creattable import *

def import2sqlite(adr, insert_table, table_list):
    records = loadCSVfile(adr)

    if str(insert_table) in table_list:
        for i in range(len(records)):
            one_data = (records[i])
            insert_data(insert_table, one_data)
        print('Import data to '+insert_table+' table finished!')
    else:
        print('Import data to table '+ insert_table + ' failed!')
