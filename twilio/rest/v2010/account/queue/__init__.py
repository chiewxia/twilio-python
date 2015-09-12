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
from twilio.rest.v2010.account.queue.member import (
    Member,
    Members,
)
from twilio.rest.resources.base import ListResource


class Queue(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: average_wait_time
    
         The average wait time of the members of this queue in seconds. This is
         calculated at the time of the request. 
    
    .. attribute:: current_size
    
        The count of calls currently in the queue.
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: friendly_name
    
        A user-provided string that identifies this queue.
    
    .. attribute:: max_size
    
         The upper limit of calls allowed to be in the queue. The default is
         100. The maximum is 1000.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this queue.
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"
    subresources = [
        Members
    ]

    def load(self, *args, **kwargs):
        super(Queue, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the queue with the new parameters
        
        :param str friendly_name: A human readable description of the queue
        :param str max_size: The maximum number of members that can be in the queue at a
            time
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Queue`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Remove an empty queue
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Queues(ListResource):
    name = "Queues"
    mount_name = "queues"
    key = "queues"
    instance = Queue

    def __init__(self, *args, **kwargs):
        super(Queues, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch an instance of a queue identified by the QueueSid
        
        :param str sid: The queue Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Queue`
        :returns: A placeholder for a :class:`Queue` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update the queue with the new parameters
        
        :param str friendly_name: A human readable description of the queue
        :param str max_size: The maximum number of members that can be in the queue at a
            time
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Queue`
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Remove an empty queue
        
        :param str sid: The queue Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of queues belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Queue`
        """
        return self.get_instances(kwargs)

    def create(self, **kwargs):
        """
        Create a queue
        
        :param str friendly_name: A user-provided string that identifies this queue.
        :param str max_size: The upper limit of calls allowed to be in the queue. The
            default is 100. The maximum is 1000.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Queue`
        """
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of queues belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Queue`
        """
        return super(Queues, self).iter(**kwargs)
