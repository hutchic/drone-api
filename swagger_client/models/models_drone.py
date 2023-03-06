# coding: utf-8

"""
    Drones Test Exercise API

    This is a sample API for renting time on a drones-as-a-service platform.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: info@superorbital.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ModelsDrone(object):
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
        'cost': 'ModelsDroneCost',
        'id': 'str',
        'instruction_index': 'int',
        'name': 'str',
        'plan': 'list[str]',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'cost': 'cost',
        'id': 'id',
        'instruction_index': 'instructionIndex',
        'name': 'name',
        'plan': 'plan',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, cost=None, id=None, instruction_index=None, name=None, plan=None, status=None, type=None):  # noqa: E501
        """ModelsDrone - a model defined in Swagger"""  # noqa: E501
        self._cost = None
        self._id = None
        self._instruction_index = None
        self._name = None
        self._plan = None
        self._status = None
        self._type = None
        self.discriminator = None
        if cost is not None:
            self.cost = cost
        if id is not None:
            self.id = id
        self.instruction_index = instruction_index
        self.name = name
        if plan is not None:
            self.plan = plan
        if status is not None:
            self.status = status
        self.type = type

    @property
    def cost(self):
        """Gets the cost of this ModelsDrone.  # noqa: E501


        :return: The cost of this ModelsDrone.  # noqa: E501
        :rtype: ModelsDroneCost
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ModelsDrone.


        :param cost: The cost of this ModelsDrone.  # noqa: E501
        :type: ModelsDroneCost
        """

        self._cost = cost

    @property
    def id(self):
        """Gets the id of this ModelsDrone.  # noqa: E501


        :return: The id of this ModelsDrone.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsDrone.


        :param id: The id of this ModelsDrone.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instruction_index(self):
        """Gets the instruction_index of this ModelsDrone.  # noqa: E501

        InstructionIndex provides a numeric index into the current instruction of the drone's plan that is being executed.  # noqa: E501

        :return: The instruction_index of this ModelsDrone.  # noqa: E501
        :rtype: int
        """
        return self._instruction_index

    @instruction_index.setter
    def instruction_index(self, instruction_index):
        """Sets the instruction_index of this ModelsDrone.

        InstructionIndex provides a numeric index into the current instruction of the drone's plan that is being executed.  # noqa: E501

        :param instruction_index: The instruction_index of this ModelsDrone.  # noqa: E501
        :type: int
        """
        if instruction_index is None:
            raise ValueError("Invalid value for `instruction_index`, must not be `None`")  # noqa: E501

        self._instruction_index = instruction_index

    @property
    def name(self):
        """Gets the name of this ModelsDrone.  # noqa: E501

        Name of the drone. For your purposes.  # noqa: E501

        :return: The name of this ModelsDrone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsDrone.

        Name of the drone. For your purposes.  # noqa: E501

        :param name: The name of this ModelsDrone.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def plan(self):
        """Gets the plan of this ModelsDrone.  # noqa: E501

        Plan for drone to fly. Must be at least one instruction long and the last instruction must be a landing command.  # noqa: E501

        :return: The plan of this ModelsDrone.  # noqa: E501
        :rtype: list[str]
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this ModelsDrone.

        Plan for drone to fly. Must be at least one instruction long and the last instruction must be a landing command.  # noqa: E501

        :param plan: The plan of this ModelsDrone.  # noqa: E501
        :type: list[str]
        """

        self._plan = plan

    @property
    def status(self):
        """Gets the status of this ModelsDrone.  # noqa: E501

        Status of the drone. Must be one of: at-home, starting-up, en-route, landing, missing  # noqa: E501

        :return: The status of this ModelsDrone.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelsDrone.

        Status of the drone. Must be one of: at-home, starting-up, en-route, landing, missing  # noqa: E501

        :param status: The status of this ModelsDrone.  # noqa: E501
        :type: str
        """
        allowed_values = ["at-home", "starting-up", "en-route", "landing", "missing"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this ModelsDrone.  # noqa: E501

        Type of drone. Must be one of: quadcopter-small, quadcopter-large, plane-small, single-rotor-large  # noqa: E501

        :return: The type of this ModelsDrone.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelsDrone.

        Type of drone. Must be one of: quadcopter-small, quadcopter-large, plane-small, single-rotor-large  # noqa: E501

        :param type: The type of this ModelsDrone.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["quadcopter-small", "quadcopter-large", "plane-small", "single-rotor-large"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ModelsDrone, dict):
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
        if not isinstance(other, ModelsDrone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
