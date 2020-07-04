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


class WritableCluster(object):
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
        'type': 'int',
        'group': 'int',
        'tenant': 'int',
        'site': 'int',
        'comments': 'str',
        'tags': 'list[str]',
        'custom_fields': 'object',
        'created': 'date',
        'last_updated': 'datetime',
        'device_count': 'int',
        'virtualmachine_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'group': 'group',
        'tenant': 'tenant',
        'site': 'site',
        'comments': 'comments',
        'tags': 'tags',
        'custom_fields': 'custom_fields',
        'created': 'created',
        'last_updated': 'last_updated',
        'device_count': 'device_count',
        'virtualmachine_count': 'virtualmachine_count'
    }

    def __init__(self, id=None, name=None, type=None, group=None, tenant=None, site=None, comments=None, tags=None, custom_fields=None, created=None, last_updated=None, device_count=None, virtualmachine_count=None):  # noqa: E501
        """WritableCluster - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._type = None
        self._group = None
        self._tenant = None
        self._site = None
        self._comments = None
        self._tags = None
        self._custom_fields = None
        self._created = None
        self._last_updated = None
        self._device_count = None
        self._virtualmachine_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.type = type
        if group is not None:
            self.group = group
        if tenant is not None:
            self.tenant = tenant
        if site is not None:
            self.site = site
        if comments is not None:
            self.comments = comments
        if tags is not None:
            self.tags = tags
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated
        if device_count is not None:
            self.device_count = device_count
        if virtualmachine_count is not None:
            self.virtualmachine_count = virtualmachine_count

    @property
    def id(self):
        """Gets the id of this WritableCluster.  # noqa: E501


        :return: The id of this WritableCluster.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableCluster.


        :param id: The id of this WritableCluster.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WritableCluster.  # noqa: E501


        :return: The name of this WritableCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WritableCluster.


        :param name: The name of this WritableCluster.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this WritableCluster.  # noqa: E501


        :return: The type of this WritableCluster.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WritableCluster.


        :param type: The type of this WritableCluster.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def group(self):
        """Gets the group of this WritableCluster.  # noqa: E501


        :return: The group of this WritableCluster.  # noqa: E501
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this WritableCluster.


        :param group: The group of this WritableCluster.  # noqa: E501
        :type: int
        """

        self._group = group

    @property
    def tenant(self):
        """Gets the tenant of this WritableCluster.  # noqa: E501


        :return: The tenant of this WritableCluster.  # noqa: E501
        :rtype: int
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this WritableCluster.


        :param tenant: The tenant of this WritableCluster.  # noqa: E501
        :type: int
        """

        self._tenant = tenant

    @property
    def site(self):
        """Gets the site of this WritableCluster.  # noqa: E501


        :return: The site of this WritableCluster.  # noqa: E501
        :rtype: int
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this WritableCluster.


        :param site: The site of this WritableCluster.  # noqa: E501
        :type: int
        """

        self._site = site

    @property
    def comments(self):
        """Gets the comments of this WritableCluster.  # noqa: E501


        :return: The comments of this WritableCluster.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this WritableCluster.


        :param comments: The comments of this WritableCluster.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def tags(self):
        """Gets the tags of this WritableCluster.  # noqa: E501


        :return: The tags of this WritableCluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WritableCluster.


        :param tags: The tags of this WritableCluster.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this WritableCluster.  # noqa: E501


        :return: The custom_fields of this WritableCluster.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this WritableCluster.


        :param custom_fields: The custom_fields of this WritableCluster.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def created(self):
        """Gets the created of this WritableCluster.  # noqa: E501


        :return: The created of this WritableCluster.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WritableCluster.


        :param created: The created of this WritableCluster.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this WritableCluster.  # noqa: E501


        :return: The last_updated of this WritableCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this WritableCluster.


        :param last_updated: The last_updated of this WritableCluster.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def device_count(self):
        """Gets the device_count of this WritableCluster.  # noqa: E501


        :return: The device_count of this WritableCluster.  # noqa: E501
        :rtype: int
        """
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        """Sets the device_count of this WritableCluster.


        :param device_count: The device_count of this WritableCluster.  # noqa: E501
        :type: int
        """

        self._device_count = device_count

    @property
    def virtualmachine_count(self):
        """Gets the virtualmachine_count of this WritableCluster.  # noqa: E501


        :return: The virtualmachine_count of this WritableCluster.  # noqa: E501
        :rtype: int
        """
        return self._virtualmachine_count

    @virtualmachine_count.setter
    def virtualmachine_count(self, virtualmachine_count):
        """Sets the virtualmachine_count of this WritableCluster.


        :param virtualmachine_count: The virtualmachine_count of this WritableCluster.  # noqa: E501
        :type: int
        """

        self._virtualmachine_count = virtualmachine_count

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
        if issubclass(WritableCluster, dict):
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
        if not isinstance(other, WritableCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
