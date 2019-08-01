# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.upstream import Upstream


def test_create_upstream():
    up = Upstream(name="upstream name")
    up.append("server url")

    assert up is not None
    assert up.id is not None
    assert up.name == "upstream name"
    assert up.servers[0] == "server url"


@pytest.mark.usefixtures("upstream_conf")
def test_dump_upstream(upstream_conf):
    up = Upstream(
        name="warehouse_inventory",
    )
    up.append("10.0.0.1:80")
    up.append("10.0.0.2:80")
    up.append("10.0.0.3:80")

    assert up.dump("upstream.conf.jinja2", {
        "name": up.name,
        "servers": up.servers,
    }) == upstream_conf
