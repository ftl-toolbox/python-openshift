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


class V1Container(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, args=None, command=None, env=None, image=None, image_pull_policy=None, lifecycle=None, liveness_probe=None, name=None, ports=None, readiness_probe=None, resources=None, security_context=None, stdin=None, stdin_once=None, termination_message_path=None, tty=None, volume_mounts=None, working_dir=None):
        """
        V1Container - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'args': 'list[str]',
            'command': 'list[str]',
            'env': 'list[V1EnvVar]',
            'image': 'str',
            'image_pull_policy': 'str',
            'lifecycle': 'V1Lifecycle',
            'liveness_probe': 'V1Probe',
            'name': 'str',
            'ports': 'list[V1ContainerPort]',
            'readiness_probe': 'V1Probe',
            'resources': 'V1ResourceRequirements',
            'security_context': 'V1SecurityContext',
            'stdin': 'bool',
            'stdin_once': 'bool',
            'termination_message_path': 'str',
            'tty': 'bool',
            'volume_mounts': 'list[V1VolumeMount]',
            'working_dir': 'str'
        }

        self.attribute_map = {
            'args': 'args',
            'command': 'command',
            'env': 'env',
            'image': 'image',
            'image_pull_policy': 'imagePullPolicy',
            'lifecycle': 'lifecycle',
            'liveness_probe': 'livenessProbe',
            'name': 'name',
            'ports': 'ports',
            'readiness_probe': 'readinessProbe',
            'resources': 'resources',
            'security_context': 'securityContext',
            'stdin': 'stdin',
            'stdin_once': 'stdinOnce',
            'termination_message_path': 'terminationMessagePath',
            'tty': 'tty',
            'volume_mounts': 'volumeMounts',
            'working_dir': 'workingDir'
        }

        self._args = args
        self._command = command
        self._env = env
        self._image = image
        self._image_pull_policy = image_pull_policy
        self._lifecycle = lifecycle
        self._liveness_probe = liveness_probe
        self._name = name
        self._ports = ports
        self._readiness_probe = readiness_probe
        self._resources = resources
        self._security_context = security_context
        self._stdin = stdin
        self._stdin_once = stdin_once
        self._termination_message_path = termination_message_path
        self._tty = tty
        self._volume_mounts = volume_mounts
        self._working_dir = working_dir

    @property
    def args(self):
        """
        Gets the args of this V1Container.
        Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/containers#containers-and-commands

        :return: The args of this V1Container.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """
        Sets the args of this V1Container.
        Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/containers#containers-and-commands

        :param args: The args of this V1Container.
        :type: list[str]
        """

        self._args = args

    @property
    def command(self):
        """
        Gets the command of this V1Container.
        Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/containers#containers-and-commands

        :return: The command of this V1Container.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this V1Container.
        Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/containers#containers-and-commands

        :param command: The command of this V1Container.
        :type: list[str]
        """

        self._command = command

    @property
    def env(self):
        """
        Gets the env of this V1Container.
        List of environment variables to set in the container. Cannot be updated.

        :return: The env of this V1Container.
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this V1Container.
        List of environment variables to set in the container. Cannot be updated.

        :param env: The env of this V1Container.
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def image(self):
        """
        Gets the image of this V1Container.
        Docker image name. More info: http://kubernetes.io/docs/user-guide/images

        :return: The image of this V1Container.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1Container.
        Docker image name. More info: http://kubernetes.io/docs/user-guide/images

        :param image: The image of this V1Container.
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """
        Gets the image_pull_policy of this V1Container.
        Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/images#updating-images

        :return: The image_pull_policy of this V1Container.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """
        Sets the image_pull_policy of this V1Container.
        Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/images#updating-images

        :param image_pull_policy: The image_pull_policy of this V1Container.
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def lifecycle(self):
        """
        Gets the lifecycle of this V1Container.
        Actions that the management system should take in response to container lifecycle events. Cannot be updated.

        :return: The lifecycle of this V1Container.
        :rtype: V1Lifecycle
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """
        Sets the lifecycle of this V1Container.
        Actions that the management system should take in response to container lifecycle events. Cannot be updated.

        :param lifecycle: The lifecycle of this V1Container.
        :type: V1Lifecycle
        """

        self._lifecycle = lifecycle

    @property
    def liveness_probe(self):
        """
        Gets the liveness_probe of this V1Container.
        Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :return: The liveness_probe of this V1Container.
        :rtype: V1Probe
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """
        Sets the liveness_probe of this V1Container.
        Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :param liveness_probe: The liveness_probe of this V1Container.
        :type: V1Probe
        """

        self._liveness_probe = liveness_probe

    @property
    def name(self):
        """
        Gets the name of this V1Container.
        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.

        :return: The name of this V1Container.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Container.
        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.

        :param name: The name of this V1Container.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def ports(self):
        """
        Gets the ports of this V1Container.
        List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.

        :return: The ports of this V1Container.
        :rtype: list[V1ContainerPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1Container.
        List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.

        :param ports: The ports of this V1Container.
        :type: list[V1ContainerPort]
        """

        self._ports = ports

    @property
    def readiness_probe(self):
        """
        Gets the readiness_probe of this V1Container.
        Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :return: The readiness_probe of this V1Container.
        :rtype: V1Probe
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """
        Sets the readiness_probe of this V1Container.
        Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :param readiness_probe: The readiness_probe of this V1Container.
        :type: V1Probe
        """

        self._readiness_probe = readiness_probe

    @property
    def resources(self):
        """
        Gets the resources of this V1Container.
        Compute Resources required by this container. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#resources

        :return: The resources of this V1Container.
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1Container.
        Compute Resources required by this container. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#resources

        :param resources: The resources of this V1Container.
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def security_context(self):
        """
        Gets the security_context of this V1Container.
        Security options the pod should run with. More info: http://releases.k8s.io/HEAD/docs/design/security_context.md

        :return: The security_context of this V1Container.
        :rtype: V1SecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """
        Sets the security_context of this V1Container.
        Security options the pod should run with. More info: http://releases.k8s.io/HEAD/docs/design/security_context.md

        :param security_context: The security_context of this V1Container.
        :type: V1SecurityContext
        """

        self._security_context = security_context

    @property
    def stdin(self):
        """
        Gets the stdin of this V1Container.
        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.

        :return: The stdin of this V1Container.
        :rtype: bool
        """
        return self._stdin

    @stdin.setter
    def stdin(self, stdin):
        """
        Sets the stdin of this V1Container.
        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.

        :param stdin: The stdin of this V1Container.
        :type: bool
        """

        self._stdin = stdin

    @property
    def stdin_once(self):
        """
        Gets the stdin_once of this V1Container.
        Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false

        :return: The stdin_once of this V1Container.
        :rtype: bool
        """
        return self._stdin_once

    @stdin_once.setter
    def stdin_once(self, stdin_once):
        """
        Sets the stdin_once of this V1Container.
        Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false

        :param stdin_once: The stdin_once of this V1Container.
        :type: bool
        """

        self._stdin_once = stdin_once

    @property
    def termination_message_path(self):
        """
        Gets the termination_message_path of this V1Container.
        Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Defaults to /dev/termination-log. Cannot be updated.

        :return: The termination_message_path of this V1Container.
        :rtype: str
        """
        return self._termination_message_path

    @termination_message_path.setter
    def termination_message_path(self, termination_message_path):
        """
        Sets the termination_message_path of this V1Container.
        Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Defaults to /dev/termination-log. Cannot be updated.

        :param termination_message_path: The termination_message_path of this V1Container.
        :type: str
        """

        self._termination_message_path = termination_message_path

    @property
    def tty(self):
        """
        Gets the tty of this V1Container.
        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.

        :return: The tty of this V1Container.
        :rtype: bool
        """
        return self._tty

    @tty.setter
    def tty(self, tty):
        """
        Sets the tty of this V1Container.
        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.

        :param tty: The tty of this V1Container.
        :type: bool
        """

        self._tty = tty

    @property
    def volume_mounts(self):
        """
        Gets the volume_mounts of this V1Container.
        Pod volumes to mount into the container's filesystem. Cannot be updated.

        :return: The volume_mounts of this V1Container.
        :rtype: list[V1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """
        Sets the volume_mounts of this V1Container.
        Pod volumes to mount into the container's filesystem. Cannot be updated.

        :param volume_mounts: The volume_mounts of this V1Container.
        :type: list[V1VolumeMount]
        """

        self._volume_mounts = volume_mounts

    @property
    def working_dir(self):
        """
        Gets the working_dir of this V1Container.
        Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.

        :return: The working_dir of this V1Container.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """
        Sets the working_dir of this V1Container.
        Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.

        :param working_dir: The working_dir of this V1Container.
        :type: str
        """

        self._working_dir = working_dir

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
