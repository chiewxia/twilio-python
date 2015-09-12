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


class Recording(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: call_sid
    
        The call_sid
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: duration
    
        The duration
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Recording, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Recordings(ListResource):
    name = "Recordings"
    mount_name = "recordings"
    key = "recordings"
    instance = Recording

    def __init__(self, *args, **kwargs):
        super(Recordings, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Recording`
        :returns: A placeholder for a :class:`Recording` resource
        """
        return self.get_instance(sid)

    def delete(self, sid):
        """
        Delete the :class:`Recording`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Recording`
        
        :param date date_created: The date_created
        :param date date_created_after: The date_created>
        :param date date_created_before: The date_created<
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Recording`
        """
        if "date_created_before" in kwargs:
            kwargs["DateCreated<"] = parse_date(kwargs["date_created_before"])
            del kwargs["date_created_before"]
        if "date_created_after" in kwargs:
            kwargs["DateCreated>"] = parse_date(kwargs["date_created_after"])
            del kwargs["date_created_after"]
        if "date_created" in kwargs:
            kwargs["DateCreated"] = parse_date(kwargs["date_created"])
            del kwargs["date_created"]
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Recording` using an iterator
        
        :param date date_created: The date_created
        :param date date_created_after: The date_created>
        :param date date_created_before: The date_created<
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Recording`
        """
        if "date_created_before" in kwargs:
            kwargs["DateCreated<"] = parse_date(kwargs["date_created_before"])
            del kwargs["date_created_before"]
        if "date_created_after" in kwargs:
            kwargs["DateCreated>"] = parse_date(kwargs["date_created_after"])
            del kwargs["date_created_after"]
        if "date_created" in kwargs:
            kwargs["DateCreated"] = parse_date(kwargs["date_created"])
            del kwargs["date_created"]
        return super(Recordings, self).iter(**kwargs)
