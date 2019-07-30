# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
import os
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template/apigw")


class Block:

    def load(self):
        pass

    def dump(self, template_name, render_key_pairs):
        j2_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                             trim_blocks=True)
        return j2_env.get_template(template_name).render(render_key_pairs)

    def append(self, block):
        raise NotImplementedError

    def remove(self):
        pass
