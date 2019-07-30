# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ddd_base import Entity
from .block import Block


class Server(Block, Entity):

    def __init__(self, name):
        super().__init__()
        self.server_name = name
        self.locations = []

    def dump(self):
        pass

    def append(self):
        pass

