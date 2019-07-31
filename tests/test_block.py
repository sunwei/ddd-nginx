# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.block import Block


def test_set_var():
    a_block = Block()
    a_block.set_var("k1", "v1")

    assert len(a_block.sets) == 1
    assert a_block.sets[0].key == "k1"
    assert a_block.sets[0].value == "v1"


@pytest.mark.usefixtures("map_empty_conf")
def test_dump_empty(map_empty_conf):
    a_block = Block()
    assert a_block.dump("api_keys.conf.jinja2", {
        "key_name": "$key",
        "value_name": "$value",
        "key_pairs": []
    }) == map_empty_conf
