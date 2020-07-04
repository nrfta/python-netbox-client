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


class CircuitType(object):
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
        'description': 'str',
        'circuit_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'description': 'description',
        'circuit_count': 'circuit_count'
    }

    def __init__(self, id=None, name=None, slug=None, description=None, circuit_count=None):  # noqa: E501
        """CircuitType - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._slug = None
        self._description = None
        self._circuit_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.slug = slug
        if description is not None:
            self.description = description
        if circuit_count is not None:
            self.circuit_count = circuit_count

    @property
    def id(self):
        """Gets the id of this CircuitType.  # noqa: E501


        :return: The id of this CircuitType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CircuitType.


        :param id: The id of this CircuitType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CircuitType.  # noqa: E501


        :return: The name of this CircuitType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CircuitType.


        :param name: The name of this CircuitType.  # noqa: E501
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
    def slug(self):
        """Gets the slug of this CircuitType.  # noqa: E501


        :return: The slug of this CircuitType.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this CircuitType.


        :param slug: The slug of this CircuitType.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501
        if slug is not None and len(slug) > 50:
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `50`")  # noqa: E501
        if slug is not None and len(slug) < 1:
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501
        if slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def description(self):
        """Gets the description of this CircuitType.  # noqa: E501


        :return: The description of this CircuitType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CircuitType.


        :param description: The description of this CircuitType.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def circuit_count(self):
        """Gets the circuit_count of this CircuitType.  # noqa: E501


        :return: The circuit_count of this CircuitType.  # noqa: E501
        :rtype: int
        """
        return self._circuit_count

    @circuit_count.setter
    def circuit_count(self, circuit_count):
        """Sets the circuit_count of this CircuitType.


        :param circuit_count: The circuit_count of this CircuitType.  # noqa: E501
        :type: int
        """

        self._circuit_count = circuit_count

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
        if issubclass(CircuitType, dict):
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
        if not isinstance(other, CircuitType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
