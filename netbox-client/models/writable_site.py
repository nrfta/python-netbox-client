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


class WritableSite(object):
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
        'status': 'str',
        'region': 'int',
        'tenant': 'int',
        'facility': 'str',
        'asn': 'int',
        'time_zone': 'str',
        'description': 'str',
        'physical_address': 'str',
        'shipping_address': 'str',
        'latitude': 'str',
        'longitude': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'contact_email': 'str',
        'comments': 'str',
        'tags': 'list[str]',
        'custom_fields': 'object',
        'created': 'date',
        'last_updated': 'datetime',
        'circuit_count': 'int',
        'device_count': 'int',
        'prefix_count': 'int',
        'rack_count': 'int',
        'virtualmachine_count': 'int',
        'vlan_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'status': 'status',
        'region': 'region',
        'tenant': 'tenant',
        'facility': 'facility',
        'asn': 'asn',
        'time_zone': 'time_zone',
        'description': 'description',
        'physical_address': 'physical_address',
        'shipping_address': 'shipping_address',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'contact_name': 'contact_name',
        'contact_phone': 'contact_phone',
        'contact_email': 'contact_email',
        'comments': 'comments',
        'tags': 'tags',
        'custom_fields': 'custom_fields',
        'created': 'created',
        'last_updated': 'last_updated',
        'circuit_count': 'circuit_count',
        'device_count': 'device_count',
        'prefix_count': 'prefix_count',
        'rack_count': 'rack_count',
        'virtualmachine_count': 'virtualmachine_count',
        'vlan_count': 'vlan_count'
    }

    def __init__(self, id=None, name=None, slug=None, status=None, region=None, tenant=None, facility=None, asn=None, time_zone=None, description=None, physical_address=None, shipping_address=None, latitude=None, longitude=None, contact_name=None, contact_phone=None, contact_email=None, comments=None, tags=None, custom_fields=None, created=None, last_updated=None, circuit_count=None, device_count=None, prefix_count=None, rack_count=None, virtualmachine_count=None, vlan_count=None):  # noqa: E501
        """WritableSite - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._slug = None
        self._status = None
        self._region = None
        self._tenant = None
        self._facility = None
        self._asn = None
        self._time_zone = None
        self._description = None
        self._physical_address = None
        self._shipping_address = None
        self._latitude = None
        self._longitude = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_email = None
        self._comments = None
        self._tags = None
        self._custom_fields = None
        self._created = None
        self._last_updated = None
        self._circuit_count = None
        self._device_count = None
        self._prefix_count = None
        self._rack_count = None
        self._virtualmachine_count = None
        self._vlan_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.slug = slug
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if tenant is not None:
            self.tenant = tenant
        if facility is not None:
            self.facility = facility
        if asn is not None:
            self.asn = asn
        if time_zone is not None:
            self.time_zone = time_zone
        if description is not None:
            self.description = description
        if physical_address is not None:
            self.physical_address = physical_address
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_phone is not None:
            self.contact_phone = contact_phone
        if contact_email is not None:
            self.contact_email = contact_email
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
        if circuit_count is not None:
            self.circuit_count = circuit_count
        if device_count is not None:
            self.device_count = device_count
        if prefix_count is not None:
            self.prefix_count = prefix_count
        if rack_count is not None:
            self.rack_count = rack_count
        if virtualmachine_count is not None:
            self.virtualmachine_count = virtualmachine_count
        if vlan_count is not None:
            self.vlan_count = vlan_count

    @property
    def id(self):
        """Gets the id of this WritableSite.  # noqa: E501


        :return: The id of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableSite.


        :param id: The id of this WritableSite.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WritableSite.  # noqa: E501


        :return: The name of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WritableSite.


        :param name: The name of this WritableSite.  # noqa: E501
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
        """Gets the slug of this WritableSite.  # noqa: E501


        :return: The slug of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this WritableSite.


        :param slug: The slug of this WritableSite.  # noqa: E501
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
    def status(self):
        """Gets the status of this WritableSite.  # noqa: E501


        :return: The status of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WritableSite.


        :param status: The status of this WritableSite.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "planned", "retired"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def region(self):
        """Gets the region of this WritableSite.  # noqa: E501


        :return: The region of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this WritableSite.


        :param region: The region of this WritableSite.  # noqa: E501
        :type: int
        """

        self._region = region

    @property
    def tenant(self):
        """Gets the tenant of this WritableSite.  # noqa: E501


        :return: The tenant of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this WritableSite.


        :param tenant: The tenant of this WritableSite.  # noqa: E501
        :type: int
        """

        self._tenant = tenant

    @property
    def facility(self):
        """Gets the facility of this WritableSite.  # noqa: E501

        Local facility ID or description  # noqa: E501

        :return: The facility of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this WritableSite.

        Local facility ID or description  # noqa: E501

        :param facility: The facility of this WritableSite.  # noqa: E501
        :type: str
        """
        if facility is not None and len(facility) > 50:
            raise ValueError("Invalid value for `facility`, length must be less than or equal to `50`")  # noqa: E501

        self._facility = facility

    @property
    def asn(self):
        """Gets the asn of this WritableSite.  # noqa: E501

        32-bit autonomous system number  # noqa: E501

        :return: The asn of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this WritableSite.

        32-bit autonomous system number  # noqa: E501

        :param asn: The asn of this WritableSite.  # noqa: E501
        :type: int
        """
        if asn is not None and asn > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `asn`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if asn is not None and asn < 1:  # noqa: E501
            raise ValueError("Invalid value for `asn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._asn = asn

    @property
    def time_zone(self):
        """Gets the time_zone of this WritableSite.  # noqa: E501


        :return: The time_zone of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this WritableSite.


        :param time_zone: The time_zone of this WritableSite.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def description(self):
        """Gets the description of this WritableSite.  # noqa: E501


        :return: The description of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WritableSite.


        :param description: The description of this WritableSite.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def physical_address(self):
        """Gets the physical_address of this WritableSite.  # noqa: E501


        :return: The physical_address of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._physical_address

    @physical_address.setter
    def physical_address(self, physical_address):
        """Sets the physical_address of this WritableSite.


        :param physical_address: The physical_address of this WritableSite.  # noqa: E501
        :type: str
        """
        if physical_address is not None and len(physical_address) > 200:
            raise ValueError("Invalid value for `physical_address`, length must be less than or equal to `200`")  # noqa: E501

        self._physical_address = physical_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this WritableSite.  # noqa: E501


        :return: The shipping_address of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this WritableSite.


        :param shipping_address: The shipping_address of this WritableSite.  # noqa: E501
        :type: str
        """
        if shipping_address is not None and len(shipping_address) > 200:
            raise ValueError("Invalid value for `shipping_address`, length must be less than or equal to `200`")  # noqa: E501

        self._shipping_address = shipping_address

    @property
    def latitude(self):
        """Gets the latitude of this WritableSite.  # noqa: E501

        GPS coordinate (latitude)  # noqa: E501

        :return: The latitude of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this WritableSite.

        GPS coordinate (latitude)  # noqa: E501

        :param latitude: The latitude of this WritableSite.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this WritableSite.  # noqa: E501

        GPS coordinate (longitude)  # noqa: E501

        :return: The longitude of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this WritableSite.

        GPS coordinate (longitude)  # noqa: E501

        :param longitude: The longitude of this WritableSite.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

    @property
    def contact_name(self):
        """Gets the contact_name of this WritableSite.  # noqa: E501


        :return: The contact_name of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this WritableSite.


        :param contact_name: The contact_name of this WritableSite.  # noqa: E501
        :type: str
        """
        if contact_name is not None and len(contact_name) > 50:
            raise ValueError("Invalid value for `contact_name`, length must be less than or equal to `50`")  # noqa: E501

        self._contact_name = contact_name

    @property
    def contact_phone(self):
        """Gets the contact_phone of this WritableSite.  # noqa: E501


        :return: The contact_phone of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this WritableSite.


        :param contact_phone: The contact_phone of this WritableSite.  # noqa: E501
        :type: str
        """
        if contact_phone is not None and len(contact_phone) > 20:
            raise ValueError("Invalid value for `contact_phone`, length must be less than or equal to `20`")  # noqa: E501

        self._contact_phone = contact_phone

    @property
    def contact_email(self):
        """Gets the contact_email of this WritableSite.  # noqa: E501


        :return: The contact_email of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this WritableSite.


        :param contact_email: The contact_email of this WritableSite.  # noqa: E501
        :type: str
        """
        if contact_email is not None and len(contact_email) > 254:
            raise ValueError("Invalid value for `contact_email`, length must be less than or equal to `254`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def comments(self):
        """Gets the comments of this WritableSite.  # noqa: E501


        :return: The comments of this WritableSite.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this WritableSite.


        :param comments: The comments of this WritableSite.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def tags(self):
        """Gets the tags of this WritableSite.  # noqa: E501


        :return: The tags of this WritableSite.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WritableSite.


        :param tags: The tags of this WritableSite.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this WritableSite.  # noqa: E501


        :return: The custom_fields of this WritableSite.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this WritableSite.


        :param custom_fields: The custom_fields of this WritableSite.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def created(self):
        """Gets the created of this WritableSite.  # noqa: E501


        :return: The created of this WritableSite.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WritableSite.


        :param created: The created of this WritableSite.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this WritableSite.  # noqa: E501


        :return: The last_updated of this WritableSite.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this WritableSite.


        :param last_updated: The last_updated of this WritableSite.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def circuit_count(self):
        """Gets the circuit_count of this WritableSite.  # noqa: E501


        :return: The circuit_count of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._circuit_count

    @circuit_count.setter
    def circuit_count(self, circuit_count):
        """Sets the circuit_count of this WritableSite.


        :param circuit_count: The circuit_count of this WritableSite.  # noqa: E501
        :type: int
        """

        self._circuit_count = circuit_count

    @property
    def device_count(self):
        """Gets the device_count of this WritableSite.  # noqa: E501


        :return: The device_count of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        """Sets the device_count of this WritableSite.


        :param device_count: The device_count of this WritableSite.  # noqa: E501
        :type: int
        """

        self._device_count = device_count

    @property
    def prefix_count(self):
        """Gets the prefix_count of this WritableSite.  # noqa: E501


        :return: The prefix_count of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._prefix_count

    @prefix_count.setter
    def prefix_count(self, prefix_count):
        """Sets the prefix_count of this WritableSite.


        :param prefix_count: The prefix_count of this WritableSite.  # noqa: E501
        :type: int
        """

        self._prefix_count = prefix_count

    @property
    def rack_count(self):
        """Gets the rack_count of this WritableSite.  # noqa: E501


        :return: The rack_count of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._rack_count

    @rack_count.setter
    def rack_count(self, rack_count):
        """Sets the rack_count of this WritableSite.


        :param rack_count: The rack_count of this WritableSite.  # noqa: E501
        :type: int
        """

        self._rack_count = rack_count

    @property
    def virtualmachine_count(self):
        """Gets the virtualmachine_count of this WritableSite.  # noqa: E501


        :return: The virtualmachine_count of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._virtualmachine_count

    @virtualmachine_count.setter
    def virtualmachine_count(self, virtualmachine_count):
        """Sets the virtualmachine_count of this WritableSite.


        :param virtualmachine_count: The virtualmachine_count of this WritableSite.  # noqa: E501
        :type: int
        """

        self._virtualmachine_count = virtualmachine_count

    @property
    def vlan_count(self):
        """Gets the vlan_count of this WritableSite.  # noqa: E501


        :return: The vlan_count of this WritableSite.  # noqa: E501
        :rtype: int
        """
        return self._vlan_count

    @vlan_count.setter
    def vlan_count(self, vlan_count):
        """Sets the vlan_count of this WritableSite.


        :param vlan_count: The vlan_count of this WritableSite.  # noqa: E501
        :type: int
        """

        self._vlan_count = vlan_count

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
        if issubclass(WritableSite, dict):
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
        if not isinstance(other, WritableSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
