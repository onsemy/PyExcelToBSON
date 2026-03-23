#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class OutputWriter(ABC):
    @abstractmethod
    def write(self, path: str, data: dict) -> None:
        pass

    @property
    @abstractmethod
    def extension(self) -> str:
        pass
