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


class NestedDeviceType(object):
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
        'url': 'str',
        'manufacturer': 'NestedManufacturer',
        'model': 'str',
        'slug': 'str',
        'display_name': 'str',
        'device_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'slug': 'slug',
        'display_name': 'display_name',
        'device_count': 'device_count'
    }

    def __init__(self, id=None, url=None, manufacturer=None, model=None, slug=None, display_name=None, device_count=None):  # noqa: E501
        """NestedDeviceType - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._manufacturer = None
        self._model = None
        self._slug = None
        self._display_name = None
        self._device_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if manufacturer is not None:
            self.manufacturer = manufacturer
        self.model = model
        self.slug = slug
        if display_name is not None:
            self.display_name = display_name
        if device_count is not None:
            self.device_count = device_count

    @property
    def id(self):
        """Gets the id of this NestedDeviceType.  # noqa: E501


        :return: The id of this NestedDeviceType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedDeviceType.


        :param id: The id of this NestedDeviceType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this NestedDeviceType.  # noqa: E501


        :return: The url of this NestedDeviceType.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NestedDeviceType.


        :param url: The url of this NestedDeviceType.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def manufacturer(self):
        """Gets the manufacturer of this NestedDeviceType.  # noqa: E501


        :return: The manufacturer of this NestedDeviceType.  # noqa: E501
        :rtype: NestedManufacturer
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this NestedDeviceType.


        :param manufacturer: The manufacturer of this NestedDeviceType.  # noqa: E501
        :type: NestedManufacturer
        """

        self._manufacturer = manufacturer

    @property
    def model(self):
        """Gets the model of this NestedDeviceType.  # noqa: E501


        :return: The model of this NestedDeviceType.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this NestedDeviceType.


        :param model: The model of this NestedDeviceType.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        if model is not None and len(model) > 50:
            raise ValueError("Invalid value for `model`, length must be less than or equal to `50`")  # noqa: E501
        if model is not None and len(model) < 1:
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `1`")  # noqa: E501

        self._model = model

    @property
    def slug(self):
        """Gets the slug of this NestedDeviceType.  # noqa: E501


        :return: The slug of this NestedDeviceType.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this NestedDeviceType.


        :param slug: The slug of this NestedDeviceType.  # noqa: E501
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
    def display_name(self):
        """Gets the display_name of this NestedDeviceType.  # noqa: E501


        :return: The display_name of this NestedDeviceType.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NestedDeviceType.


        :param display_name: The display_name of this NestedDeviceType.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def device_count(self):
        """Gets the device_count of this NestedDeviceType.  # noqa: E501


        :return: The device_count of this NestedDeviceType.  # noqa: E501
        :rtype: int
        """
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        """Sets the device_count of this NestedDeviceType.


        :param device_count: The device_count of this NestedDeviceType.  # noqa: E501
        :type: int
        """

        self._device_count = device_count

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
        if issubclass(NestedDeviceType, dict):
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
        if not isinstance(other, NestedDeviceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other