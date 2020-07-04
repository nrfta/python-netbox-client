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


class WritableSecret(object):
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
        'device': 'int',
        'role': 'int',
        'name': 'str',
        'plaintext': 'str',
        'hash': 'str',
        'tags': 'list[str]',
        'custom_fields': 'object',
        'created': 'date',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'role': 'role',
        'name': 'name',
        'plaintext': 'plaintext',
        'hash': 'hash',
        'tags': 'tags',
        'custom_fields': 'custom_fields',
        'created': 'created',
        'last_updated': 'last_updated'
    }

    def __init__(self, id=None, device=None, role=None, name=None, plaintext=None, hash=None, tags=None, custom_fields=None, created=None, last_updated=None):  # noqa: E501
        """WritableSecret - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device = None
        self._role = None
        self._name = None
        self._plaintext = None
        self._hash = None
        self._tags = None
        self._custom_fields = None
        self._created = None
        self._last_updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.device = device
        self.role = role
        if name is not None:
            self.name = name
        self.plaintext = plaintext
        if hash is not None:
            self.hash = hash
        if tags is not None:
            self.tags = tags
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def id(self):
        """Gets the id of this WritableSecret.  # noqa: E501


        :return: The id of this WritableSecret.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableSecret.


        :param id: The id of this WritableSecret.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """Gets the device of this WritableSecret.  # noqa: E501


        :return: The device of this WritableSecret.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this WritableSecret.


        :param device: The device of this WritableSecret.  # noqa: E501
        :type: int
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def role(self):
        """Gets the role of this WritableSecret.  # noqa: E501


        :return: The role of this WritableSecret.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this WritableSecret.


        :param role: The role of this WritableSecret.  # noqa: E501
        :type: int
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def name(self):
        """Gets the name of this WritableSecret.  # noqa: E501


        :return: The name of this WritableSecret.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WritableSecret.


        :param name: The name of this WritableSecret.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def plaintext(self):
        """Gets the plaintext of this WritableSecret.  # noqa: E501


        :return: The plaintext of this WritableSecret.  # noqa: E501
        :rtype: str
        """
        return self._plaintext

    @plaintext.setter
    def plaintext(self, plaintext):
        """Sets the plaintext of this WritableSecret.


        :param plaintext: The plaintext of this WritableSecret.  # noqa: E501
        :type: str
        """
        if plaintext is None:
            raise ValueError("Invalid value for `plaintext`, must not be `None`")  # noqa: E501
        if plaintext is not None and len(plaintext) < 1:
            raise ValueError("Invalid value for `plaintext`, length must be greater than or equal to `1`")  # noqa: E501

        self._plaintext = plaintext

    @property
    def hash(self):
        """Gets the hash of this WritableSecret.  # noqa: E501


        :return: The hash of this WritableSecret.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this WritableSecret.


        :param hash: The hash of this WritableSecret.  # noqa: E501
        :type: str
        """
        if hash is not None and len(hash) < 1:
            raise ValueError("Invalid value for `hash`, length must be greater than or equal to `1`")  # noqa: E501

        self._hash = hash

    @property
    def tags(self):
        """Gets the tags of this WritableSecret.  # noqa: E501


        :return: The tags of this WritableSecret.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WritableSecret.


        :param tags: The tags of this WritableSecret.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this WritableSecret.  # noqa: E501


        :return: The custom_fields of this WritableSecret.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this WritableSecret.


        :param custom_fields: The custom_fields of this WritableSecret.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def created(self):
        """Gets the created of this WritableSecret.  # noqa: E501


        :return: The created of this WritableSecret.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WritableSecret.


        :param created: The created of this WritableSecret.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this WritableSecret.  # noqa: E501


        :return: The last_updated of this WritableSecret.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this WritableSecret.


        :param last_updated: The last_updated of this WritableSecret.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if issubclass(WritableSecret, dict):
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
        if not isinstance(other, WritableSecret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other