# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.map import Map
from ddd_nginx.map import MapDefinition
from ddd_nginx.map import MapKeyParis


def test_create_map():
    a_map = Map(MapDefinition(key="$key", value="$value"))

    assert a_map.definition.key is "$key"
    assert a_map.definition.value is "$value"


def test_compare_map():
    a_map = Map(MapDefinition(key="$key", value="$value"))
    b_map = Map(MapDefinition(key="$key", value="$value"))

    assert a_map.same_as(b_map) is True


@pytest.mark.usefixtures("map_empty_conf")
def test_dump_empty(map_empty_conf):
    a_map = Map(MapDefinition(key="$key", value="$value"))

    assert a_map.dump("api_keys.conf.jinja2", {
        "key_name": a_map.definition.key,
        "value_name": a_map.definition.value,
        "key_pairs": a_map.key_pairs
    }) == map_empty_conf


@pytest.mark.usefixtures("map_conf")
def test_dump(map_conf):
    a_map = Map(MapDefinition(key="$key", value="$value"))
    a_map.append(MapKeyParis("k1", "v1"))
    a_map.append(MapKeyParis("k2", "v2"))
    a_map.append(MapKeyParis("k3", "v3"))

    assert a_map.dump("api_keys.conf.jinja2", {
        "key_name": a_map.definition.key,
        "value_name": a_map.definition.value,
        "key_pairs": a_map.key_pairs
    }) == map_conf
