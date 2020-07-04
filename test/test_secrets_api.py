# coding: utf-8

"""
    NetBox API

    API to access NetBox  # noqa: E501

    OpenAPI spec version: 2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import netbox_client
from netbox_client.api.secrets_api import SecretsApi  # noqa: E501
from netbox_client.rest import ApiException


class TestSecretsApi(unittest.TestCase):
    """SecretsApi unit test stubs"""

    def setUp(self):
        self.api = netbox_client.api.secrets_api.SecretsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_secrets_generate_rsa_key_pair_list(self):
        """Test case for secrets_generate_rsa_key_pair_list

        This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.  # noqa: E501
        """
        pass

    def test_secrets_get_session_key_create(self):
        """Test case for secrets_get_session_key_create

        """
        pass

    def test_secrets_secret_roles_create(self):
        """Test case for secrets_secret_roles_create

        """
        pass

    def test_secrets_secret_roles_delete(self):
        """Test case for secrets_secret_roles_delete

        """
        pass

    def test_secrets_secret_roles_list(self):
        """Test case for secrets_secret_roles_list

        """
        pass

    def test_secrets_secret_roles_partial_update(self):
        """Test case for secrets_secret_roles_partial_update

        """
        pass

    def test_secrets_secret_roles_read(self):
        """Test case for secrets_secret_roles_read

        """
        pass

    def test_secrets_secret_roles_update(self):
        """Test case for secrets_secret_roles_update

        """
        pass

    def test_secrets_secrets_create(self):
        """Test case for secrets_secrets_create

        """
        pass

    def test_secrets_secrets_delete(self):
        """Test case for secrets_secrets_delete

        """
        pass

    def test_secrets_secrets_list(self):
        """Test case for secrets_secrets_list

        """
        pass

    def test_secrets_secrets_partial_update(self):
        """Test case for secrets_secrets_partial_update

        """
        pass

    def test_secrets_secrets_read(self):
        """Test case for secrets_secrets_read

        """
        pass

    def test_secrets_secrets_update(self):
        """Test case for secrets_secrets_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
