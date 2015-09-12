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


class Activity(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: available
    
        The available
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Activity, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Activity`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Activities(NextGenListResource):
    name = "Activities"
    mount_name = "activities"
    key = "activities"
    instance = Activity

    def __init__(self, *args, **kwargs):
        super(Activities, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Activity`
        :returns: A placeholder for a :class:`Activity` resource
        """
        return self.get_instance(sid)

    def update(self, sid, friendly_name, **kwargs):
        """
        Update a :class:`Activity`
        
        :param str friendly_name: The friendly_name
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Activity`
        """
        kwargs["FriendlyName"] = friendly_name
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Activity`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Activity`
        
        :param str available: The available
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Activity`
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, available, **kwargs):
        """
        Create a new :class:`Activity`
        
        :param bool available: The available
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Activity`
        """
        kwargs["FriendlyName"] = friendly_name
        kwargs["Available"] = available
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Activity` using an iterator
        
        :param str available: The available
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Activity`
        """
        return super(Activities, self).iter(**kwargs)
