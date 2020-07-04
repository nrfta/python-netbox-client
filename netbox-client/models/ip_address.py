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


class IPAddress(object):
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
        'family': 'Family',
        'address': 'str',
        'vrf': 'NestedVRF',
        'tenant': 'NestedTenant',
        'status': 'Status6',
        'role': 'Role1',
        'interface': 'IPAddressInterface',
        'nat_inside': 'NestedIPAddress',
        'nat_outside': 'NestedIPAddress',
        'dns_name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'custom_fields': 'object',
        'created': 'date',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'family': 'family',
        'address': 'address',
        'vrf': 'vrf',
        'tenant': 'tenant',
        'status': 'status',
        'role': 'role',
        'interface': 'interface',
        'nat_inside': 'nat_inside',
        'nat_outside': 'nat_outside',
        'dns_name': 'dns_name',
        'description': 'description',
        'tags': 'tags',
        'custom_fields': 'custom_fields',
        'created': 'created',
        'last_updated': 'last_updated'
    }

    def __init__(self, id=None, family=None, address=None, vrf=None, tenant=None, status=None, role=None, interface=None, nat_inside=None, nat_outside=None, dns_name=None, description=None, tags=None, custom_fields=None, created=None, last_updated=None):  # noqa: E501
        """IPAddress - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._family = None
        self._address = None
        self._vrf = None
        self._tenant = None
        self._status = None
        self._role = None
        self._interface = None
        self._nat_inside = None
        self._nat_outside = None
        self._dns_name = None
        self._description = None
        self._tags = None
        self._custom_fields = None
        self._created = None
        self._last_updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if family is not None:
            self.family = family
        self.address = address
        if vrf is not None:
            self.vrf = vrf
        if tenant is not None:
            self.tenant = tenant
        if status is not None:
            self.status = status
        if role is not None:
            self.role = role
        if interface is not None:
            self.interface = interface
        if nat_inside is not None:
            self.nat_inside = nat_inside
        if nat_outside is not None:
            self.nat_outside = nat_outside
        if dns_name is not None:
            self.dns_name = dns_name
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
        """Gets the id of this IPAddress.  # noqa: E501


        :return: The id of this IPAddress.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IPAddress.


        :param id: The id of this IPAddress.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def family(self):
        """Gets the family of this IPAddress.  # noqa: E501


        :return: The family of this IPAddress.  # noqa: E501
        :rtype: Family
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this IPAddress.


        :param family: The family of this IPAddress.  # noqa: E501
        :type: Family
        """

        self._family = family

    @property
    def address(self):
        """Gets the address of this IPAddress.  # noqa: E501

        IPv4 or IPv6 address (with mask)  # noqa: E501

        :return: The address of this IPAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IPAddress.

        IPv4 or IPv6 address (with mask)  # noqa: E501

        :param address: The address of this IPAddress.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def vrf(self):
        """Gets the vrf of this IPAddress.  # noqa: E501


        :return: The vrf of this IPAddress.  # noqa: E501
        :rtype: NestedVRF
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this IPAddress.


        :param vrf: The vrf of this IPAddress.  # noqa: E501
        :type: NestedVRF
        """

        self._vrf = vrf

    @property
    def tenant(self):
        """Gets the tenant of this IPAddress.  # noqa: E501


        :return: The tenant of this IPAddress.  # noqa: E501
        :rtype: NestedTenant
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this IPAddress.


        :param tenant: The tenant of this IPAddress.  # noqa: E501
        :type: NestedTenant
        """

        self._tenant = tenant

    @property
    def status(self):
        """Gets the status of this IPAddress.  # noqa: E501


        :return: The status of this IPAddress.  # noqa: E501
        :rtype: Status6
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IPAddress.


        :param status: The status of this IPAddress.  # noqa: E501
        :type: Status6
        """

        self._status = status

    @property
    def role(self):
        """Gets the role of this IPAddress.  # noqa: E501


        :return: The role of this IPAddress.  # noqa: E501
        :rtype: Role1
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this IPAddress.


        :param role: The role of this IPAddress.  # noqa: E501
        :type: Role1
        """

        self._role = role

    @property
    def interface(self):
        """Gets the interface of this IPAddress.  # noqa: E501


        :return: The interface of this IPAddress.  # noqa: E501
        :rtype: IPAddressInterface
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this IPAddress.


        :param interface: The interface of this IPAddress.  # noqa: E501
        :type: IPAddressInterface
        """

        self._interface = interface

    @property
    def nat_inside(self):
        """Gets the nat_inside of this IPAddress.  # noqa: E501


        :return: The nat_inside of this IPAddress.  # noqa: E501
        :rtype: NestedIPAddress
        """
        return self._nat_inside

    @nat_inside.setter
    def nat_inside(self, nat_inside):
        """Sets the nat_inside of this IPAddress.


        :param nat_inside: The nat_inside of this IPAddress.  # noqa: E501
        :type: NestedIPAddress
        """

        self._nat_inside = nat_inside

    @property
    def nat_outside(self):
        """Gets the nat_outside of this IPAddress.  # noqa: E501


        :return: The nat_outside of this IPAddress.  # noqa: E501
        :rtype: NestedIPAddress
        """
        return self._nat_outside

    @nat_outside.setter
    def nat_outside(self, nat_outside):
        """Sets the nat_outside of this IPAddress.


        :param nat_outside: The nat_outside of this IPAddress.  # noqa: E501
        :type: NestedIPAddress
        """

        self._nat_outside = nat_outside

    @property
    def dns_name(self):
        """Gets the dns_name of this IPAddress.  # noqa: E501

        Hostname or FQDN (not case-sensitive)  # noqa: E501

        :return: The dns_name of this IPAddress.  # noqa: E501
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this IPAddress.

        Hostname or FQDN (not case-sensitive)  # noqa: E501

        :param dns_name: The dns_name of this IPAddress.  # noqa: E501
        :type: str
        """
        if dns_name is not None and len(dns_name) > 255:
            raise ValueError("Invalid value for `dns_name`, length must be less than or equal to `255`")  # noqa: E501
        if dns_name is not None and not re.search(r'^[0-9A-Za-z._-]+$', dns_name):  # noqa: E501
            raise ValueError(r"Invalid value for `dns_name`, must be a follow pattern or equal to `/^[0-9A-Za-z._-]+$/`")  # noqa: E501

        self._dns_name = dns_name

    @property
    def description(self):
        """Gets the description of this IPAddress.  # noqa: E501


        :return: The description of this IPAddress.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IPAddress.


        :param description: The description of this IPAddress.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this IPAddress.  # noqa: E501


        :return: The tags of this IPAddress.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IPAddress.


        :param tags: The tags of this IPAddress.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this IPAddress.  # noqa: E501


        :return: The custom_fields of this IPAddress.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this IPAddress.


        :param custom_fields: The custom_fields of this IPAddress.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def created(self):
        """Gets the created of this IPAddress.  # noqa: E501


        :return: The created of this IPAddress.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this IPAddress.


        :param created: The created of this IPAddress.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this IPAddress.  # noqa: E501


        :return: The last_updated of this IPAddress.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this IPAddress.


        :param last_updated: The last_updated of this IPAddress.  # noqa: E501
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
        if issubclass(IPAddress, dict):
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
        if not isinstance(other, IPAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
