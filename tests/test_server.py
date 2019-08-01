# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.server import Server


def test_create_upstream():
    sev = Server(name="server name")

    assert sev is not None
    assert sev.id is not None
    assert sev.name == "server name"


@pytest.mark.usefixtures("server_conf")
def test_dump_upstream(server_conf):
    sev = Server(
        name="api.example.com",
    )
    sev.set_var("$api_name", "-")

    assert sev.dump("server.conf.jinja2", {
        "name": sev.name,
        "variables": sev.sets,
    }) == server_conf
