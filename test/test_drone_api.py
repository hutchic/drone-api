# coding: utf-8

"""
    Drones Test Exercise API

    This is a sample API for renting time on a drones-as-a-service platform.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: info@superorbital.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.drone_api import DroneApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDroneApi(unittest.TestCase):
    """DroneApi unit test stubs"""

    def setUp(self):
        self.api = DroneApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_drone(self):
        """Test case for create_drone

        Creates a new drone resource  # noqa: E501
        """
        pass

    def test_delete_drone(self):
        """Test case for delete_drone

        Removes a drone from your collection.  # noqa: E501
        """
        pass

    def test_list_drones(self):
        """Test case for list_drones

        Lists all drones in your collection.  # noqa: E501
        """
        pass

    def test_read_drone(self):
        """Test case for read_drone

        Get status of a drone by id  # noqa: E501
        """
        pass

    def test_update_drone(self):
        """Test case for update_drone

        Change config for drone by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
