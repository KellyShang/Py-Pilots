# -*- coding: utf-8 -*-

# Create By: Kelly Shang - 商轲
# Create Date: Apr. 2017
# Purpose: load data from csv to list

import csv

def loadCSVfile(file_adr):
    list_file = []

    with open(file_adr,'r') as csv_file:
        all_lines = csv.reader(csv_file)

        for line in all_lines:
            list_file.append(line)


    list_file.remove(list_file[0])
    print('Data from csv file: ' + str(list_file))
    return list_file
