#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import bson
import json
import os
import shutil

from openpyxl import load_workbook

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
wb = load_workbook(filename=args.input, data_only=True)

if os.path.exists("output"):
    if args.clean:
        shutil.rmtree("output", ignore_errors=True)
        os.mkdir("output")
else:
    os.mkdir("output")

for sheet in wb:
    if sheet.title[0] == '_':
        print("INFO] skipped sheet - " + sheet.title)
        continue

    json_dict = {}
    print("INFO] start convert sheet - {}".format(sheet.title))
    with open("./output/{}.bson".format(sheet.title), mode='wb') as bson_file:
        data_list = []
        key_list = []

        rowIndex = -1

        for row in sheet:
            colIndex = 0

            rowIndex = rowIndex + 1

            if rowIndex < 4:
                continue
            
            if rowIndex == 4:
                for col in row:
                    if col.value is None:
                        break
                    key_list.append(str(col.value))
                continue

            key_index = 0
            data_dict = {}

            for col in row:
                if col.value is None:
                    break
                data_dict[key_list[key_index]] = col.value
                key_index = key_index + 1

            data_list.append(data_dict)

        json_dict['data'] = data_list

        bson_file.write(bson.dumps(json_dict))

    if args.debug:
        with open("./output/{}.json".format(sheet.title), mode='w', encoding='utf-8') as json_file:
            json.dump(json_dict, json_file, indent=4, sort_keys=True, ensure_ascii=False)

    print("INFO] end convert process - {}".format(sheet.title))

    # NOTE(jjo): for test
    #with open(sheet.name + '.bson', 'rb') as bson_f:
    #    data = bson_f.read()
    #    print(bson.loads(data))

