# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ddd_base import ValueObject
from .block import Block


class Location(ValueObject, Block):

    def __init__(self, name, upstream):
        super().__init__()
        self.name = name
        self.upstream = upstream

    def __eq__(self, other):
        if not isinstance(other, Map):
            return NotImplemented

        return self.key_name == other.key_name \
            and self.value_name == other.value_name \
            and self.key_pairs == other.key_pairs

    def append(self, block):
        pass

