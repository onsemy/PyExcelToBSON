#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from writers.output_writer import OutputWriter


class JsonWriter(OutputWriter):
    @property
    def extension(self) -> str:
        return 'json'

    def write(self, path: str, data: dict) -> None:
        with open(path, mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
