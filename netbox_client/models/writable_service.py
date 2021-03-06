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


class WritableService(object):
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
        'virtual_machine': 'int',
        'name': 'str',
        'port': 'int',
        'protocol': 'str',
        'ipaddresses': 'list[int]',
        'description': 'str',
        'tags': 'list[str]',
        'custom_fields': 'object',
        'created': 'date',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'virtual_machine': 'virtual_machine',
        'name': 'name',
        'port': 'port',
        'protocol': 'protocol',
        'ipaddresses': 'ipaddresses',
        'description': 'description',
        'tags': 'tags',
        'custom_fields': 'custom_fields',
        'created': 'created',
        'last_updated': 'last_updated'
    }

    def __init__(self, id=None, device=None, virtual_machine=None, name=None, port=None, protocol=None, ipaddresses=None, description=None, tags=None, custom_fields=None, created=None, last_updated=None):  # noqa: E501
        """WritableService - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device = None
        self._virtual_machine = None
        self._name = None
        self._port = None
        self._protocol = None
        self._ipaddresses = None
        self._description = None
        self._tags = None
        self._custom_fields = None
        self._created = None
        self._last_updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if device is not None:
            self.device = device
        if virtual_machine is not None:
            self.virtual_machine = virtual_machine
        self.name = name
        self.port = port
        self.protocol = protocol
        if ipaddresses is not None:
            self.ipaddresses = ipaddresses
        if description is not None:
            self.description = description
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
        """Gets the id of this WritableService.  # noqa: E501


        :return: The id of this WritableService.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableService.


        :param id: The id of this WritableService.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """Gets the device of this WritableService.  # noqa: E501


        :return: The device of this WritableService.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this WritableService.


        :param device: The device of this WritableService.  # noqa: E501
        :type: int
        """

        self._device = device

    @property
    def virtual_machine(self):
        """Gets the virtual_machine of this WritableService.  # noqa: E501


        :return: The virtual_machine of this WritableService.  # noqa: E501
        :rtype: int
        """
        return self._virtual_machine

    @virtual_machine.setter
    def virtual_machine(self, virtual_machine):
        """Sets the virtual_machine of this WritableService.


        :param virtual_machine: The virtual_machine of this WritableService.  # noqa: E501
        :type: int
        """

        self._virtual_machine = virtual_machine

    @property
    def name(self):
        """Gets the name of this WritableService.  # noqa: E501


        :return: The name of this WritableService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WritableService.


        :param name: The name of this WritableService.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 30:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def port(self):
        """Gets the port of this WritableService.  # noqa: E501


        :return: The port of this WritableService.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this WritableService.


        :param port: The port of this WritableService.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501
        if port is not None and port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if port is not None and port < 1:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this WritableService.  # noqa: E501


        :return: The protocol of this WritableService.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this WritableService.


        :param protocol: The protocol of this WritableService.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["tcp", "udp"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def ipaddresses(self):
        """Gets the ipaddresses of this WritableService.  # noqa: E501


        :return: The ipaddresses of this WritableService.  # noqa: E501
        :rtype: list[int]
        """
        return self._ipaddresses

    @ipaddresses.setter
    def ipaddresses(self, ipaddresses):
        """Sets the ipaddresses of this WritableService.


        :param ipaddresses: The ipaddresses of this WritableService.  # noqa: E501
        :type: list[int]
        """

        self._ipaddresses = ipaddresses

    @property
    def description(self):
        """Gets the description of this WritableService.  # noqa: E501


        :return: The description of this WritableService.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WritableService.


        :param description: The description of this WritableService.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this WritableService.  # noqa: E501


        :return: The tags of this WritableService.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WritableService.


        :param tags: The tags of this WritableService.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this WritableService.  # noqa: E501


        :return: The custom_fields of this WritableService.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this WritableService.


        :param custom_fields: The custom_fields of this WritableService.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def created(self):
        """Gets the created of this WritableService.  # noqa: E501


        :return: The created of this WritableService.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WritableService.


        :param created: The created of this WritableService.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this WritableService.  # noqa: E501


        :return: The last_updated of this WritableService.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this WritableService.


        :param last_updated: The last_updated of this WritableService.  # noqa: E501
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
        if issubclass(WritableService, dict):
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
        if not isinstance(other, WritableService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
