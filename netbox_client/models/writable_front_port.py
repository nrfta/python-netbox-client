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


class WritableFrontPort(object):
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
        'name': 'str',
        'type': 'str',
        'rear_port': 'int',
        'rear_port_position': 'int',
        'description': 'str',
        'cable': 'NestedCable',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'name': 'name',
        'type': 'type',
        'rear_port': 'rear_port',
        'rear_port_position': 'rear_port_position',
        'description': 'description',
        'cable': 'cable',
        'tags': 'tags'
    }

    def __init__(self, id=None, device=None, name=None, type=None, rear_port=None, rear_port_position=None, description=None, cable=None, tags=None):  # noqa: E501
        """WritableFrontPort - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device = None
        self._name = None
        self._type = None
        self._rear_port = None
        self._rear_port_position = None
        self._description = None
        self._cable = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.device = device
        self.name = name
        self.type = type
        self.rear_port = rear_port
        if rear_port_position is not None:
            self.rear_port_position = rear_port_position
        if description is not None:
            self.description = description
        if cable is not None:
            self.cable = cable
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this WritableFrontPort.  # noqa: E501


        :return: The id of this WritableFrontPort.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableFrontPort.


        :param id: The id of this WritableFrontPort.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """Gets the device of this WritableFrontPort.  # noqa: E501


        :return: The device of this WritableFrontPort.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this WritableFrontPort.


        :param device: The device of this WritableFrontPort.  # noqa: E501
        :type: int
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def name(self):
        """Gets the name of this WritableFrontPort.  # noqa: E501


        :return: The name of this WritableFrontPort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WritableFrontPort.


        :param name: The name of this WritableFrontPort.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this WritableFrontPort.  # noqa: E501


        :return: The type of this WritableFrontPort.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WritableFrontPort.


        :param type: The type of this WritableFrontPort.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["8p8c", "110-punch", "bnc", "mrj21", "fc", "lc", "lc-apc", "lsh", "lsh-apc", "mpo", "mtrj", "sc", "sc-apc", "st"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def rear_port(self):
        """Gets the rear_port of this WritableFrontPort.  # noqa: E501


        :return: The rear_port of this WritableFrontPort.  # noqa: E501
        :rtype: int
        """
        return self._rear_port

    @rear_port.setter
    def rear_port(self, rear_port):
        """Sets the rear_port of this WritableFrontPort.


        :param rear_port: The rear_port of this WritableFrontPort.  # noqa: E501
        :type: int
        """
        if rear_port is None:
            raise ValueError("Invalid value for `rear_port`, must not be `None`")  # noqa: E501

        self._rear_port = rear_port

    @property
    def rear_port_position(self):
        """Gets the rear_port_position of this WritableFrontPort.  # noqa: E501


        :return: The rear_port_position of this WritableFrontPort.  # noqa: E501
        :rtype: int
        """
        return self._rear_port_position

    @rear_port_position.setter
    def rear_port_position(self, rear_port_position):
        """Sets the rear_port_position of this WritableFrontPort.


        :param rear_port_position: The rear_port_position of this WritableFrontPort.  # noqa: E501
        :type: int
        """
        if rear_port_position is not None and rear_port_position > 64:  # noqa: E501
            raise ValueError("Invalid value for `rear_port_position`, must be a value less than or equal to `64`")  # noqa: E501
        if rear_port_position is not None and rear_port_position < 1:  # noqa: E501
            raise ValueError("Invalid value for `rear_port_position`, must be a value greater than or equal to `1`")  # noqa: E501

        self._rear_port_position = rear_port_position

    @property
    def description(self):
        """Gets the description of this WritableFrontPort.  # noqa: E501


        :return: The description of this WritableFrontPort.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WritableFrontPort.


        :param description: The description of this WritableFrontPort.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def cable(self):
        """Gets the cable of this WritableFrontPort.  # noqa: E501


        :return: The cable of this WritableFrontPort.  # noqa: E501
        :rtype: NestedCable
        """
        return self._cable

    @cable.setter
    def cable(self, cable):
        """Sets the cable of this WritableFrontPort.


        :param cable: The cable of this WritableFrontPort.  # noqa: E501
        :type: NestedCable
        """

        self._cable = cable

    @property
    def tags(self):
        """Gets the tags of this WritableFrontPort.  # noqa: E501


        :return: The tags of this WritableFrontPort.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WritableFrontPort.


        :param tags: The tags of this WritableFrontPort.  # noqa: E501
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
        if issubclass(WritableFrontPort, dict):
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
        if not isinstance(other, WritableFrontPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
