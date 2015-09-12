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
from twilio.rest.resources.base import GetQuery


class Statistics(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: cumulative
    
        The cumulative
    
    .. attribute:: realtime
    
        The realtime
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    """
    id_key = "sid"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(Statistics, self).__init__(parent, None)


class StatisticsList(NextGenListResource):
    name = "Workers/Statistics"
    mount_name = "statistics"
    key = "statistics"
    instance = Statistics

    def __init__(self, *args, **kwargs):
        super(StatisticsList, self).__init__(*args, **kwargs)

    def get(self, **kwargs):
        """
        Get the Statistics
        
        :param date end_date: The end_date
        :param date start_date: The start_date
        :param str friendly_name: The friendly_name
        :param str minutes: The minutes
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        
        :raises TwilioRestException: when the request fails on execute
        """
        if "start_date" in kwargs:
            kwargs["StartDate"] = parse_date(kwargs["start_date"])
            del kwargs["start_date"]
        if "end_date" in kwargs:
            kwargs["EndDate"] = parse_date(kwargs["end_date"])
            del kwargs["end_date"]
        
        return GetQuery(self, self.uri, self.use_json_extension,
                        params=kwargs)

    def load_instance(self, data):
        """ Override because Statistics does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
