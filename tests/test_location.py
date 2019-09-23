# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.location import Location
from ddd_nginx.location import LocationProxy, LocationRewrite


def test_create_location():
    a_location = Location(
        name="location name",
        internal=True
    )
    b_location = Location(
        name="location name",
        internal=False
    )

    assert a_location is not None
    assert a_location.name == "location name"
    assert a_location.internal is True
    assert a_location.same_as(b_location) is False


@pytest.mark.usefixtures("location_api")
def test_dump_api(location_api):
    source_location = Location(
        name="/api/warehouse/pricing",
        internal=False
    )
    source_location.set_var("$upstream", "warehouse_pricing")

    destination_location = Location(
        name="/_warehouse",
        internal=True
    )
    source_location.append(LocationRewrite(destination_location))

    assert source_location.dump("location-rewrite.conf.jinja2", {
        "name": source_location.name,
        "variables": source_location.sets,
        "destination_name": source_location.rewrite.destination.name,
    }) == location_api

    assert source_location.dump_rewrite() == location_api
    assert source_location.smart_dump() == location_api


@pytest.mark.usefixtures("location_policy")
def test_dump_policy(location_policy):
    a_location = Location(
        name="= /_warehouse",
        internal=True
    )
    a_location.set_var('$api_name', '"Warehouse"')
    a_location.append(LocationProxy('abc.com'))

    assert a_location.dump("location-proxy.conf.jinja2", {
        "name": a_location.name,
        "variables": a_location.sets,
        "host": a_location.proxy.host,
    }) == location_policy

    assert a_location.dump_proxy() == location_policy
    assert a_location.smart_dump() == location_policy
