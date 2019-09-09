# -*- coding: utf-8 -*-
"""Test data"""
import os
import pytest

TEST_PATH = os.path.abspath(os.path.dirname(__file__))
TEST_DATA_PATH = os.path.join(TEST_PATH, 'test_data')


def _get_test_data(filename):
    file_path = os.path.join(TEST_DATA_PATH, filename)
    with open(file_path, encoding='utf-8') as data_file:
        data = data_file.read()
    return data


@pytest.fixture(name='map_empty_conf')
def map_empty_conf():
    return _get_test_data('map-empty.conf')


@pytest.fixture(name='map_conf')
def map_conf():
    return _get_test_data('map.conf')


@pytest.fixture(name='location_api')
def location_api():
    return _get_test_data('location-api.conf')


@pytest.fixture(name='location_policy')
def location_policy():
    return _get_test_data('location-policy.conf')


@pytest.fixture(name='upstream_conf')
def upstream_conf():
    return _get_test_data('upstream.conf')


@pytest.fixture(name='server_conf')
def server_conf():
    return _get_test_data('server.conf')


@pytest.fixture(name='server_no_tls_conf')
def server_no_tls_conf():
    return _get_test_data('server-no-tls.conf')


@pytest.fixture(name='server_location_conf')
def server_location_conf():
    return _get_test_data('server-location.conf')


@pytest.fixture(name='server_location_no_tls_conf')
def server_location_no_tls_conf():
    return _get_test_data('server-location-no-tls.conf')


@pytest.fixture(name='nginx_conf')
def nginx_conf():
    return _get_test_data('nginx.conf')
