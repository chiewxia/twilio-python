# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource


class ConnectApp(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account that created this ConnectApp.
    
    .. attribute:: authorize_redirect_url
    
        The URL the user's browser will redirect to after Twilio authenticates
        the user and obtains authorization for this Connect App.
    
    .. attribute:: company_name
    
        The company name set for this Connect App.
    
    .. attribute:: deauthorize_callback_method
    
        The HTTP method to be used when making a request to the
        `DeauthorizeCallbackUrl`.
    
    .. attribute:: deauthorize_callback_url
    
        The URL to which Twilio will send a request when a user de-authorizes
        this Connect App.
    
    .. attribute:: description
    
        A more detailed human readable description of the Connect App.
    
    .. attribute:: friendly_name
    
        A human readable name for the Connect App.
    
    .. attribute:: homepage_url
    
        The public URL where users can obtain more information about this
        Connect App.
    
    .. attribute:: permissions
    
        The set of permissions that your ConnectApp requests.
    
    .. attribute:: sid
    
        The unique id of this Connect App.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`.
    """
    id_key = "sid"
    GET_ALL = "get-all"
    POST_ALL = "post-all"

    def update(self, **kwargs):
        """
        Update a connect-app with the specified parameters
        
        :param connect_app.permission permissions: The set of permissions that your
            ConnectApp requests.
        :param str authorize_redirect_url: The URL the user's browser will redirect to
            after Twilio authenticates the user and obtains authorization for this Connect
            App.
        :param str company_name: The company name set for this Connect App.
        :param str deauthorize_callback_method: The HTTP method to be used when making a
            request to the `DeauthorizeCallbackUrl`.
        :param str deauthorize_callback_url: The URL to which Twilio will send a request
            when a user de-authorizes this Connect App.
        :param str description: A more detailed human readable description of the
            Connect App.
        :param str friendly_name: A human readable name for the Connect App.
        :param str homepage_url: The public URL where users can obtain more information
            about this Connect App.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`ConnectApp`
        """
        return self.update_instance(kwargs)


class ConnectApps(ListResource):
    name = "ConnectApps"
    mount_name = "connect_apps"
    key = "connect_apps"
    instance = ConnectApp

    def __init__(self, *args, **kwargs):
        super(ConnectApps, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch an instance of a connect-app
        
        :param str sid: The connect-app Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ConnectApp`
        :returns: A placeholder for a :class:`ConnectApp` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a connect-app with the specified parameters
        
        :param connect_app.permission permissions: The set of permissions that your
            ConnectApp requests.
        :param str authorize_redirect_url: The URL the user's browser will redirect to
            after Twilio authenticates the user and obtains authorization for this Connect
            App.
        :param str company_name: The company name set for this Connect App.
        :param str deauthorize_callback_method: The HTTP method to be used when making a
            request to the `DeauthorizeCallbackUrl`.
        :param str deauthorize_callback_url: The URL to which Twilio will send a request
            when a user de-authorizes this Connect App.
        :param str description: A more detailed human readable description of the
            Connect App.
        :param str friendly_name: A human readable name for the Connect App.
        :param str homepage_url: The public URL where users can obtain more information
            about this Connect App.
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`ConnectApp`
        """
        return self.update_instance(sid, kwargs)

    def list(self, **kwargs):
        """
        Retrieve a list of connect-apps belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`ConnectApp`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of connect-apps belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`ConnectApp`
        """
        return super(ConnectApps, self).iter(**kwargs)
