# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose">
#   Copyright (c) 2018 Aspose.Slides for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

import pprint
import re  # noqa: F401

import six

from asposeslidescloud.models.math_element import MathElement

class PhantomElement(MathElement):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'base': 'MathElement',
        'show': 'bool',
        'zero_width': 'bool',
        'zero_asc': 'bool',
        'zero_desc': 'bool',
        'transp': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'base': 'base',
        'show': 'show',
        'zero_width': 'zeroWidth',
        'zero_asc': 'zeroAsc',
        'zero_desc': 'zeroDesc',
        'transp': 'transp'
    }

    type_determiners = {
        'type': 'Phantom',
    }

    def __init__(self, type='Phantom', base=None, show=None, zero_width=None, zero_asc=None, zero_desc=None, transp=None):  # noqa: E501
        """PhantomElement - a model defined in Swagger"""  # noqa: E501
        super(PhantomElement, self).__init__(type)

        self._base = None
        self._show = None
        self._zero_width = None
        self._zero_asc = None
        self._zero_desc = None
        self._transp = None
        self.type = 'Phantom'

        if base is not None:
            self.base = base
        if show is not None:
            self.show = show
        if zero_width is not None:
            self.zero_width = zero_width
        if zero_asc is not None:
            self.zero_asc = zero_asc
        if zero_desc is not None:
            self.zero_desc = zero_desc
        if transp is not None:
            self.transp = transp

    @property
    def base(self):
        """Gets the base of this PhantomElement.  # noqa: E501

        Base element  # noqa: E501

        :return: The base of this PhantomElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this PhantomElement.

        Base element  # noqa: E501

        :param base: The base of this PhantomElement.  # noqa: E501
        :type: MathElement
        """
        self._base = base

    @property
    def show(self):
        """Gets the show of this PhantomElement.  # noqa: E501

        true if the base element is displayed.  # noqa: E501

        :return: The show of this PhantomElement.  # noqa: E501
        :rtype: bool
        """
        return self._show

    @show.setter
    def show(self, show):
        """Sets the show of this PhantomElement.

        true if the base element is displayed.  # noqa: E501

        :param show: The show of this PhantomElement.  # noqa: E501
        :type: bool
        """
        self._show = show

    @property
    def zero_width(self):
        """Gets the zero_width of this PhantomElement.  # noqa: E501

        true if the the width of the base element should be treated as zero.  # noqa: E501

        :return: The zero_width of this PhantomElement.  # noqa: E501
        :rtype: bool
        """
        return self._zero_width

    @zero_width.setter
    def zero_width(self, zero_width):
        """Sets the zero_width of this PhantomElement.

        true if the the width of the base element should be treated as zero.  # noqa: E501

        :param zero_width: The zero_width of this PhantomElement.  # noqa: E501
        :type: bool
        """
        self._zero_width = zero_width

    @property
    def zero_asc(self):
        """Gets the zero_asc of this PhantomElement.  # noqa: E501

        true if the the ascent (height above baseline) of the base element should be treated as zero.  # noqa: E501

        :return: The zero_asc of this PhantomElement.  # noqa: E501
        :rtype: bool
        """
        return self._zero_asc

    @zero_asc.setter
    def zero_asc(self, zero_asc):
        """Sets the zero_asc of this PhantomElement.

        true if the the ascent (height above baseline) of the base element should be treated as zero.  # noqa: E501

        :param zero_asc: The zero_asc of this PhantomElement.  # noqa: E501
        :type: bool
        """
        self._zero_asc = zero_asc

    @property
    def zero_desc(self):
        """Gets the zero_desc of this PhantomElement.  # noqa: E501

        true if the the descent (depth below baseline) of the base element should be treated as zero.  # noqa: E501

        :return: The zero_desc of this PhantomElement.  # noqa: E501
        :rtype: bool
        """
        return self._zero_desc

    @zero_desc.setter
    def zero_desc(self, zero_desc):
        """Sets the zero_desc of this PhantomElement.

        true if the the descent (depth below baseline) of the base element should be treated as zero.  # noqa: E501

        :param zero_desc: The zero_desc of this PhantomElement.  # noqa: E501
        :type: bool
        """
        self._zero_desc = zero_desc

    @property
    def transp(self):
        """Gets the transp of this PhantomElement.  # noqa: E501

        true if operators and symbols inside the phantom still affect mathematical spacing around the phantom (as if visible).  # noqa: E501

        :return: The transp of this PhantomElement.  # noqa: E501
        :rtype: bool
        """
        return self._transp

    @transp.setter
    def transp(self, transp):
        """Sets the transp of this PhantomElement.

        true if operators and symbols inside the phantom still affect mathematical spacing around the phantom (as if visible).  # noqa: E501

        :param transp: The transp of this PhantomElement.  # noqa: E501
        :type: bool
        """
        self._transp = transp

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PhantomElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
