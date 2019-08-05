# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.location import Location
from ddd_nginx.location import ReverseProxyStrategy


def test_create_location():
    a_location = Location(
        name="location name",
        proxy=ReverseProxyStrategy('rewrite', 'change uri'),
        scope="internal"
    )
    b_location = Location(
        name="location name",
        proxy=ReverseProxyStrategy('rewrite', 'change uri'),
        scope="internal"
    )

    assert a_location is not None
    assert a_location.name == "location name"
    assert a_location.scope == "internal"
    assert a_location.proxy.strategy == "rewrite"
    assert a_location.proxy.rule == "change uri"
    assert a_location.same_as(b_location)


@pytest.mark.usefixtures("location_api")
def test_dump_api(location_api):
    a_location = Location(
        name="/api/warehouse/pricing",
        proxy=ReverseProxyStrategy('rewrite', '^ /_warehouse last')
    )
    a_location.set_var("$upstream", "warehouse_pricing")

    assert a_location.dump("location.conf.jinja2", {
        "name": a_location.name,
        "proxy": a_location.proxy,
        "variables": a_location.sets
    }) == location_api


@pytest.mark.usefixtures("location_policy")
def test_dump_policy(location_policy):
    a_location = Location(
        name="= /_warehouse",
        proxy=ReverseProxyStrategy('proxy_pass', 'http://$upstream$request_uri'),
        scope="internal"
    )
    a_location.set_var('$api_name', '"Warehouse"')

    assert a_location.dump("location.conf.jinja2", {
        "name": a_location.name,
        "proxy": a_location.proxy,
        "variables": a_location.sets,
        "scope": a_location.scope
    }) == location_policy
