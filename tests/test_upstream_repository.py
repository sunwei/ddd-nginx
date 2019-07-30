# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_api_gateway.apigw_factory import create_api_gw
from ddd_api_gateway.upstream_repository import UpstreamRepository


@pytest.mark.usefixtures("api_gw_json_data")
def test_find_upstream_by_id(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)
    repository = UpstreamRepository(upstreams=api_gw_instance.upstreams)
    first_upstream = repository.upstreams[0]
    assert repository.find(first_upstream.id) is first_upstream


@pytest.mark.usefixtures("api_gw_json_data")
def test_find_upstream_by_name(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)
    repository = UpstreamRepository(upstreams=api_gw_instance.upstreams)
    first_upstream = repository.upstreams[0]
    assert repository.find_by_name(first_upstream.name) is first_upstream


@pytest.mark.usefixtures("api_gw_json_data")
def test_find_all_upstreams(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)
    repository = UpstreamRepository(upstreams=api_gw_instance.upstreams)
    assert repository.find_all() is repository.upstreams
