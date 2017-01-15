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


class V1OAuthAuthorizeToken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, client_name=None, code_challenge=None, code_challenge_method=None, expires_in=None, metadata=None, redirect_uri=None, scopes=None, state=None, user_name=None, user_uid=None):
        """
        V1OAuthAuthorizeToken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client_name': 'str',
            'code_challenge': 'str',
            'code_challenge_method': 'str',
            'expires_in': 'int',
            'metadata': 'V1ObjectMeta',
            'redirect_uri': 'str',
            'scopes': 'list[str]',
            'state': 'str',
            'user_name': 'str',
            'user_uid': 'str'
        }

        self.attribute_map = {
            'client_name': 'clientName',
            'code_challenge': 'codeChallenge',
            'code_challenge_method': 'codeChallengeMethod',
            'expires_in': 'expiresIn',
            'metadata': 'metadata',
            'redirect_uri': 'redirectURI',
            'scopes': 'scopes',
            'state': 'state',
            'user_name': 'userName',
            'user_uid': 'userUID'
        }

        self._client_name = client_name
        self._code_challenge = code_challenge
        self._code_challenge_method = code_challenge_method
        self._expires_in = expires_in
        self._metadata = metadata
        self._redirect_uri = redirect_uri
        self._scopes = scopes
        self._state = state
        self._user_name = user_name
        self._user_uid = user_uid

    @property
    def client_name(self):
        """
        Gets the client_name of this V1OAuthAuthorizeToken.
        ClientName references the client that created this token.

        :return: The client_name of this V1OAuthAuthorizeToken.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """
        Sets the client_name of this V1OAuthAuthorizeToken.
        ClientName references the client that created this token.

        :param client_name: The client_name of this V1OAuthAuthorizeToken.
        :type: str
        """

        self._client_name = client_name

    @property
    def code_challenge(self):
        """
        Gets the code_challenge of this V1OAuthAuthorizeToken.
        CodeChallenge is the optional code_challenge associated with this authorization code, as described in rfc7636

        :return: The code_challenge of this V1OAuthAuthorizeToken.
        :rtype: str
        """
        return self._code_challenge

    @code_challenge.setter
    def code_challenge(self, code_challenge):
        """
        Sets the code_challenge of this V1OAuthAuthorizeToken.
        CodeChallenge is the optional code_challenge associated with this authorization code, as described in rfc7636

        :param code_challenge: The code_challenge of this V1OAuthAuthorizeToken.
        :type: str
        """

        self._code_challenge = code_challenge

    @property
    def code_challenge_method(self):
        """
        Gets the code_challenge_method of this V1OAuthAuthorizeToken.
        CodeChallengeMethod is the optional code_challenge_method associated with this authorization code, as described in rfc7636

        :return: The code_challenge_method of this V1OAuthAuthorizeToken.
        :rtype: str
        """
        return self._code_challenge_method

    @code_challenge_method.setter
    def code_challenge_method(self, code_challenge_method):
        """
        Sets the code_challenge_method of this V1OAuthAuthorizeToken.
        CodeChallengeMethod is the optional code_challenge_method associated with this authorization code, as described in rfc7636

        :param code_challenge_method: The code_challenge_method of this V1OAuthAuthorizeToken.
        :type: str
        """

        self._code_challenge_method = code_challenge_method

    @property
    def expires_in(self):
        """
        Gets the expires_in of this V1OAuthAuthorizeToken.
        ExpiresIn is the seconds from CreationTime before this token expires.

        :return: The expires_in of this V1OAuthAuthorizeToken.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this V1OAuthAuthorizeToken.
        ExpiresIn is the seconds from CreationTime before this token expires.

        :param expires_in: The expires_in of this V1OAuthAuthorizeToken.
        :type: int
        """

        self._expires_in = expires_in

    @property
    def metadata(self):
        """
        Gets the metadata of this V1OAuthAuthorizeToken.
        Standard object's metadata.

        :return: The metadata of this V1OAuthAuthorizeToken.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1OAuthAuthorizeToken.
        Standard object's metadata.

        :param metadata: The metadata of this V1OAuthAuthorizeToken.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def redirect_uri(self):
        """
        Gets the redirect_uri of this V1OAuthAuthorizeToken.
        RedirectURI is the redirection associated with the token.

        :return: The redirect_uri of this V1OAuthAuthorizeToken.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """
        Sets the redirect_uri of this V1OAuthAuthorizeToken.
        RedirectURI is the redirection associated with the token.

        :param redirect_uri: The redirect_uri of this V1OAuthAuthorizeToken.
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def scopes(self):
        """
        Gets the scopes of this V1OAuthAuthorizeToken.
        Scopes is an array of the requested scopes.

        :return: The scopes of this V1OAuthAuthorizeToken.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this V1OAuthAuthorizeToken.
        Scopes is an array of the requested scopes.

        :param scopes: The scopes of this V1OAuthAuthorizeToken.
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def state(self):
        """
        Gets the state of this V1OAuthAuthorizeToken.
        State data from request

        :return: The state of this V1OAuthAuthorizeToken.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this V1OAuthAuthorizeToken.
        State data from request

        :param state: The state of this V1OAuthAuthorizeToken.
        :type: str
        """

        self._state = state

    @property
    def user_name(self):
        """
        Gets the user_name of this V1OAuthAuthorizeToken.
        UserName is the user name associated with this token

        :return: The user_name of this V1OAuthAuthorizeToken.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this V1OAuthAuthorizeToken.
        UserName is the user name associated with this token

        :param user_name: The user_name of this V1OAuthAuthorizeToken.
        :type: str
        """

        self._user_name = user_name

    @property
    def user_uid(self):
        """
        Gets the user_uid of this V1OAuthAuthorizeToken.
        UserUID is the unique UID associated with this token. UserUID and UserName must both match for this token to be valid.

        :return: The user_uid of this V1OAuthAuthorizeToken.
        :rtype: str
        """
        return self._user_uid

    @user_uid.setter
    def user_uid(self, user_uid):
        """
        Sets the user_uid of this V1OAuthAuthorizeToken.
        UserUID is the unique UID associated with this token. UserUID and UserName must both match for this token to be valid.

        :param user_uid: The user_uid of this V1OAuthAuthorizeToken.
        :type: str
        """

        self._user_uid = user_uid

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
