#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class InputReader(ABC):
    @abstractmethod
    def read_sheets(self):
        pass
