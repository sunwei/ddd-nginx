# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ddd_base import ValueObject


class Location(ValueObject):

    def __init__(self, name, upstream):
        super().__init__()
        self.name = name
        self.upstream = upstream
