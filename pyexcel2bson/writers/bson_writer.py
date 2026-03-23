#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bson

from pyexcel2bson.writers.output_writer import OutputWriter


class BsonWriter(OutputWriter):
    @property
    def extension(self) -> str:
        return 'bson'

    def write(self, path: str, data: dict) -> None:
        with open(path, mode='wb') as f:
            f.write(bson.dumps(data))
