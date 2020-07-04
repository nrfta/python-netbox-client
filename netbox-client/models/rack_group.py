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


class RackGroup(object):
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
        'site': 'NestedSite',
        'parent': 'NestedRackGroup',
        'description': 'str',
        'rack_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'site': 'site',
        'parent': 'parent',
        'description': 'description',
        'rack_count': 'rack_count'
    }

    def __init__(self, id=None, name=None, slug=None, site=None, parent=None, description=None, rack_count=None):  # noqa: E501
        """RackGroup - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._slug = None
        self._site = None
        self._parent = None
        self._description = None
        self._rack_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.slug = slug
        self.site = site
        if parent is not None:
            self.parent = parent
        if description is not None:
            self.description = description
        if rack_count is not None:
            self.rack_count = rack_count

    @property
    def id(self):
        """Gets the id of this RackGroup.  # noqa: E501


        :return: The id of this RackGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RackGroup.


        :param id: The id of this RackGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RackGroup.  # noqa: E501


        :return: The name of this RackGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RackGroup.


        :param name: The name of this RackGroup.  # noqa: E501
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
        """Gets the slug of this RackGroup.  # noqa: E501


        :return: The slug of this RackGroup.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this RackGroup.


        :param slug: The slug of this RackGroup.  # noqa: E501
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
    def site(self):
        """Gets the site of this RackGroup.  # noqa: E501


        :return: The site of this RackGroup.  # noqa: E501
        :rtype: NestedSite
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this RackGroup.


        :param site: The site of this RackGroup.  # noqa: E501
        :type: NestedSite
        """
        if site is None:
            raise ValueError("Invalid value for `site`, must not be `None`")  # noqa: E501

        self._site = site

    @property
    def parent(self):
        """Gets the parent of this RackGroup.  # noqa: E501


        :return: The parent of this RackGroup.  # noqa: E501
        :rtype: NestedRackGroup
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this RackGroup.


        :param parent: The parent of this RackGroup.  # noqa: E501
        :type: NestedRackGroup
        """

        self._parent = parent

    @property
    def description(self):
        """Gets the description of this RackGroup.  # noqa: E501


        :return: The description of this RackGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RackGroup.


        :param description: The description of this RackGroup.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def rack_count(self):
        """Gets the rack_count of this RackGroup.  # noqa: E501


        :return: The rack_count of this RackGroup.  # noqa: E501
        :rtype: int
        """
        return self._rack_count

    @rack_count.setter
    def rack_count(self, rack_count):
        """Sets the rack_count of this RackGroup.


        :param rack_count: The rack_count of this RackGroup.  # noqa: E501
        :type: int
        """

        self._rack_count = rack_count

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
        if issubclass(RackGroup, dict):
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
        if not isinstance(other, RackGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
