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


class WritableCable(object):
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
        'termination_a_type': 'str',
        'termination_a_id': 'int',
        'termination_a': 'dict(str, str)',
        'termination_b_type': 'str',
        'termination_b_id': 'int',
        'termination_b': 'dict(str, str)',
        'type': 'str',
        'status': 'str',
        'label': 'str',
        'color': 'str',
        'length': 'int',
        'length_unit': 'str'
    }

    attribute_map = {
        'id': 'id',
        'termination_a_type': 'termination_a_type',
        'termination_a_id': 'termination_a_id',
        'termination_a': 'termination_a',
        'termination_b_type': 'termination_b_type',
        'termination_b_id': 'termination_b_id',
        'termination_b': 'termination_b',
        'type': 'type',
        'status': 'status',
        'label': 'label',
        'color': 'color',
        'length': 'length',
        'length_unit': 'length_unit'
    }

    def __init__(self, id=None, termination_a_type=None, termination_a_id=None, termination_a=None, termination_b_type=None, termination_b_id=None, termination_b=None, type=None, status=None, label=None, color=None, length=None, length_unit=None):  # noqa: E501
        """WritableCable - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._termination_a_type = None
        self._termination_a_id = None
        self._termination_a = None
        self._termination_b_type = None
        self._termination_b_id = None
        self._termination_b = None
        self._type = None
        self._status = None
        self._label = None
        self._color = None
        self._length = None
        self._length_unit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.termination_a_type = termination_a_type
        self.termination_a_id = termination_a_id
        if termination_a is not None:
            self.termination_a = termination_a
        self.termination_b_type = termination_b_type
        self.termination_b_id = termination_b_id
        if termination_b is not None:
            self.termination_b = termination_b
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if label is not None:
            self.label = label
        if color is not None:
            self.color = color
        if length is not None:
            self.length = length
        if length_unit is not None:
            self.length_unit = length_unit

    @property
    def id(self):
        """Gets the id of this WritableCable.  # noqa: E501


        :return: The id of this WritableCable.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableCable.


        :param id: The id of this WritableCable.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def termination_a_type(self):
        """Gets the termination_a_type of this WritableCable.  # noqa: E501


        :return: The termination_a_type of this WritableCable.  # noqa: E501
        :rtype: str
        """
        return self._termination_a_type

    @termination_a_type.setter
    def termination_a_type(self, termination_a_type):
        """Sets the termination_a_type of this WritableCable.


        :param termination_a_type: The termination_a_type of this WritableCable.  # noqa: E501
        :type: str
        """
        if termination_a_type is None:
            raise ValueError("Invalid value for `termination_a_type`, must not be `None`")  # noqa: E501

        self._termination_a_type = termination_a_type

    @property
    def termination_a_id(self):
        """Gets the termination_a_id of this WritableCable.  # noqa: E501


        :return: The termination_a_id of this WritableCable.  # noqa: E501
        :rtype: int
        """
        return self._termination_a_id

    @termination_a_id.setter
    def termination_a_id(self, termination_a_id):
        """Sets the termination_a_id of this WritableCable.


        :param termination_a_id: The termination_a_id of this WritableCable.  # noqa: E501
        :type: int
        """
        if termination_a_id is None:
            raise ValueError("Invalid value for `termination_a_id`, must not be `None`")  # noqa: E501
        if termination_a_id is not None and termination_a_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `termination_a_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if termination_a_id is not None and termination_a_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `termination_a_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._termination_a_id = termination_a_id

    @property
    def termination_a(self):
        """Gets the termination_a of this WritableCable.  # noqa: E501


        :return: The termination_a of this WritableCable.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._termination_a

    @termination_a.setter
    def termination_a(self, termination_a):
        """Sets the termination_a of this WritableCable.


        :param termination_a: The termination_a of this WritableCable.  # noqa: E501
        :type: dict(str, str)
        """

        self._termination_a = termination_a

    @property
    def termination_b_type(self):
        """Gets the termination_b_type of this WritableCable.  # noqa: E501


        :return: The termination_b_type of this WritableCable.  # noqa: E501
        :rtype: str
        """
        return self._termination_b_type

    @termination_b_type.setter
    def termination_b_type(self, termination_b_type):
        """Sets the termination_b_type of this WritableCable.


        :param termination_b_type: The termination_b_type of this WritableCable.  # noqa: E501
        :type: str
        """
        if termination_b_type is None:
            raise ValueError("Invalid value for `termination_b_type`, must not be `None`")  # noqa: E501

        self._termination_b_type = termination_b_type

    @property
    def termination_b_id(self):
        """Gets the termination_b_id of this WritableCable.  # noqa: E501


        :return: The termination_b_id of this WritableCable.  # noqa: E501
        :rtype: int
        """
        return self._termination_b_id

    @termination_b_id.setter
    def termination_b_id(self, termination_b_id):
        """Sets the termination_b_id of this WritableCable.


        :param termination_b_id: The termination_b_id of this WritableCable.  # noqa: E501
        :type: int
        """
        if termination_b_id is None:
            raise ValueError("Invalid value for `termination_b_id`, must not be `None`")  # noqa: E501
        if termination_b_id is not None and termination_b_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `termination_b_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if termination_b_id is not None and termination_b_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `termination_b_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._termination_b_id = termination_b_id

    @property
    def termination_b(self):
        """Gets the termination_b of this WritableCable.  # noqa: E501


        :return: The termination_b of this WritableCable.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._termination_b

    @termination_b.setter
    def termination_b(self, termination_b):
        """Sets the termination_b of this WritableCable.


        :param termination_b: The termination_b of this WritableCable.  # noqa: E501
        :type: dict(str, str)
        """

        self._termination_b = termination_b

    @property
    def type(self):
        """Gets the type of this WritableCable.  # noqa: E501


        :return: The type of this WritableCable.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WritableCable.


        :param type: The type of this WritableCable.  # noqa: E501
        :type: str
        """
        allowed_values = ["cat3", "cat5", "cat5e", "cat6", "cat6a", "cat7", "dac-active", "dac-passive", "mrj21-trunk", "coaxial", "mmf", "mmf-om1", "mmf-om2", "mmf-om3", "mmf-om4", "smf", "smf-os1", "smf-os2", "aoc", "power"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this WritableCable.  # noqa: E501


        :return: The status of this WritableCable.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WritableCable.


        :param status: The status of this WritableCable.  # noqa: E501
        :type: str
        """
        allowed_values = ["connected", "planned", "decommissioning"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def label(self):
        """Gets the label of this WritableCable.  # noqa: E501


        :return: The label of this WritableCable.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this WritableCable.


        :param label: The label of this WritableCable.  # noqa: E501
        :type: str
        """
        if label is not None and len(label) > 100:
            raise ValueError("Invalid value for `label`, length must be less than or equal to `100`")  # noqa: E501

        self._label = label

    @property
    def color(self):
        """Gets the color of this WritableCable.  # noqa: E501


        :return: The color of this WritableCable.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this WritableCable.


        :param color: The color of this WritableCable.  # noqa: E501
        :type: str
        """
        if color is not None and len(color) > 6:
            raise ValueError("Invalid value for `color`, length must be less than or equal to `6`")  # noqa: E501
        if color is not None and not re.search(r'^$|^[0-9a-f]{6}$', color):  # noqa: E501
            raise ValueError(r"Invalid value for `color`, must be a follow pattern or equal to `/^$|^[0-9a-f]{6}$/`")  # noqa: E501

        self._color = color

    @property
    def length(self):
        """Gets the length of this WritableCable.  # noqa: E501


        :return: The length of this WritableCable.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this WritableCable.


        :param length: The length of this WritableCable.  # noqa: E501
        :type: int
        """
        if length is not None and length > 32767:  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value less than or equal to `32767`")  # noqa: E501
        if length is not None and length < 0:  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._length = length

    @property
    def length_unit(self):
        """Gets the length_unit of this WritableCable.  # noqa: E501


        :return: The length_unit of this WritableCable.  # noqa: E501
        :rtype: str
        """
        return self._length_unit

    @length_unit.setter
    def length_unit(self, length_unit):
        """Sets the length_unit of this WritableCable.


        :param length_unit: The length_unit of this WritableCable.  # noqa: E501
        :type: str
        """
        allowed_values = ["m", "cm", "ft", "in"]  # noqa: E501
        if length_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `length_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(length_unit, allowed_values)
            )

        self._length_unit = length_unit

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
        if issubclass(WritableCable, dict):
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
        if not isinstance(other, WritableCable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
