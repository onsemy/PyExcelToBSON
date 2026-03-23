#!/usr/bin/env python
# -*- coding: utf-8 -*-

# NOTE(JJO): Const
from openpyxl import load_workbook

from pyexcel2bson.readers.input_reader import InputReader


SKIP_ROW_COUNT = 4
KEY_ROW_INDEX = 4
SKIP_SHEET_PREFIX = '_'
DATA_TYPE_ROW_INDEX = 3


class DataConverter:
    # NOTE(JJO): 자료형 기본값
    DEFAULT_VALUES = {
        'int': 0,
        'float': 0.0,
    }

    @staticmethod
    def resolve_cell_value(cell, data_type: str) -> object:
        if cell.value is not None:
            return cell.value
        return DataConverter.DEFAULT_VALUES.get(data_type, '')
    
    @staticmethod
    def parse_row(row, key_list: list, type_list: list) -> dict | None:
        data = {}
        for index, cell in enumerate(row):
            if index >= len(key_list):
                break
            if 0 == index and cell.value is None:
                return None
            data_type = type_list[index] if index < len(type_list) else ''
            data[key_list[index]] = DataConverter.resolve_cell_value(cell, data_type)
        return data if data else None
    

class ExcelReader(InputReader):
    def __init__(self, filepath: str):
        self.workbook = load_workbook(filename=filepath, data_only=True)

    def read_sheets(self):
        for sheet in self.workbook:
            if sheet.title.startswith(SKIP_SHEET_PREFIX):
                print(f"[INFO] Skip: {sheet.title}")
                continue

            yield sheet.title, self._parse_sheet(sheet)

    @staticmethod
    def _parse_sheet(sheet) -> dict:
        key_list = []
        data_list = []
        type_list = []

        for row_index, row in enumerate(sheet):
            if row_index < SKIP_ROW_COUNT:
                continue

            if row_index == KEY_ROW_INDEX:
                key_list = ExcelReader._extract_keys(row)
                continue

            if row_index == DATA_TYPE_ROW_INDEX:
                type_list = ExcelReader._extract_keys(row)
                continue

            parsed = DataConverter.parse_row(row, key_list, type_list)
            if parsed is not None:
                data_list.append(parsed)

        return {'data': data_list}
    
    @staticmethod
    def _extract_keys(row) -> list:
        keys = []
        for cell in row:
            if cell.value is None:
                break
            keys.append(str(cell.value))
        return keys
