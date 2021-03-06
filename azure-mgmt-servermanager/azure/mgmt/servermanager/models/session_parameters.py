# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SessionParameters(Model):
    """SessionParameters.

    :param user_name: User name to be used to connect to node
    :type user_name: str
    :param password: Password associated with user name
    :type password: str
    """ 

    _attribute_map = {
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
    }

    def __init__(self, user_name=None, password=None):
        self.user_name = user_name
        self.password = password
