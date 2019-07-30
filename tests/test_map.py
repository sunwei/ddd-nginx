# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.map import Map


def test_create_map():
    a_map = Map(key_name="$key", value_name="$value")

    assert a_map.key_name is "$key"
    assert a_map.value_name is "$value"


def test_compare_map():
    a_map = Map(key_name="$key", value_name="$value")
    b_map = Map(key_name="$key", value_name="$value")

    assert a_map.same_as(b_map) is True


@pytest.mark.usefixtures("map_empty_conf")
def test_dump_empty(map_empty_conf):
    a_map = Map(key_name="$key", value_name="$value")

    assert a_map.dump("api_keys.conf.jinja2", {
        "key_name": a_map.key_name,
        "value_name": a_map.value_name,
        "key_pairs": a_map.key_pairs
    }) == map_empty_conf


@pytest.mark.usefixtures("map_conf")
def test_dump(map_conf):
    a_map = Map(key_name="$key", value_name="$value")
    a_map.append({"key": "k1", "value": "v1"})
    a_map.append({"key": "k2", "value": "v2"})
    a_map.append({"key": "k3", "value": "v3"})

    assert a_map.dump("api_keys.conf.jinja2", {
        "key_name": a_map.key_name,
        "value_name": a_map.value_name,
        "key_pairs": a_map.key_pairs
    }) == map_conf
