#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


class OutputManager:
    def __init__(self, output_dir: str, suffix: str = ''):
        self.output_dir = output_dir
        self.suffix = suffix

    def prepare_directory(self, clean: bool = False) -> None:
        if os.path.exists(self.output_dir):
            if clean:
                shutil.rmtree(self.output_dir, ignore_errors=True)
                os.mkdir(self.output_dir)
        else:
            os.mkdir(self.output_dir)

    def build_path(self, sheet_name: str, extension: str) -> str:
        filename = f"{sheet_name}{self.suffix}.{extension}"
        return os.path.join(self.output_dir, filename)
