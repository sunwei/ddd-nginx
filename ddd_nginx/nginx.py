# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ddd_base import Aggregate
from .block import Block


class Nginx(Block, Aggregate):

    def __init__(self, namespace):
        super().__init__()
        self.namespace = namespace
        self.upstreams = []
        self.map = []
        self.server = None

    def dump(self):
        pass

    def append(self):
        pass
