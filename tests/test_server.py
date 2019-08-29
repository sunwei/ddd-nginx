# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.server import Server
from ddd_nginx.location import Location, ReverseProxyStrategy


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
    }) == server_conf


@pytest.mark.usefixtures("server_location_conf")
def test_dump_server_dumps(server_location_conf):
    sev = Server(
        name="api.example.com",
    )
    sev.set_var("$api_name", "-")

    b_location = Location(
        name="/api/warehouse/pricing",
        proxy=ReverseProxyStrategy('rewrite', '^ /_warehouse last')
    )
    b_location.set_var("$upstream", "warehouse_pricing")
    sev.append(b_location)

    a_location = Location(
        name="= /_warehouse",
        proxy=ReverseProxyStrategy('proxy_pass', 'http://$upstream$request_uri'),
        scope="internal"
    )
    a_location.set_var('$api_name', '"Warehouse"')
    sev.append(a_location)

    assert sev.dump("server-location.conf.jinja2", {
        "name": sev.name,
        "variables": sev.sets,
        "locations": sev.locations,
    }) == server_location_conf
