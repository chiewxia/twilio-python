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


class IpAccessControlListMapping(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(IpAccessControlListMapping, self).load(*args, **kwargs)
        
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


class IpAccessControlListMappings(ListResource):
    name = "IpAccessControlListMappings"
    mount_name = "ip_access_control_list_mappings"
    key = "ip_access_control_list_mappings"
    instance = IpAccessControlListMapping

    def __init__(self, *args, **kwargs):
        super(IpAccessControlListMappings, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`IpAccessControlListMapping`
        :returns: A placeholder for a :class:`IpAccessControlListMapping` resource
        """
        return self.get_instance(sid)

    def create(self, ip_access_control_list_sid, **kwargs):
        """
        Create a new :class:`IpAccessControlListMapping`
        
        :param str ip_access_control_list_sid: The ip_access_control_list_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`IpAccessControlListMapping`
        """
        kwargs["IpAccessControlListSid"] = ip_access_control_list_sid
        return self.create_instance(kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`IpAccessControlListMapping`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`IpAccessControlListMapping`
        """
        return self.get_instances(kwargs)

    def delete(self, sid):
        """
        Delete the :class:`IpAccessControlListMapping`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`IpAccessControlListMapping` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`IpAccessControlListMapping`
        """
        return super(IpAccessControlListMappings, self).iter(**kwargs)
