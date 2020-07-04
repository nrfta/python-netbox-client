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


class Type5(object):
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
        'label': 'str',
        'value': 'str'
    }

    attribute_map = {
        'label': 'label',
        'value': 'value'
    }

    def __init__(self, label=None, value=None):  # noqa: E501
        """Type5 - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._value = None
        self.discriminator = None

        self.label = label
        self.value = value

    @property
    def label(self):
        """Gets the label of this Type5.  # noqa: E501


        :return: The label of this Type5.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Type5.


        :param label: The label of this Type5.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501
        allowed_values = ["C5", "C7", "C13", "C15", "C19", "P+N+E 4H", "P+N+E 6H", "P+N+E 9H", "2P+E 4H", "2P+E 6H", "2P+E 9H", "3P+E 4H", "3P+E 6H", "3P+E 9H", "3P+N+E 4H", "3P+N+E 6H", "3P+N+E 9H", "NEMA 5-15R", "NEMA 5-20R", "NEMA 5-30R", "NEMA 5-50R", "NEMA 6-15R", "NEMA 6-20R", "NEMA 6-30R", "NEMA 6-50R", "NEMA L5-15R", "NEMA L5-20R", "NEMA L5-30R", "NEMA L6-15R", "NEMA L6-20R", "NEMA L6-30R", "NEMA L6-50R", "NEMA L14-20R", "NEMA L14-30R", "NEMA L21-20R", "NEMA L21-30R", "CS6360C", "CS6364C", "CS8164C", "CS8264C", "CS8364C", "CS8464C", "ITA Type E (CEE7/5)", "ITA Type F (CEE7/3)", "ITA Type G (BS 1363)", "ITA Type H", "ITA Type I", "ITA Type J", "ITA Type K", "ITA Type L (CEI 23-50)", "ITA Type M (BS 546)", "ITA Type N", "ITA Type O", "HDOT Cx"]  # noqa: E501
        if label not in allowed_values:
            raise ValueError(
                "Invalid value for `label` ({0}), must be one of {1}"  # noqa: E501
                .format(label, allowed_values)
            )

        self._label = label

    @property
    def value(self):
        """Gets the value of this Type5.  # noqa: E501


        :return: The value of this Type5.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Type5.


        :param value: The value of this Type5.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        allowed_values = ["iec-60320-c5", "iec-60320-c7", "iec-60320-c13", "iec-60320-c15", "iec-60320-c19", "iec-60309-p-n-e-4h", "iec-60309-p-n-e-6h", "iec-60309-p-n-e-9h", "iec-60309-2p-e-4h", "iec-60309-2p-e-6h", "iec-60309-2p-e-9h", "iec-60309-3p-e-4h", "iec-60309-3p-e-6h", "iec-60309-3p-e-9h", "iec-60309-3p-n-e-4h", "iec-60309-3p-n-e-6h", "iec-60309-3p-n-e-9h", "nema-5-15r", "nema-5-20r", "nema-5-30r", "nema-5-50r", "nema-6-15r", "nema-6-20r", "nema-6-30r", "nema-6-50r", "nema-l5-15r", "nema-l5-20r", "nema-l5-30r", "nema-l5-50r", "nema-l6-20r", "nema-l6-30r", "nema-l6-50r", "nema-l14-20r", "nema-l14-30r", "nema-l21-20r", "nema-l21-30r", "CS6360C", "CS6364C", "CS8164C", "CS8264C", "CS8364C", "CS8464C", "ita-e", "ita-f", "ita-g", "ita-h", "ita-i", "ita-j", "ita-k", "ita-l", "ita-m", "ita-n", "ita-o", "hdot-cx"]  # noqa: E501
        if value not in allowed_values:
            raise ValueError(
                "Invalid value for `value` ({0}), must be one of {1}"  # noqa: E501
                .format(value, allowed_values)
            )

        self._value = value

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
        if issubclass(Type5, dict):
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
        if not isinstance(other, Type5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other