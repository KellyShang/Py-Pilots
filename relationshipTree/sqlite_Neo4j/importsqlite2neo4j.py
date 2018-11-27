# -*- coding: utf-8 -*-

# Create By: Kelly Shang
# Create Date: Apr. 2017
# Purpose: import data from sqlite to Neo4j database

import operator
import os
import sys
import sqlite3

from py2neo import Graph


class ImportSQLite2Neo4j(object):
    dbaddr = os.path.dirname(os.path.dirname(__file__)) + '\csv_sqlite'

    def trans_dict(rows, col_name_list):
        dict_all = []
        for i in rows:
            m = 0
            dict_one = {}  ## note location
            for k in i:
                dict_one[col_name_list[m]] = i[m]
                m = m + 1
            print('dict_one: ', dict_one)
            dict_all.append(dict_one)

        print('dict_all: ', dict_all)
        sorted_dict = sorted(dict_all, key=operator.itemgetter('staff_id'))
        return sorted_dict

    # link to Sqlite
    conn = sqlite3.connect(dbaddr + '\\callTree.db')
    cur = conn.cursor()

    #   ----------------for user 表--------------
    cur.execute('select * from staff')
    # 返回一个list，list中的对象类型为tuple（元组）
    rows_user = cur.fetchall()
    cur.close()
    print('rows staff: ',rows_user)  # staff信息数组
    user_col_name_list = [tuple[0] for tuple in cur.description]  # ['staff_id', 'staff_name', 'phone', 'report_to']
    print('user_col_name_list: ', user_col_name_list)

    sorted_user_dict = trans_dict(rows_user, user_col_name_list)
    print('sorted_user_dict after def: ', sorted_user_dict)


    # link to Neo4j
    link = "http://neo4j:neo4j@localhost:7474/db/data/"
    gdb = Graph(link)
    rec = gdb.run("MATCH(staff:Staff) return staff limit 1")
    print('length1: ', len(rec.data()))

    for line in sorted_user_dict:
        query = "Merge (staff:Staff {staff_id: %s, staff_name: '%s', phone: '%s', report_to:'%s'})" % (
        line['staff_id'], line['staff_name'], line['phone'], line['report_to'])
        print('query: ', query)
        insert = gdb.run(query)


    query2 = """ MATCH (s1:Staff),(s2:Staff)
                       where s1.staff_name = s2.report_to
                       MERGE (s2) -[:Report_To]-> (s1)"""
    insert2 = gdb.run(query2)

    rec = gdb.run("MATCH(staff:Staff) return staff ")
    print('length2: ', len(rec.data()))

if __name__ == '__main__':
    ImportSQLite2Neo4j()
