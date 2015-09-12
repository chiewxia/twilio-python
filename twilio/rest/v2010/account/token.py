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


class Token(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account that created this Token.
    
    .. attribute:: date_created
    
        The date that this resource was created, given in RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given in RFC 2822 format.
    
    .. attribute:: ice_servers
    
        An array representing the ephemeral credentials and the STUN and TURN
        server URIs.
    
    .. attribute:: password
    
        The temporary password that the username will use when authenticating
        with Twilio.
    
    .. attribute:: ttl
    
        The duration in seconds for which the username and password are valid,
        the default value is 86,400 (24 hours)
    
    .. attribute:: username
    
        The temporary username that uniquely identifies a Token.
    """
    id_key = "sid"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(Token, self).__init__(parent, None)

    def load(self, *args, **kwargs):
        super(Token, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)


class Tokens(ListResource):
    name = "Tokens"
    mount_name = "tokens"
    key = "tokens"
    instance = Token

    def __init__(self, *args, **kwargs):
        super(Tokens, self).__init__(*args, **kwargs)

    def create(self, **kwargs):
        """
        Create a new token
        
        :param str ttl: The duration in seconds for which the generated credentials are
            valid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Token`
        """
        return self.create_instance(kwargs)

    def load_instance(self, data):
        """ Override because Token does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
