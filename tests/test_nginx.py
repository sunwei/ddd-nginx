# -*- coding: utf-8 -*-
"""Test ApiGW"""
import os
import pytest
from ddd_nginx.nginx import Nginx
from ddd_nginx.map import Map, MapKeyParis, MapDefinition
from ddd_nginx.server import Server
from ddd_nginx.location import Location, ReverseProxyStrategy
from ddd_nginx.upstream import Upstream
from ddd_nginx.exception import NginxError
from ddd_nginx.file_manager import remove_dir


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


def test_dumps():
    nginx = Nginx(host="oneapi.cc")
    nginx.namespace = "api"

    a_map = Map(MapDefinition(key="$http_apikey", value="$api_client_name"))
    a_map.append(MapKeyParis("7B5zIqmRGXmrJTFmKa99vcit", "client_one"))
    a_map.append(MapKeyParis("QzVV6y1EmQFbbxOfRCwyJs35", "client_two"))
    a_map.append(MapKeyParis("mGcjH8Fv6U9y3BVF9H3Ypb9T", "client_six"))

    a_upstream = Upstream(name="warehouse_inventory")
    a_upstream.append("10.0.0.1:80")
    a_upstream.append("10.0.0.2:80")
    a_upstream.append("10.0.0.3:80")

    b_upstream = Upstream(name="warehouse_pricing")
    b_upstream.append("10.0.0.1:80")
    b_upstream.append("10.0.0.2:80")
    b_upstream.append("10.0.0.3:80")

    a_location = Location(
        name="/api/warehouse/inventory",
        proxy=ReverseProxyStrategy('rewrite', '^ /_warehouse last')
    )
    a_location.set_var("$upstream", "warehouse_inventory")
    b_location = Location(
        name="/api/warehouse/pricing",
        proxy=ReverseProxyStrategy('rewrite', '^ /_warehouse last')
    )
    b_location.set_var("$upstream", "warehouse_pricing")
    c_location = Location(
        name="= /_warehouse",
        proxy=ReverseProxyStrategy('proxy_pass', 'http://$upstream$request_uri'),
        scope="internal"
    )
    c_location.set_var("$api_name", "Warehouse")

    a_server = Server(name=nginx.namespace)
    a_server.set_var("$api_name", "-")

    nginx.append(a_map)
    nginx.append(a_upstream)
    nginx.append(b_upstream)
    nginx.append(a_location)
    nginx.append(b_location)
    nginx.append(c_location)
    nginx.append(a_server)

    root_dir = "./dumps_dir"
    nginx.dumps(root_dir)

    assert os.path.isdir(root_dir) is True
    assert os.path.isdir(os.path.join(root_dir, "locations_conf.d")) is True
    assert os.path.isfile(os.path.join(root_dir, "root.conf"))
    assert os.path.isfile(os.path.join(root_dir, "0_map.conf"))
    assert os.path.isfile(os.path.join(root_dir, "0_server.conf"))
    assert os.path.isfile(os.path.join(root_dir, "warehouse_inventory_upstream.conf"))
    assert os.path.isfile(os.path.join(root_dir, "warehouse_pricing_upstream.conf"))
    assert os.path.isfile(os.path.join(root_dir, "locations_conf.d/0_location.conf"))
    assert os.path.isfile(os.path.join(root_dir, "locations_conf.d/1_location.conf"))
    assert os.path.isfile(os.path.join(root_dir, "locations_conf.d/2_location.conf"))

    remove_dir(root_dir)
