# coding: utf-8

"""
    NetBox API

    API to access NetBox  # noqa: E501

    OpenAPI spec version: 2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WritablePlatform(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'slug': 'str',
        'manufacturer': 'int',
        'napalm_driver': 'str',
        'napalm_args': 'str',
        'description': 'str',
        'device_count': 'int',
        'virtualmachine_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'manufacturer': 'manufacturer',
        'napalm_driver': 'napalm_driver',
        'napalm_args': 'napalm_args',
        'description': 'description',
        'device_count': 'device_count',
        'virtualmachine_count': 'virtualmachine_count'
    }

    def __init__(self, id=None, name=None, slug=None, manufacturer=None, napalm_driver=None, napalm_args=None, description=None, device_count=None, virtualmachine_count=None):  # noqa: E501
        """WritablePlatform - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._slug = None
        self._manufacturer = None
        self._napalm_driver = None
        self._napalm_args = None
        self._description = None
        self._device_count = None
        self._virtualmachine_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.slug = slug
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if napalm_driver is not None:
            self.napalm_driver = napalm_driver
        if napalm_args is not None:
            self.napalm_args = napalm_args
        if description is not None:
            self.description = description
        if device_count is not None:
            self.device_count = device_count
        if virtualmachine_count is not None:
            self.virtualmachine_count = virtualmachine_count

    @property
    def id(self):
        """Gets the id of this WritablePlatform.  # noqa: E501


        :return: The id of this WritablePlatform.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritablePlatform.


        :param id: The id of this WritablePlatform.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WritablePlatform.  # noqa: E501


        :return: The name of this WritablePlatform.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WritablePlatform.


        :param name: The name of this WritablePlatform.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this WritablePlatform.  # noqa: E501


        :return: The slug of this WritablePlatform.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this WritablePlatform.


        :param slug: The slug of this WritablePlatform.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501
        if slug is not None and len(slug) > 100:
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `100`")  # noqa: E501
        if slug is not None and len(slug) < 1:
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501
        if slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def manufacturer(self):
        """Gets the manufacturer of this WritablePlatform.  # noqa: E501

        Optionally limit this platform to devices of a certain manufacturer  # noqa: E501

        :return: The manufacturer of this WritablePlatform.  # noqa: E501
        :rtype: int
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this WritablePlatform.

        Optionally limit this platform to devices of a certain manufacturer  # noqa: E501

        :param manufacturer: The manufacturer of this WritablePlatform.  # noqa: E501
        :type: int
        """

        self._manufacturer = manufacturer

    @property
    def napalm_driver(self):
        """Gets the napalm_driver of this WritablePlatform.  # noqa: E501

        The name of the NAPALM driver to use when interacting with devices  # noqa: E501

        :return: The napalm_driver of this WritablePlatform.  # noqa: E501
        :rtype: str
        """
        return self._napalm_driver

    @napalm_driver.setter
    def napalm_driver(self, napalm_driver):
        """Sets the napalm_driver of this WritablePlatform.

        The name of the NAPALM driver to use when interacting with devices  # noqa: E501

        :param napalm_driver: The napalm_driver of this WritablePlatform.  # noqa: E501
        :type: str
        """
        if napalm_driver is not None and len(napalm_driver) > 50:
            raise ValueError("Invalid value for `napalm_driver`, length must be less than or equal to `50`")  # noqa: E501

        self._napalm_driver = napalm_driver

    @property
    def napalm_args(self):
        """Gets the napalm_args of this WritablePlatform.  # noqa: E501

        Additional arguments to pass when initiating the NAPALM driver (JSON format)  # noqa: E501

        :return: The napalm_args of this WritablePlatform.  # noqa: E501
        :rtype: str
        """
        return self._napalm_args

    @napalm_args.setter
    def napalm_args(self, napalm_args):
        """Sets the napalm_args of this WritablePlatform.

        Additional arguments to pass when initiating the NAPALM driver (JSON format)  # noqa: E501

        :param napalm_args: The napalm_args of this WritablePlatform.  # noqa: E501
        :type: str
        """

        self._napalm_args = napalm_args

    @property
    def description(self):
        """Gets the description of this WritablePlatform.  # noqa: E501


        :return: The description of this WritablePlatform.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WritablePlatform.


        :param description: The description of this WritablePlatform.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def device_count(self):
        """Gets the device_count of this WritablePlatform.  # noqa: E501


        :return: The device_count of this WritablePlatform.  # noqa: E501
        :rtype: int
        """
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        """Sets the device_count of this WritablePlatform.


        :param device_count: The device_count of this WritablePlatform.  # noqa: E501
        :type: int
        """

        self._device_count = device_count

    @property
    def virtualmachine_count(self):
        """Gets the virtualmachine_count of this WritablePlatform.  # noqa: E501


        :return: The virtualmachine_count of this WritablePlatform.  # noqa: E501
        :rtype: int
        """
        return self._virtualmachine_count

    @virtualmachine_count.setter
    def virtualmachine_count(self, virtualmachine_count):
        """Sets the virtualmachine_count of this WritablePlatform.


        :param virtualmachine_count: The virtualmachine_count of this WritablePlatform.  # noqa: E501
        :type: int
        """

        self._virtualmachine_count = virtualmachine_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WritablePlatform, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WritablePlatform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
