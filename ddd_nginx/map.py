# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ddd_base import ValueObject
from .block import Block


class Map(ValueObject, Block):

    def __init__(self, key_name, value_name):
        super().__init__()
        self.key_name = key_name
        self.value_name = value_name
        self.key_pairs = []

    def __eq__(self, other):
        if not isinstance(other, Map):
            return NotImplemented

        return self.key_name == other.key_name \
            and self.value_name == other.value_name \
            and self.key_pairs == other.key_pairs

    def append(self, block):
        self.key_pairs.append(block)
