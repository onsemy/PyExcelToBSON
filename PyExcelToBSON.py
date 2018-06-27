#!/usr/bin/env python

import argparse

import bson
import json

from xlrd import open_workbook

def set_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path of excel file", required=True)
    args = parser.parse_args()
    if not args.input:
        print("PARSER ERROR] arguments is wrong!")
        exit(1)

    return args

args = set_parser()
wb = open_workbook(args.input)
for sheet in wb.sheets():
    print(sheet.name)

    if sheet.name[0] == '_':
        print("INFO] skipped sheet - " + sheet.name)
        continue

    with open(sheet.name + '.bson', 'wb') as bson_file:
        json_dict = {}
        data_list = []
        key_list = []

        for i in range(sheet.nrows):
            #print("{} 번째".format(i))
            if i < 4:
                continue

            row = sheet.row(i)

            if i == 4:
                for col in row:
                    key_list.append(col.value)
                continue

            key_index = 0
            data_dict = {}
            for col in row:
                data_dict[key_list[key_index]] = col.value
                key_index = key_index + 1

            data_list.append(data_dict)

        json_dict['data'] = data_list

        bson_file.write(bson.dumps(json_dict))

    # NOTE(jjo): for test
    #with open(sheet.name + '.bson', 'rb') as bson_f:
    #    data = bson_f.read()
    #    print(bson.loads(data))

