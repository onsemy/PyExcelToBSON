#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import bson
import json
import os
import shutil

from xlrd import open_workbook

def set_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path of excel file", required=True)
    parser.add_argument("-d", "--debug", help="export to json file", action="store_true")
    parser.add_argument("-c", "--clean", help="clean up output", action="store_true")
    args = parser.parse_args()
    if not args.input:
        print("PARSER ERROR] arguments is wrong!")
        exit(1)

    return args

args = set_parser()
wb = open_workbook(args.input)

if os.path.exists("output"):
    if args.clean:
        shutil.rmtree("output", ignore_errors=True)
        os.mkdir("output")
else:
    os.mkdir("output")

for sheet in wb.sheets():
    if sheet.name[0] == '_':
        print("INFO] skipped sheet - " + sheet.name)
        continue

    json_dict = {}
    print("INFO] start convert sheet - {}".format(sheet.name))
    with open("./output/{}.bson".format(sheet.name), 'wb') as bson_file:
        data_list = []
        key_list = []

        for i in range(sheet.nrows):
            # NOTE(jjo): 규칙에 의거하여 스킵 
            if i < 4:
                continue

            row = sheet.row(i)

            # NOTE(jjo): column name 수집 
            if i == 4:
                for col in row:
                    key_list.append(col.value)
                continue

            key_index = 0
            data_dict = {}
            for col in row:
                data_dict[key_list[key_index]] = str(col.value)
                key_index = key_index + 1

            data_list.append(data_dict)

        json_dict['data'] = data_list

        bson_file.write(bson.dumps(json_dict))

    if args.debug:
        with open("./output/{}.json".format(sheet.name), 'w') as json_file:
            json.dump(json_dict, json_file, indent=4, sort_keys=True)

    print("INFO] end convert process - {}".format(sheet.name))

    # NOTE(jjo): for test
    #with open(sheet.name + '.bson', 'rb') as bson_f:
    #    data = bson_f.read()
    #    print(bson.loads(data))

