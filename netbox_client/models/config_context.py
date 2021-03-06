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


class ConfigContext(object):
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
        'weight': 'int',
        'description': 'str',
        'is_active': 'bool',
        'regions': 'list[NestedRegion]',
        'sites': 'list[NestedSite]',
        'roles': 'list[NestedDeviceRole]',
        'platforms': 'list[NestedPlatform]',
        'cluster_groups': 'list[NestedClusterGroup]',
        'clusters': 'list[NestedCluster]',
        'tenant_groups': 'list[NestedTenantGroup]',
        'tenants': 'list[NestedTenant]',
        'tags': 'list[str]',
        'data': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'weight': 'weight',
        'description': 'description',
        'is_active': 'is_active',
        'regions': 'regions',
        'sites': 'sites',
        'roles': 'roles',
        'platforms': 'platforms',
        'cluster_groups': 'cluster_groups',
        'clusters': 'clusters',
        'tenant_groups': 'tenant_groups',
        'tenants': 'tenants',
        'tags': 'tags',
        'data': 'data'
    }

    def __init__(self, id=None, name=None, weight=None, description=None, is_active=None, regions=None, sites=None, roles=None, platforms=None, cluster_groups=None, clusters=None, tenant_groups=None, tenants=None, tags=None, data=None):  # noqa: E501
        """ConfigContext - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._weight = None
        self._description = None
        self._is_active = None
        self._regions = None
        self._sites = None
        self._roles = None
        self._platforms = None
        self._cluster_groups = None
        self._clusters = None
        self._tenant_groups = None
        self._tenants = None
        self._tags = None
        self._data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if weight is not None:
            self.weight = weight
        if description is not None:
            self.description = description
        if is_active is not None:
            self.is_active = is_active
        if regions is not None:
            self.regions = regions
        if sites is not None:
            self.sites = sites
        if roles is not None:
            self.roles = roles
        if platforms is not None:
            self.platforms = platforms
        if cluster_groups is not None:
            self.cluster_groups = cluster_groups
        if clusters is not None:
            self.clusters = clusters
        if tenant_groups is not None:
            self.tenant_groups = tenant_groups
        if tenants is not None:
            self.tenants = tenants
        if tags is not None:
            self.tags = tags
        self.data = data

    @property
    def id(self):
        """Gets the id of this ConfigContext.  # noqa: E501


        :return: The id of this ConfigContext.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigContext.


        :param id: The id of this ConfigContext.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ConfigContext.  # noqa: E501


        :return: The name of this ConfigContext.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigContext.


        :param name: The name of this ConfigContext.  # noqa: E501
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
    def weight(self):
        """Gets the weight of this ConfigContext.  # noqa: E501


        :return: The weight of this ConfigContext.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ConfigContext.


        :param weight: The weight of this ConfigContext.  # noqa: E501
        :type: int
        """
        if weight is not None and weight > 32767:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must be a value less than or equal to `32767`")  # noqa: E501
        if weight is not None and weight < 0:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weight = weight

    @property
    def description(self):
        """Gets the description of this ConfigContext.  # noqa: E501


        :return: The description of this ConfigContext.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigContext.


        :param description: The description of this ConfigContext.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def is_active(self):
        """Gets the is_active of this ConfigContext.  # noqa: E501


        :return: The is_active of this ConfigContext.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ConfigContext.


        :param is_active: The is_active of this ConfigContext.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def regions(self):
        """Gets the regions of this ConfigContext.  # noqa: E501


        :return: The regions of this ConfigContext.  # noqa: E501
        :rtype: list[NestedRegion]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ConfigContext.


        :param regions: The regions of this ConfigContext.  # noqa: E501
        :type: list[NestedRegion]
        """

        self._regions = regions

    @property
    def sites(self):
        """Gets the sites of this ConfigContext.  # noqa: E501


        :return: The sites of this ConfigContext.  # noqa: E501
        :rtype: list[NestedSite]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this ConfigContext.


        :param sites: The sites of this ConfigContext.  # noqa: E501
        :type: list[NestedSite]
        """

        self._sites = sites

    @property
    def roles(self):
        """Gets the roles of this ConfigContext.  # noqa: E501


        :return: The roles of this ConfigContext.  # noqa: E501
        :rtype: list[NestedDeviceRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ConfigContext.


        :param roles: The roles of this ConfigContext.  # noqa: E501
        :type: list[NestedDeviceRole]
        """

        self._roles = roles

    @property
    def platforms(self):
        """Gets the platforms of this ConfigContext.  # noqa: E501


        :return: The platforms of this ConfigContext.  # noqa: E501
        :rtype: list[NestedPlatform]
        """
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        """Sets the platforms of this ConfigContext.


        :param platforms: The platforms of this ConfigContext.  # noqa: E501
        :type: list[NestedPlatform]
        """

        self._platforms = platforms

    @property
    def cluster_groups(self):
        """Gets the cluster_groups of this ConfigContext.  # noqa: E501


        :return: The cluster_groups of this ConfigContext.  # noqa: E501
        :rtype: list[NestedClusterGroup]
        """
        return self._cluster_groups

    @cluster_groups.setter
    def cluster_groups(self, cluster_groups):
        """Sets the cluster_groups of this ConfigContext.


        :param cluster_groups: The cluster_groups of this ConfigContext.  # noqa: E501
        :type: list[NestedClusterGroup]
        """

        self._cluster_groups = cluster_groups

    @property
    def clusters(self):
        """Gets the clusters of this ConfigContext.  # noqa: E501


        :return: The clusters of this ConfigContext.  # noqa: E501
        :rtype: list[NestedCluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this ConfigContext.


        :param clusters: The clusters of this ConfigContext.  # noqa: E501
        :type: list[NestedCluster]
        """

        self._clusters = clusters

    @property
    def tenant_groups(self):
        """Gets the tenant_groups of this ConfigContext.  # noqa: E501


        :return: The tenant_groups of this ConfigContext.  # noqa: E501
        :rtype: list[NestedTenantGroup]
        """
        return self._tenant_groups

    @tenant_groups.setter
    def tenant_groups(self, tenant_groups):
        """Sets the tenant_groups of this ConfigContext.


        :param tenant_groups: The tenant_groups of this ConfigContext.  # noqa: E501
        :type: list[NestedTenantGroup]
        """

        self._tenant_groups = tenant_groups

    @property
    def tenants(self):
        """Gets the tenants of this ConfigContext.  # noqa: E501


        :return: The tenants of this ConfigContext.  # noqa: E501
        :rtype: list[NestedTenant]
        """
        return self._tenants

    @tenants.setter
    def tenants(self, tenants):
        """Sets the tenants of this ConfigContext.


        :param tenants: The tenants of this ConfigContext.  # noqa: E501
        :type: list[NestedTenant]
        """

        self._tenants = tenants

    @property
    def tags(self):
        """Gets the tags of this ConfigContext.  # noqa: E501


        :return: The tags of this ConfigContext.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ConfigContext.


        :param tags: The tags of this ConfigContext.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def data(self):
        """Gets the data of this ConfigContext.  # noqa: E501


        :return: The data of this ConfigContext.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ConfigContext.


        :param data: The data of this ConfigContext.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(ConfigContext, dict):
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
        if not isinstance(other, ConfigContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
