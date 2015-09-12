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


class Notification(InstanceResource):
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
    
    .. attribute:: error_code
    
        The error_code
    
    .. attribute:: log
    
        The log
    
    .. attribute:: message_date
    
        The message_date
    
    .. attribute:: message_text
    
        The message_text
    
    .. attribute:: more_info
    
        The more_info
    
    .. attribute:: request_method
    
        The request_method
    
    .. attribute:: request_url
    
        The request_url
    
    .. attribute:: request_variables
    
        The request_variables
    
    .. attribute:: response_body
    
        The response_body
    
    .. attribute:: response_headers
    
        The response_headers
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Notification, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)
        
        if hasattr(self, "message_date") and self.message_date:
            self.message_date = parse_iso_date(self.message_date)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Notifications(ListResource):
    name = "Notifications"
    mount_name = "notifications"
    key = "notifications"
    instance = Notification

    def __init__(self, *args, **kwargs):
        super(Notifications, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Notification`
        :returns: A placeholder for a :class:`Notification` resource
        """
        return self.get_instance(sid)

    def delete(self, sid):
        """
        Delete the :class:`Notification`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Notification`
        
        :param date message_date: The message_date
        :param date message_date_after: The message_date>
        :param date message_date_before: The message_date<
        :param str log: The log
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Notification`
        """
        if "message_date_before" in kwargs:
            kwargs["MessageDate<"] = parse_date(kwargs["message_date_before"])
            del kwargs["message_date_before"]
        if "message_date_after" in kwargs:
            kwargs["MessageDate>"] = parse_date(kwargs["message_date_after"])
            del kwargs["message_date_after"]
        if "message_date" in kwargs:
            kwargs["MessageDate"] = parse_date(kwargs["message_date"])
            del kwargs["message_date"]
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Notification` using an iterator
        
        :param date message_date: The message_date
        :param date message_date_after: The message_date>
        :param date message_date_before: The message_date<
        :param str log: The log
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Notification`
        """
        if "message_date_before" in kwargs:
            kwargs["MessageDate<"] = parse_date(kwargs["message_date_before"])
            del kwargs["message_date_before"]
        if "message_date_after" in kwargs:
            kwargs["MessageDate>"] = parse_date(kwargs["message_date_after"])
            del kwargs["message_date_after"]
        if "message_date" in kwargs:
            kwargs["MessageDate"] = parse_date(kwargs["message_date"])
            del kwargs["message_date"]
        return super(Notifications, self).iter(**kwargs)
