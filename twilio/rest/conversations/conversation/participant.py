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
from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.resources.base import NextGenListResource


class Participant(NextGenInstanceResource):
    """
    .. attribute:: sid
    
        The sid
    
    .. attribute:: address
    
        The address
    
    .. attribute:: status
    
        The status
    
    .. attribute:: conversation_sid
    
        The conversation_sid
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: start_time
    
        The start_time
    
    .. attribute:: end_time
    
        The end_time
    
    .. attribute:: duration
    
        The duration
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: url
    
        The url
    """
    id_key = "sid"
    CONNECTED = "connected"
    CONNECTING = "connecting"
    CREATED = "created"
    DISCONNECTED = "disconnected"
    FAILED = "failed"

    def load(self, *args, **kwargs):
        super(Participant, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "start_time") and self.start_time:
            self.start_time = parse_iso_date(self.start_time)
        
        if hasattr(self, "end_time") and self.end_time:
            self.end_time = parse_iso_date(self.end_time)


class Participants(NextGenListResource):
    name = "Participants"
    mount_name = "participants"
    key = "participants"
    instance = Participant

    def __init__(self, *args, **kwargs):
        super(Participants, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Participant`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Participant`
        """
        return self.get_instances(kwargs)

    def create(self, to, from_, **kwargs):
        """
        Create a new :class:`Participant`
        
        :param str from_: The from
        :param str to: The to
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Participant`
        """
        kwargs["To"] = to
        kwargs["From"] = from_
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Participant`
        :returns: A placeholder for a :class:`Participant` resource
        """
        return self.get_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Participant` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Participant`
        """
        return super(Participants, self).iter(**kwargs)
