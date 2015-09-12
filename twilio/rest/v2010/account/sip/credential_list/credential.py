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


class Credential(InstanceResource):
    """
    .. attribute:: sid
    
        The sid
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: credential_list_sid
    
        The credential_list_sid
    
    .. attribute:: username
    
        The username
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Credential, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str password: The password
        :param str username: The username
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Credential`
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


class Credentials(ListResource):
    name = "Credentials"
    mount_name = "credentials"
    key = "credentials"
    instance = Credential

    def __init__(self, *args, **kwargs):
        super(Credentials, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Credential`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Credential`
        """
        return self.get_instances(kwargs)

    def create(self, username, password, **kwargs):
        """
        Create a new :class:`Credential`
        
        :param str password: The password
        :param str username: The username
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Credential`
        """
        kwargs["Username"] = username
        kwargs["Password"] = password
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Credential`
        :returns: A placeholder for a :class:`Credential` resource
        """
        return self.get_instance(sid)

    def update(self, sid, username, password, **kwargs):
        """
        Update a :class:`Credential`
        
        :param str password: The password
        :param str sid: The sid
        :param str username: The username
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Credential`
        """
        kwargs["Username"] = username
        kwargs["Password"] = password
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Credential`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Credential` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Credential`
        """
        return super(Credentials, self).iter(**kwargs)
