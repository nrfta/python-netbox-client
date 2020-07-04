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


class ImageAttachment(object):
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
        'content_type': 'str',
        'object_id': 'int',
        'parent': 'dict(str, str)',
        'name': 'str',
        'image': 'str',
        'image_height': 'int',
        'image_width': 'int',
        'created': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'content_type': 'content_type',
        'object_id': 'object_id',
        'parent': 'parent',
        'name': 'name',
        'image': 'image',
        'image_height': 'image_height',
        'image_width': 'image_width',
        'created': 'created'
    }

    def __init__(self, id=None, content_type=None, object_id=None, parent=None, name=None, image=None, image_height=None, image_width=None, created=None):  # noqa: E501
        """ImageAttachment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._content_type = None
        self._object_id = None
        self._parent = None
        self._name = None
        self._image = None
        self._image_height = None
        self._image_width = None
        self._created = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.content_type = content_type
        self.object_id = object_id
        if parent is not None:
            self.parent = parent
        if name is not None:
            self.name = name
        if image is not None:
            self.image = image
        self.image_height = image_height
        self.image_width = image_width
        if created is not None:
            self.created = created

    @property
    def id(self):
        """Gets the id of this ImageAttachment.  # noqa: E501


        :return: The id of this ImageAttachment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageAttachment.


        :param id: The id of this ImageAttachment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def content_type(self):
        """Gets the content_type of this ImageAttachment.  # noqa: E501


        :return: The content_type of this ImageAttachment.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ImageAttachment.


        :param content_type: The content_type of this ImageAttachment.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def object_id(self):
        """Gets the object_id of this ImageAttachment.  # noqa: E501


        :return: The object_id of this ImageAttachment.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ImageAttachment.


        :param object_id: The object_id of this ImageAttachment.  # noqa: E501
        :type: int
        """
        if object_id is None:
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501
        if object_id is not None and object_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `object_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if object_id is not None and object_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `object_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._object_id = object_id

    @property
    def parent(self):
        """Gets the parent of this ImageAttachment.  # noqa: E501


        :return: The parent of this ImageAttachment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ImageAttachment.


        :param parent: The parent of this ImageAttachment.  # noqa: E501
        :type: dict(str, str)
        """

        self._parent = parent

    @property
    def name(self):
        """Gets the name of this ImageAttachment.  # noqa: E501


        :return: The name of this ImageAttachment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageAttachment.


        :param name: The name of this ImageAttachment.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def image(self):
        """Gets the image of this ImageAttachment.  # noqa: E501


        :return: The image of this ImageAttachment.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ImageAttachment.


        :param image: The image of this ImageAttachment.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_height(self):
        """Gets the image_height of this ImageAttachment.  # noqa: E501


        :return: The image_height of this ImageAttachment.  # noqa: E501
        :rtype: int
        """
        return self._image_height

    @image_height.setter
    def image_height(self, image_height):
        """Sets the image_height of this ImageAttachment.


        :param image_height: The image_height of this ImageAttachment.  # noqa: E501
        :type: int
        """
        if image_height is None:
            raise ValueError("Invalid value for `image_height`, must not be `None`")  # noqa: E501
        if image_height is not None and image_height > 32767:  # noqa: E501
            raise ValueError("Invalid value for `image_height`, must be a value less than or equal to `32767`")  # noqa: E501
        if image_height is not None and image_height < 0:  # noqa: E501
            raise ValueError("Invalid value for `image_height`, must be a value greater than or equal to `0`")  # noqa: E501

        self._image_height = image_height

    @property
    def image_width(self):
        """Gets the image_width of this ImageAttachment.  # noqa: E501


        :return: The image_width of this ImageAttachment.  # noqa: E501
        :rtype: int
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """Sets the image_width of this ImageAttachment.


        :param image_width: The image_width of this ImageAttachment.  # noqa: E501
        :type: int
        """
        if image_width is None:
            raise ValueError("Invalid value for `image_width`, must not be `None`")  # noqa: E501
        if image_width is not None and image_width > 32767:  # noqa: E501
            raise ValueError("Invalid value for `image_width`, must be a value less than or equal to `32767`")  # noqa: E501
        if image_width is not None and image_width < 0:  # noqa: E501
            raise ValueError("Invalid value for `image_width`, must be a value greater than or equal to `0`")  # noqa: E501

        self._image_width = image_width

    @property
    def created(self):
        """Gets the created of this ImageAttachment.  # noqa: E501


        :return: The created of this ImageAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ImageAttachment.


        :param created: The created of this ImageAttachment.  # noqa: E501
        :type: datetime
        """

        self._created = created

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
        if issubclass(ImageAttachment, dict):
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
        if not isinstance(other, ImageAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
