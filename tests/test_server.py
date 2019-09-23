# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
import re
from ddd_nginx.server import Server
from ddd_nginx.location import Location, LocationProxy, LocationRewrite


def test_create_upstream():
    sev = Server(name="server name")

    assert sev is not None
    assert sev.id is not None
    assert sev.name == "server name"


@pytest.mark.usefixtures("server_conf")
def test_dump_server(server_conf):
    sev = Server(
        name="api.example.com",
    )
    sev.set_var("$api_name", "-")

    assert sev.dump("server.conf.jinja2", {
        "name": sev.name,
        "variables": sev.sets,
        "tls": sev.tls,
    }) == server_conf


@pytest.mark.usefixtures("server_no_tls_conf")
def test_dump_server(server_no_tls_conf):
    sev = Server(
        name="api.example.com",
    )
    sev.set_var("$api_name", "-")

    assert sev.dump("server.conf.jinja2", {
        "name": sev.name,
        "variables": sev.sets,
    }) == server_no_tls_conf


@pytest.mark.usefixtures("server_location_conf")
def test_dump_server_dumps(server_location_conf):
    sev = Server(
        name="api.example.com",
    )
    sev.set_var("$api_name", "-")

    source_location = Location(
        name="/api/warehouse/pricing",
        internal=False
    )
    source_location.set_var("$upstream", "warehouse_pricing")

    destination_location = Location(
        name="/_warehouse",
        internal=True
    )
    destination_location.set_var('$api_name', '"Warehouse"')
    destination_location.append(LocationProxy('abc.com'))

    source_location.append(LocationRewrite(destination_location))

    sev.append(source_location)
    sev.append(destination_location)

    locations_dump = [Location.add_tab(a_location.smart_dump()) for a_location in sev.locations]

    print('??????')
    print(locations_dump)

    assert sev.dump("server-location.conf.jinja2", {
        "name": sev.name,
        "variables": sev.sets,
        "locations": locations_dump,
        "tls": sev.tls,
    }) == server_location_conf
