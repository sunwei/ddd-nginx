# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
import uuid
from ddd_base import Entity
from .block import Block


class Upstream(Entity, Block):

    def __init__(self, name, endpoints):
        super(Upstream, self).__init__()
        self.name = name
        self.endpoints = endpoints

    def dump(self):
        upstream_copy = self.__class__(self.name, self.endpoints)
        upstream_copy.__dict__.update(**kwargs)
        upstream_copy.id = uuid.uuid1()
        return upstream_copy

    def append(self, block):
        pass
