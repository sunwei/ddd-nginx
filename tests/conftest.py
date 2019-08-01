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
