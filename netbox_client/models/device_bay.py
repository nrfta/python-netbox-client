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


class DeviceBay(object):
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
        'device': 'NestedDevice',
        'name': 'str',
        'description': 'str',
        'installed_device': 'NestedDevice',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'name': 'name',
        'description': 'description',
        'installed_device': 'installed_device',
        'tags': 'tags'
    }

    def __init__(self, id=None, device=None, name=None, description=None, installed_device=None, tags=None):  # noqa: E501
        """DeviceBay - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device = None
        self._name = None
        self._description = None
        self._installed_device = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.device = device
        self.name = name
        if description is not None:
            self.description = description
        if installed_device is not None:
            self.installed_device = installed_device
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this DeviceBay.  # noqa: E501


        :return: The id of this DeviceBay.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceBay.


        :param id: The id of this DeviceBay.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """Gets the device of this DeviceBay.  # noqa: E501


        :return: The device of this DeviceBay.  # noqa: E501
        :rtype: NestedDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DeviceBay.


        :param device: The device of this DeviceBay.  # noqa: E501
        :type: NestedDevice
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def name(self):
        """Gets the name of this DeviceBay.  # noqa: E501


        :return: The name of this DeviceBay.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceBay.


        :param name: The name of this DeviceBay.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DeviceBay.  # noqa: E501


        :return: The description of this DeviceBay.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceBay.


        :param description: The description of this DeviceBay.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def installed_device(self):
        """Gets the installed_device of this DeviceBay.  # noqa: E501


        :return: The installed_device of this DeviceBay.  # noqa: E501
        :rtype: NestedDevice
        """
        return self._installed_device

    @installed_device.setter
    def installed_device(self, installed_device):
        """Sets the installed_device of this DeviceBay.


        :param installed_device: The installed_device of this DeviceBay.  # noqa: E501
        :type: NestedDevice
        """

        self._installed_device = installed_device

    @property
    def tags(self):
        """Gets the tags of this DeviceBay.  # noqa: E501


        :return: The tags of this DeviceBay.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DeviceBay.


        :param tags: The tags of this DeviceBay.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(DeviceBay, dict):
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
        if not isinstance(other, DeviceBay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
