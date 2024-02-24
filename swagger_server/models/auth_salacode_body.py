# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AuthSalacodeBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: str=None):  # noqa: E501
        """AuthSalacodeBody - a model defined in Swagger

        :param code: The code of this AuthSalacodeBody.  # noqa: E501
        :type code: str
        """
        self.swagger_types = {
            'code': str
        }

        self.attribute_map = {
            'code': 'code'
        }
        self._code = code

    @classmethod
    def from_dict(cls, dikt) -> 'AuthSalacodeBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The auth_salacode_body of this AuthSalacodeBody.  # noqa: E501
        :rtype: AuthSalacodeBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this AuthSalacodeBody.


        :return: The code of this AuthSalacodeBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this AuthSalacodeBody.


        :param code: The code of this AuthSalacodeBody.
        :type code: str
        """

        self._code = code