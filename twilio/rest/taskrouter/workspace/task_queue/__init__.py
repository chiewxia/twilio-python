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
from twilio.rest.taskrouter.workspace.task_queue.task_queue_statistics import (
    Statistics,
    StatisticsList,
)
from twilio.rest.resources.base import NextGenListResource
from twilio.rest.taskrouter.workspace.task_queue.task_queues_statistics import (
    StatisticsList as TaskQueuesStatistics_StatisticsList,
    Statistics as TaskQueuesStatistics_Statistics,
)


class TaskQueue(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: assignment_activity_sid
    
        The assignment_activity_sid
    
    .. attribute:: assignment_activity_name
    
        The assignment_activity_name
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: max_reserved_workers
    
        The max_reserved_workers
    
    .. attribute:: reservation_activity_sid
    
        The reservation_activity_sid
    
    .. attribute:: reservation_activity_name
    
        The reservation_activity_name
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: target_workers
    
        The target_workers
    
    .. attribute:: url
    
        The url
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    """
    id_key = "sid"
    subresources = [
        StatisticsList
    ]

    def load(self, *args, **kwargs):
        super(TaskQueue, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str assignment_activity_sid: The assignment_activity_sid
        :param str friendly_name: The friendly_name
        :param str max_reserved_workers: The max_reserved_workers
        :param str reservation_activity_sid: The reservation_activity_sid
        :param str target_workers: The target_workers
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`TaskQueue`
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


class TaskQueues(NextGenListResource):
    name = "TaskQueues"
    mount_name = "task_queues"
    key = "task_queues"
    instance = TaskQueue

    def __init__(self, *args, **kwargs):
        super(TaskQueues, self).__init__(*args, **kwargs)
        self.statistics = TaskQueuesStatistics_StatisticsList(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`TaskQueue`
        :returns: A placeholder for a :class:`TaskQueue` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`TaskQueue`
        
        :param str assignment_activity_sid: The assignment_activity_sid
        :param str friendly_name: The friendly_name
        :param str max_reserved_workers: The max_reserved_workers
        :param str reservation_activity_sid: The reservation_activity_sid
        :param str sid: The sid
        :param str target_workers: The target_workers
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`TaskQueue`
        """
        return self.update_instance(sid, kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`TaskQueue`
        
        :param str evaluate_worker_attributes: The evaluate_worker_attributes
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`TaskQueue`
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, reservation_activity_sid,
               assignment_activity_sid, **kwargs):
        """
        Create a new :class:`TaskQueue`
        
        :param str assignment_activity_sid: The assignment_activity_sid
        :param str friendly_name: The friendly_name
        :param str max_reserved_workers: The max_reserved_workers
        :param str reservation_activity_sid: The reservation_activity_sid
        :param str target_workers: The target_workers
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`TaskQueue`
        """
        kwargs["FriendlyName"] = friendly_name
        kwargs["ReservationActivitySid"] = reservation_activity_sid
        kwargs["AssignmentActivitySid"] = assignment_activity_sid
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the :class:`TaskQueue`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`TaskQueue` using an iterator
        
        :param str evaluate_worker_attributes: The evaluate_worker_attributes
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`TaskQueue`
        """
        return super(TaskQueues, self).iter(**kwargs)
