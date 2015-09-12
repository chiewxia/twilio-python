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
from twilio.rest.taskrouter.workspace.activity import (
    Activity,
    Activities,
)
from twilio.rest.taskrouter.workspace.event import (
    Event,
    Events,
)
from twilio.rest.taskrouter.workspace.task import (
    Task,
    Tasks,
)
from twilio.rest.taskrouter.workspace.task_queue import (
    TaskQueue,
    TaskQueues,
)
from twilio.rest.taskrouter.workspace.worker import (
    Worker,
    Workers,
)
from twilio.rest.taskrouter.workspace.workflow import (
    Workflow,
    Workflows,
)
from twilio.rest.taskrouter.workspace.statistics import (
    Statistics,
    StatisticsList,
)
from twilio.rest.resources.base import NextGenListResource


class Workspace(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: default_activity_name
    
        The default_activity_name
    
    .. attribute:: default_activity_sid
    
        The default_activity_sid
    
    .. attribute:: event_callback_url
    
        The event_callback_url
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: timeout_activity_name
    
        The timeout_activity_name
    
    .. attribute:: timeout_activity_sid
    
        The timeout_activity_sid
    """
    id_key = "sid"
    subresources = [
        Activities,
        Events,
        Tasks,
        TaskQueues,
        Workers,
        Workflows,
        StatisticsList
    ]

    def load(self, *args, **kwargs):
        super(Workspace, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str default_activity_sid: The default_activity_sid
        :param str event_callback_url: The event_callback_url
        :param str friendly_name: The friendly_name
        :param str timeout_activity_sid: The timeout_activity_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Workspace`
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


class Workspaces(NextGenListResource):
    name = "Workspaces"
    mount_name = "workspaces"
    key = "workspaces"
    instance = Workspace

    def __init__(self, *args, **kwargs):
        super(Workspaces, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Workspace`
        :returns: A placeholder for a :class:`Workspace` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Workspace`
        
        :param str default_activity_sid: The default_activity_sid
        :param str event_callback_url: The event_callback_url
        :param str friendly_name: The friendly_name
        :param str sid: The sid
        :param str timeout_activity_sid: The timeout_activity_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Workspace`
        """
        return self.update_instance(sid, kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Workspace`
        
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Workspace`
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Create a new :class:`Workspace`
        
        :param str event_callback_url: The event_callback_url
        :param str friendly_name: The friendly_name
        :param str template: The template
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Workspace`
        """
        kwargs["FriendlyName"] = friendly_name
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Workspace`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Workspace` using an iterator
        
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Workspace`
        """
        return super(Workspaces, self).iter(**kwargs)
