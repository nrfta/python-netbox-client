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


class ObjectChange(object):
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
        'time': 'datetime',
        'user': 'NestedUser',
        'user_name': 'str',
        'request_id': 'str',
        'action': 'Action',
        'changed_object_type': 'str',
        'changed_object_id': 'int',
        'changed_object': 'dict(str, str)',
        'object_data': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'user': 'user',
        'user_name': 'user_name',
        'request_id': 'request_id',
        'action': 'action',
        'changed_object_type': 'changed_object_type',
        'changed_object_id': 'changed_object_id',
        'changed_object': 'changed_object',
        'object_data': 'object_data'
    }

    def __init__(self, id=None, time=None, user=None, user_name=None, request_id=None, action=None, changed_object_type=None, changed_object_id=None, changed_object=None, object_data=None):  # noqa: E501
        """ObjectChange - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._time = None
        self._user = None
        self._user_name = None
        self._request_id = None
        self._action = None
        self._changed_object_type = None
        self._changed_object_id = None
        self._changed_object = None
        self._object_data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if time is not None:
            self.time = time
        if user is not None:
            self.user = user
        if user_name is not None:
            self.user_name = user_name
        if request_id is not None:
            self.request_id = request_id
        if action is not None:
            self.action = action
        if changed_object_type is not None:
            self.changed_object_type = changed_object_type
        self.changed_object_id = changed_object_id
        if changed_object is not None:
            self.changed_object = changed_object
        if object_data is not None:
            self.object_data = object_data

    @property
    def id(self):
        """Gets the id of this ObjectChange.  # noqa: E501


        :return: The id of this ObjectChange.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectChange.


        :param id: The id of this ObjectChange.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this ObjectChange.  # noqa: E501


        :return: The time of this ObjectChange.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ObjectChange.


        :param time: The time of this ObjectChange.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def user(self):
        """Gets the user of this ObjectChange.  # noqa: E501


        :return: The user of this ObjectChange.  # noqa: E501
        :rtype: NestedUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ObjectChange.


        :param user: The user of this ObjectChange.  # noqa: E501
        :type: NestedUser
        """

        self._user = user

    @property
    def user_name(self):
        """Gets the user_name of this ObjectChange.  # noqa: E501


        :return: The user_name of this ObjectChange.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ObjectChange.


        :param user_name: The user_name of this ObjectChange.  # noqa: E501
        :type: str
        """
        if user_name is not None and len(user_name) < 1:
            raise ValueError("Invalid value for `user_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_name = user_name

    @property
    def request_id(self):
        """Gets the request_id of this ObjectChange.  # noqa: E501


        :return: The request_id of this ObjectChange.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ObjectChange.


        :param request_id: The request_id of this ObjectChange.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def action(self):
        """Gets the action of this ObjectChange.  # noqa: E501


        :return: The action of this ObjectChange.  # noqa: E501
        :rtype: Action
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ObjectChange.


        :param action: The action of this ObjectChange.  # noqa: E501
        :type: Action
        """

        self._action = action

    @property
    def changed_object_type(self):
        """Gets the changed_object_type of this ObjectChange.  # noqa: E501


        :return: The changed_object_type of this ObjectChange.  # noqa: E501
        :rtype: str
        """
        return self._changed_object_type

    @changed_object_type.setter
    def changed_object_type(self, changed_object_type):
        """Sets the changed_object_type of this ObjectChange.


        :param changed_object_type: The changed_object_type of this ObjectChange.  # noqa: E501
        :type: str
        """

        self._changed_object_type = changed_object_type

    @property
    def changed_object_id(self):
        """Gets the changed_object_id of this ObjectChange.  # noqa: E501


        :return: The changed_object_id of this ObjectChange.  # noqa: E501
        :rtype: int
        """
        return self._changed_object_id

    @changed_object_id.setter
    def changed_object_id(self, changed_object_id):
        """Sets the changed_object_id of this ObjectChange.


        :param changed_object_id: The changed_object_id of this ObjectChange.  # noqa: E501
        :type: int
        """
        if changed_object_id is None:
            raise ValueError("Invalid value for `changed_object_id`, must not be `None`")  # noqa: E501
        if changed_object_id is not None and changed_object_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `changed_object_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if changed_object_id is not None and changed_object_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `changed_object_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._changed_object_id = changed_object_id

    @property
    def changed_object(self):
        """Gets the changed_object of this ObjectChange.  # noqa: E501

         Serialize a nested representation of the changed object.   # noqa: E501

        :return: The changed_object of this ObjectChange.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._changed_object

    @changed_object.setter
    def changed_object(self, changed_object):
        """Sets the changed_object of this ObjectChange.

         Serialize a nested representation of the changed object.   # noqa: E501

        :param changed_object: The changed_object of this ObjectChange.  # noqa: E501
        :type: dict(str, str)
        """

        self._changed_object = changed_object

    @property
    def object_data(self):
        """Gets the object_data of this ObjectChange.  # noqa: E501


        :return: The object_data of this ObjectChange.  # noqa: E501
        :rtype: str
        """
        return self._object_data

    @object_data.setter
    def object_data(self, object_data):
        """Sets the object_data of this ObjectChange.


        :param object_data: The object_data of this ObjectChange.  # noqa: E501
        :type: str
        """

        self._object_data = object_data

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
        if issubclass(ObjectChange, dict):
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
        if not isinstance(other, ObjectChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
