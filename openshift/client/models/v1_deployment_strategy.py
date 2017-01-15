# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v1.5.0-alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DeploymentStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active_deadline_seconds=None, annotations=None, custom_params=None, labels=None, recreate_params=None, resources=None, rolling_params=None, type=None):
        """
        V1DeploymentStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active_deadline_seconds': 'int',
            'annotations': 'dict(str, str)',
            'custom_params': 'V1CustomDeploymentStrategyParams',
            'labels': 'dict(str, str)',
            'recreate_params': 'V1RecreateDeploymentStrategyParams',
            'resources': 'V1ResourceRequirements',
            'rolling_params': 'V1RollingDeploymentStrategyParams',
            'type': 'str'
        }

        self.attribute_map = {
            'active_deadline_seconds': 'activeDeadlineSeconds',
            'annotations': 'annotations',
            'custom_params': 'customParams',
            'labels': 'labels',
            'recreate_params': 'recreateParams',
            'resources': 'resources',
            'rolling_params': 'rollingParams',
            'type': 'type'
        }

        self._active_deadline_seconds = active_deadline_seconds
        self._annotations = annotations
        self._custom_params = custom_params
        self._labels = labels
        self._recreate_params = recreate_params
        self._resources = resources
        self._rolling_params = rolling_params
        self._type = type

    @property
    def active_deadline_seconds(self):
        """
        Gets the active_deadline_seconds of this V1DeploymentStrategy.
        ActiveDeadlineSeconds is the duration in seconds that the deployer pods for this deployment config may be active on a node before the system actively tries to terminate them.

        :return: The active_deadline_seconds of this V1DeploymentStrategy.
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """
        Sets the active_deadline_seconds of this V1DeploymentStrategy.
        ActiveDeadlineSeconds is the duration in seconds that the deployer pods for this deployment config may be active on a node before the system actively tries to terminate them.

        :param active_deadline_seconds: The active_deadline_seconds of this V1DeploymentStrategy.
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def annotations(self):
        """
        Gets the annotations of this V1DeploymentStrategy.
        Annotations is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods.

        :return: The annotations of this V1DeploymentStrategy.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this V1DeploymentStrategy.
        Annotations is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods.

        :param annotations: The annotations of this V1DeploymentStrategy.
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def custom_params(self):
        """
        Gets the custom_params of this V1DeploymentStrategy.
        CustomParams are the input to the Custom deployment strategy, and may also be specified for the Recreate and Rolling strategies to customize the execution process that runs the deployment.

        :return: The custom_params of this V1DeploymentStrategy.
        :rtype: V1CustomDeploymentStrategyParams
        """
        return self._custom_params

    @custom_params.setter
    def custom_params(self, custom_params):
        """
        Sets the custom_params of this V1DeploymentStrategy.
        CustomParams are the input to the Custom deployment strategy, and may also be specified for the Recreate and Rolling strategies to customize the execution process that runs the deployment.

        :param custom_params: The custom_params of this V1DeploymentStrategy.
        :type: V1CustomDeploymentStrategyParams
        """

        self._custom_params = custom_params

    @property
    def labels(self):
        """
        Gets the labels of this V1DeploymentStrategy.
        Labels is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods.

        :return: The labels of this V1DeploymentStrategy.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this V1DeploymentStrategy.
        Labels is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods.

        :param labels: The labels of this V1DeploymentStrategy.
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def recreate_params(self):
        """
        Gets the recreate_params of this V1DeploymentStrategy.
        RecreateParams are the input to the Recreate deployment strategy.

        :return: The recreate_params of this V1DeploymentStrategy.
        :rtype: V1RecreateDeploymentStrategyParams
        """
        return self._recreate_params

    @recreate_params.setter
    def recreate_params(self, recreate_params):
        """
        Sets the recreate_params of this V1DeploymentStrategy.
        RecreateParams are the input to the Recreate deployment strategy.

        :param recreate_params: The recreate_params of this V1DeploymentStrategy.
        :type: V1RecreateDeploymentStrategyParams
        """

        self._recreate_params = recreate_params

    @property
    def resources(self):
        """
        Gets the resources of this V1DeploymentStrategy.
        Resources contains resource requirements to execute the deployment and any hooks.

        :return: The resources of this V1DeploymentStrategy.
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1DeploymentStrategy.
        Resources contains resource requirements to execute the deployment and any hooks.

        :param resources: The resources of this V1DeploymentStrategy.
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def rolling_params(self):
        """
        Gets the rolling_params of this V1DeploymentStrategy.
        RollingParams are the input to the Rolling deployment strategy.

        :return: The rolling_params of this V1DeploymentStrategy.
        :rtype: V1RollingDeploymentStrategyParams
        """
        return self._rolling_params

    @rolling_params.setter
    def rolling_params(self, rolling_params):
        """
        Sets the rolling_params of this V1DeploymentStrategy.
        RollingParams are the input to the Rolling deployment strategy.

        :param rolling_params: The rolling_params of this V1DeploymentStrategy.
        :type: V1RollingDeploymentStrategyParams
        """

        self._rolling_params = rolling_params

    @property
    def type(self):
        """
        Gets the type of this V1DeploymentStrategy.
        Type is the name of a deployment strategy.

        :return: The type of this V1DeploymentStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1DeploymentStrategy.
        Type is the name of a deployment strategy.

        :param type: The type of this V1DeploymentStrategy.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
