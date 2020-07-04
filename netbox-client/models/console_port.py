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


class ConsolePort(object):
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
        'type': 'Type',
        'description': 'str',
        'connected_endpoint_type': 'str',
        'connected_endpoint': 'dict(str, str)',
        'connection_status': 'ConnectionStatus',
        'cable': 'NestedCable',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'connected_endpoint_type': 'connected_endpoint_type',
        'connected_endpoint': 'connected_endpoint',
        'connection_status': 'connection_status',
        'cable': 'cable',
        'tags': 'tags'
    }

    def __init__(self, id=None, device=None, name=None, type=None, description=None, connected_endpoint_type=None, connected_endpoint=None, connection_status=None, cable=None, tags=None):  # noqa: E501
        """ConsolePort - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device = None
        self._name = None
        self._type = None
        self._description = None
        self._connected_endpoint_type = None
        self._connected_endpoint = None
        self._connection_status = None
        self._cable = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.device = device
        self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if connected_endpoint_type is not None:
            self.connected_endpoint_type = connected_endpoint_type
        if connected_endpoint is not None:
            self.connected_endpoint = connected_endpoint
        if connection_status is not None:
            self.connection_status = connection_status
        if cable is not None:
            self.cable = cable
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this ConsolePort.  # noqa: E501


        :return: The id of this ConsolePort.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConsolePort.


        :param id: The id of this ConsolePort.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """Gets the device of this ConsolePort.  # noqa: E501


        :return: The device of this ConsolePort.  # noqa: E501
        :rtype: NestedDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this ConsolePort.


        :param device: The device of this ConsolePort.  # noqa: E501
        :type: NestedDevice
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def name(self):
        """Gets the name of this ConsolePort.  # noqa: E501


        :return: The name of this ConsolePort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConsolePort.


        :param name: The name of this ConsolePort.  # noqa: E501
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
    def type(self):
        """Gets the type of this ConsolePort.  # noqa: E501


        :return: The type of this ConsolePort.  # noqa: E501
        :rtype: Type
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConsolePort.


        :param type: The type of this ConsolePort.  # noqa: E501
        :type: Type
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this ConsolePort.  # noqa: E501


        :return: The description of this ConsolePort.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConsolePort.


        :param description: The description of this ConsolePort.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def connected_endpoint_type(self):
        """Gets the connected_endpoint_type of this ConsolePort.  # noqa: E501


        :return: The connected_endpoint_type of this ConsolePort.  # noqa: E501
        :rtype: str
        """
        return self._connected_endpoint_type

    @connected_endpoint_type.setter
    def connected_endpoint_type(self, connected_endpoint_type):
        """Sets the connected_endpoint_type of this ConsolePort.


        :param connected_endpoint_type: The connected_endpoint_type of this ConsolePort.  # noqa: E501
        :type: str
        """

        self._connected_endpoint_type = connected_endpoint_type

    @property
    def connected_endpoint(self):
        """Gets the connected_endpoint of this ConsolePort.  # noqa: E501

         Return the appropriate serializer for the type of connected object.   # noqa: E501

        :return: The connected_endpoint of this ConsolePort.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._connected_endpoint

    @connected_endpoint.setter
    def connected_endpoint(self, connected_endpoint):
        """Sets the connected_endpoint of this ConsolePort.

         Return the appropriate serializer for the type of connected object.   # noqa: E501

        :param connected_endpoint: The connected_endpoint of this ConsolePort.  # noqa: E501
        :type: dict(str, str)
        """

        self._connected_endpoint = connected_endpoint

    @property
    def connection_status(self):
        """Gets the connection_status of this ConsolePort.  # noqa: E501


        :return: The connection_status of this ConsolePort.  # noqa: E501
        :rtype: ConnectionStatus
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this ConsolePort.


        :param connection_status: The connection_status of this ConsolePort.  # noqa: E501
        :type: ConnectionStatus
        """

        self._connection_status = connection_status

    @property
    def cable(self):
        """Gets the cable of this ConsolePort.  # noqa: E501


        :return: The cable of this ConsolePort.  # noqa: E501
        :rtype: NestedCable
        """
        return self._cable

    @cable.setter
    def cable(self, cable):
        """Sets the cable of this ConsolePort.


        :param cable: The cable of this ConsolePort.  # noqa: E501
        :type: NestedCable
        """

        self._cable = cable

    @property
    def tags(self):
        """Gets the tags of this ConsolePort.  # noqa: E501


        :return: The tags of this ConsolePort.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ConsolePort.


        :param tags: The tags of this ConsolePort.  # noqa: E501
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
        if issubclass(ConsolePort, dict):
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
        if not isinstance(other, ConsolePort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other