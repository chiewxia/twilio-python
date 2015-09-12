# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource


class AuthorizedConnectApp(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the SubAccount this Connect App has access to.
    
    .. attribute:: connect_app_company_name
    
        The company name set for this Connect App.
    
    .. attribute:: connect_app_description
    
        A more detailed human readable description of the Connect App.
    
    .. attribute:: connect_app_friendly_name
    
        A human readable name for the Connect App.
    
    .. attribute:: connect_app_homepage_url
    
        The public URL for this Connect App.
    
    .. attribute:: connect_app_sid
    
        The unique id of the Connect App that was authorized.
    
    .. attribute:: date_created
    
        The date that this resource was created, given as GMT RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given as GMT RFC 2822
        format.
    
    .. attribute:: permissions
    
        The set of permissions that you have authorized for this Connect App. 
        Valid permisisons are `get-all` or `post-all`.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`.
    """
    id_key = "connect_app_sid"
    GET_ALL = "get-all"
    POST_ALL = "post-all"

    def load(self, *args, **kwargs):
        super(AuthorizedConnectApp, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)


class AuthorizedConnectApps(ListResource):
    name = "AuthorizedConnectApps"
    mount_name = "authorized_connect_apps"
    key = "authorized_connect_apps"
    instance = AuthorizedConnectApp

    def __init__(self, *args, **kwargs):
        super(AuthorizedConnectApps, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch an instance of an authorized-connect-app
        
        :param str sid: The authorized-connect-app Sid that uniquely identifies this
            resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`AuthorizedConnectApp`
        :returns: A placeholder for a :class:`AuthorizedConnectApp` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of authorized-connect-apps belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`AuthorizedConnectApp`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of authorized-connect-apps belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`AuthorizedConnectApp`
        """
        return super(AuthorizedConnectApps, self).iter(**kwargs)
