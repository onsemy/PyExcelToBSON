#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
PyExcelToBSON - Excel 파일을 BSON 파일로 변환하는 CLI 도구
"""

import argparse

from factories.reader_factory import ReaderFactory
from factories.writer_factory import WriterFactory
from output_manager import OutputManager
    

def build_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Excel 파일을 BSON으로 변환합니다.')
    parser.add_argument('-i', '--input',  help='입력 파일 경로 (.xlsx/.xls)', required=True)
    parser.add_argument('-o', '--output', help='출력 디렉토리 경로',           required=True)
    parser.add_argument('-s', '--suffix', help='출력 파일 접미사',              required=False, default='')
    parser.add_argument('-d', '--debug',  help='JSON 파일도 함께 출력',        action='store_true')
    parser.add_argument('-c', '--clean',  help='출력 디렉토리 초기화',          action='store_true')
    return parser.parse_args()


def main() -> None:
    args = build_parser()

    output_manager = OutputManager(args.output, args.suffix)
    output_manager.prepare_directory(clean=args.clean)

    reader = ReaderFactory.create(args)
    writers = WriterFactory.create(args)

    for sheet_name, data in reader.read_sheets():
        print(f"[INFO] 변환 시작: {sheet_name}")
        for writer in writers:
            path = output_manager.build_path(sheet_name, writer.extension)
            writer.write(path, data)
        print(f"[INFO] 변환 종료: {sheet_name}")


if __name__ == '__main__':
    main()
