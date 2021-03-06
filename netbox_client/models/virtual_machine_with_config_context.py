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


class VirtualMachineWithConfigContext(object):
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
        'status': 'Status9',
        'site': 'NestedSite',
        'cluster': 'NestedCluster',
        'role': 'NestedDeviceRole',
        'tenant': 'NestedTenant',
        'platform': 'NestedPlatform',
        'primary_ip': 'NestedIPAddress',
        'primary_ip4': 'NestedIPAddress',
        'primary_ip6': 'NestedIPAddress',
        'vcpus': 'int',
        'memory': 'int',
        'disk': 'int',
        'comments': 'str',
        'local_context_data': 'str',
        'tags': 'list[str]',
        'custom_fields': 'object',
        'config_context': 'dict(str, str)',
        'created': 'date',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'site': 'site',
        'cluster': 'cluster',
        'role': 'role',
        'tenant': 'tenant',
        'platform': 'platform',
        'primary_ip': 'primary_ip',
        'primary_ip4': 'primary_ip4',
        'primary_ip6': 'primary_ip6',
        'vcpus': 'vcpus',
        'memory': 'memory',
        'disk': 'disk',
        'comments': 'comments',
        'local_context_data': 'local_context_data',
        'tags': 'tags',
        'custom_fields': 'custom_fields',
        'config_context': 'config_context',
        'created': 'created',
        'last_updated': 'last_updated'
    }

    def __init__(self, id=None, name=None, status=None, site=None, cluster=None, role=None, tenant=None, platform=None, primary_ip=None, primary_ip4=None, primary_ip6=None, vcpus=None, memory=None, disk=None, comments=None, local_context_data=None, tags=None, custom_fields=None, config_context=None, created=None, last_updated=None):  # noqa: E501
        """VirtualMachineWithConfigContext - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._status = None
        self._site = None
        self._cluster = None
        self._role = None
        self._tenant = None
        self._platform = None
        self._primary_ip = None
        self._primary_ip4 = None
        self._primary_ip6 = None
        self._vcpus = None
        self._memory = None
        self._disk = None
        self._comments = None
        self._local_context_data = None
        self._tags = None
        self._custom_fields = None
        self._config_context = None
        self._created = None
        self._last_updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if status is not None:
            self.status = status
        if site is not None:
            self.site = site
        self.cluster = cluster
        if role is not None:
            self.role = role
        if tenant is not None:
            self.tenant = tenant
        if platform is not None:
            self.platform = platform
        if primary_ip is not None:
            self.primary_ip = primary_ip
        if primary_ip4 is not None:
            self.primary_ip4 = primary_ip4
        if primary_ip6 is not None:
            self.primary_ip6 = primary_ip6
        if vcpus is not None:
            self.vcpus = vcpus
        if memory is not None:
            self.memory = memory
        if disk is not None:
            self.disk = disk
        if comments is not None:
            self.comments = comments
        if local_context_data is not None:
            self.local_context_data = local_context_data
        if tags is not None:
            self.tags = tags
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if config_context is not None:
            self.config_context = config_context
        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def id(self):
        """Gets the id of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The id of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualMachineWithConfigContext.


        :param id: The id of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The name of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualMachineWithConfigContext.


        :param name: The name of this VirtualMachineWithConfigContext.  # noqa: E501
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
    def status(self):
        """Gets the status of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The status of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: Status9
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VirtualMachineWithConfigContext.


        :param status: The status of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: Status9
        """

        self._status = status

    @property
    def site(self):
        """Gets the site of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The site of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: NestedSite
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this VirtualMachineWithConfigContext.


        :param site: The site of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: NestedSite
        """

        self._site = site

    @property
    def cluster(self):
        """Gets the cluster of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The cluster of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this VirtualMachineWithConfigContext.


        :param cluster: The cluster of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: NestedCluster
        """
        if cluster is None:
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def role(self):
        """Gets the role of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The role of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: NestedDeviceRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this VirtualMachineWithConfigContext.


        :param role: The role of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: NestedDeviceRole
        """

        self._role = role

    @property
    def tenant(self):
        """Gets the tenant of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The tenant of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: NestedTenant
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this VirtualMachineWithConfigContext.


        :param tenant: The tenant of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: NestedTenant
        """

        self._tenant = tenant

    @property
    def platform(self):
        """Gets the platform of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The platform of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: NestedPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this VirtualMachineWithConfigContext.


        :param platform: The platform of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: NestedPlatform
        """

        self._platform = platform

    @property
    def primary_ip(self):
        """Gets the primary_ip of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The primary_ip of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: NestedIPAddress
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """Sets the primary_ip of this VirtualMachineWithConfigContext.


        :param primary_ip: The primary_ip of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: NestedIPAddress
        """

        self._primary_ip = primary_ip

    @property
    def primary_ip4(self):
        """Gets the primary_ip4 of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The primary_ip4 of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: NestedIPAddress
        """
        return self._primary_ip4

    @primary_ip4.setter
    def primary_ip4(self, primary_ip4):
        """Sets the primary_ip4 of this VirtualMachineWithConfigContext.


        :param primary_ip4: The primary_ip4 of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: NestedIPAddress
        """

        self._primary_ip4 = primary_ip4

    @property
    def primary_ip6(self):
        """Gets the primary_ip6 of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The primary_ip6 of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: NestedIPAddress
        """
        return self._primary_ip6

    @primary_ip6.setter
    def primary_ip6(self, primary_ip6):
        """Sets the primary_ip6 of this VirtualMachineWithConfigContext.


        :param primary_ip6: The primary_ip6 of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: NestedIPAddress
        """

        self._primary_ip6 = primary_ip6

    @property
    def vcpus(self):
        """Gets the vcpus of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The vcpus of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this VirtualMachineWithConfigContext.


        :param vcpus: The vcpus of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: int
        """
        if vcpus is not None and vcpus > 32767:  # noqa: E501
            raise ValueError("Invalid value for `vcpus`, must be a value less than or equal to `32767`")  # noqa: E501
        if vcpus is not None and vcpus < 0:  # noqa: E501
            raise ValueError("Invalid value for `vcpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vcpus = vcpus

    @property
    def memory(self):
        """Gets the memory of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The memory of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this VirtualMachineWithConfigContext.


        :param memory: The memory of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: int
        """
        if memory is not None and memory > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `memory`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if memory is not None and memory < 0:  # noqa: E501
            raise ValueError("Invalid value for `memory`, must be a value greater than or equal to `0`")  # noqa: E501

        self._memory = memory

    @property
    def disk(self):
        """Gets the disk of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The disk of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: int
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this VirtualMachineWithConfigContext.


        :param disk: The disk of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: int
        """
        if disk is not None and disk > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `disk`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if disk is not None and disk < 0:  # noqa: E501
            raise ValueError("Invalid value for `disk`, must be a value greater than or equal to `0`")  # noqa: E501

        self._disk = disk

    @property
    def comments(self):
        """Gets the comments of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The comments of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this VirtualMachineWithConfigContext.


        :param comments: The comments of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def local_context_data(self):
        """Gets the local_context_data of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The local_context_data of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: str
        """
        return self._local_context_data

    @local_context_data.setter
    def local_context_data(self, local_context_data):
        """Sets the local_context_data of this VirtualMachineWithConfigContext.


        :param local_context_data: The local_context_data of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: str
        """

        self._local_context_data = local_context_data

    @property
    def tags(self):
        """Gets the tags of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The tags of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualMachineWithConfigContext.


        :param tags: The tags of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The custom_fields of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this VirtualMachineWithConfigContext.


        :param custom_fields: The custom_fields of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def config_context(self):
        """Gets the config_context of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The config_context of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._config_context

    @config_context.setter
    def config_context(self, config_context):
        """Sets the config_context of this VirtualMachineWithConfigContext.


        :param config_context: The config_context of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: dict(str, str)
        """

        self._config_context = config_context

    @property
    def created(self):
        """Gets the created of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The created of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this VirtualMachineWithConfigContext.


        :param created: The created of this VirtualMachineWithConfigContext.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this VirtualMachineWithConfigContext.  # noqa: E501


        :return: The last_updated of this VirtualMachineWithConfigContext.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this VirtualMachineWithConfigContext.


        :param last_updated: The last_updated of this VirtualMachineWithConfigContext.  # noqa: E501
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
        if issubclass(VirtualMachineWithConfigContext, dict):
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
        if not isinstance(other, VirtualMachineWithConfigContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
