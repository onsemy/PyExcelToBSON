#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

from pyexcel2bson.readers.excel_reader import ExcelReader
from pyexcel2bson.readers.input_reader import InputReader


_READER_MAP: dict[str, type[InputReader]] = {
    '.xlsx': ExcelReader,
    '.xls': ExcelReader,
}

class ReaderFactory:
    @staticmethod
    def create(args: argparse.Namespace) -> InputReader:
        ext = os.path.splitext(args.input)[1].lower()
        reader_class = _READER_MAP.get(ext)
        if reader_class is None:
            raise ValueError(f"Not supported format: {ext}\nSupported format: {list(_READER_MAP.keys())}")
        return reader_class(args.input)
