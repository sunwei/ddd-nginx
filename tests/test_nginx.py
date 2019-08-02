# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_nginx.nginx import Nginx
from ddd_nginx.map import Map
from ddd_nginx.map import MapDefinition
from ddd_nginx.server import Server
from ddd_nginx.upstream import Upstream
from ddd_nginx.exception import NginxError


def test_create_nginx():
    nginx = Nginx(host="oneapi.cc")
    nginx.namespace = "api"

    assert nginx is not None
    assert nginx.host is not None
    assert nginx.namespace == "api." + nginx.host


def test_append():
    nginx = Nginx(host="oneapi.cc")
    a_server = Server(name="api.example.com")
    a_map = Map(MapDefinition(key="$key", value="$value"))
    a_upstream = Upstream(name="upstream name")

    nginx.append(a_server)
    nginx.append(a_map)
    nginx.append(a_upstream)

    assert a_server.name == nginx.servers[0].name
    assert a_upstream.name == nginx.upstreams[0].name
    assert a_map.same_as(nginx.maps[0])

    with pytest.raises(NginxError):
        assert nginx.append(None)


@pytest.mark.usefixtures("nginx_conf")
def test_dump_empty(nginx_conf):
    nginx = Nginx(host="oneapi.cc")
    nginx.namespace = "api"

    assert nginx.dump("nginx.conf.jinja2", {
        "namespace": nginx.namespace,
    }) == nginx_conf
