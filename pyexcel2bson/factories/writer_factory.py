#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from pyexcel2bson.writers.bson_writer import BsonWriter
from pyexcel2bson.writers.json_writer import JsonWriter
from pyexcel2bson.writers.output_writer import OutputWriter


class WriterFactory:
    @staticmethod
    def create(args: argparse.Namespace) -> list[OutputWriter]:
        writers: list[OutputWriter] = [BsonWriter()]
        if args.debug:
            writers.append(JsonWriter())
        
        return writers
