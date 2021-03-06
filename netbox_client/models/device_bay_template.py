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


class DeviceBayTemplate(object):
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
        'device_type': 'NestedDeviceType',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'device_type': 'device_type',
        'name': 'name'
    }

    def __init__(self, id=None, device_type=None, name=None):  # noqa: E501
        """DeviceBayTemplate - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device_type = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.device_type = device_type
        self.name = name

    @property
    def id(self):
        """Gets the id of this DeviceBayTemplate.  # noqa: E501


        :return: The id of this DeviceBayTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceBayTemplate.


        :param id: The id of this DeviceBayTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device_type(self):
        """Gets the device_type of this DeviceBayTemplate.  # noqa: E501


        :return: The device_type of this DeviceBayTemplate.  # noqa: E501
        :rtype: NestedDeviceType
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this DeviceBayTemplate.


        :param device_type: The device_type of this DeviceBayTemplate.  # noqa: E501
        :type: NestedDeviceType
        """
        if device_type is None:
            raise ValueError("Invalid value for `device_type`, must not be `None`")  # noqa: E501

        self._device_type = device_type

    @property
    def name(self):
        """Gets the name of this DeviceBayTemplate.  # noqa: E501


        :return: The name of this DeviceBayTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceBayTemplate.


        :param name: The name of this DeviceBayTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

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
        if issubclass(DeviceBayTemplate, dict):
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
        if not isinstance(other, DeviceBayTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
