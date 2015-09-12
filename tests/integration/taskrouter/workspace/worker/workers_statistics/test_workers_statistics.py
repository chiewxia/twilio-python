# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

import unittest
from datetime import datetime
from twilio.ext.holodeck import Holodeck
from twilio.rest.taskrouter.client import TaskrouterClient
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class StatisticsIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "cumulative": {
                "activity_durations": [
                    {
                        "avg": 0.0,
                        "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Busy",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Idle",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Offline",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Reserved",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    }
                ],
                "end_time": "2015-08-18T16:35:33Z",
                "reservations_accepted": 0,
                "reservations_canceled": 0,
                "reservations_created": 0,
                "reservations_rejected": 0,
                "reservations_rescinded": 0,
                "reservations_timed_out": 0,
                "start_time": "2015-08-18T16:20:33Z",
                "tasks_assigned": 0
            },
            "realtime": {
                "activity_statistics": [
                    {
                        "friendly_name": "Offline",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 1
                    },
                    {
                        "friendly_name": "Idle",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "Reserved",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "Busy",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    }
                ],
                "total_workers": 1
            },
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers \
            .statistics.get(
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                task_queue_name="task_queue_name",
                friendly_name="friendly_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/Statistics",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndDate": "2008-01-02",
                "FriendlyName": "friendly_name",
                "Minutes": 1,
                "StartDate": "2008-01-02",
                "TaskQueueName": "task_queue_name",
                "TaskQueueSid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "cumulative": {
                "activity_durations": [
                    {
                        "avg": 0.0,
                        "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Busy",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Idle",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Offline",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Reserved",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    }
                ],
                "end_time": "2015-08-18T16:35:33Z",
                "reservations_accepted": 0,
                "reservations_canceled": 0,
                "reservations_created": 0,
                "reservations_rejected": 0,
                "reservations_rescinded": 0,
                "reservations_timed_out": 0,
                "start_time": "2015-08-18T16:20:33Z",
                "tasks_assigned": 0
            },
            "realtime": {
                "activity_statistics": [
                    {
                        "friendly_name": "Offline",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 1
                    },
                    {
                        "friendly_name": "Idle",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "Reserved",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "Busy",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    },
                    {
                        "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workers": 0
                    }
                ],
                "total_workers": 1
            },
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers \
            .statistics.get(
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                task_queue_name="task_queue_name",
                friendly_name="friendly_name"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.cumulative)
        self.assertEqual({
            "activity_durations": [
                {
                    "avg": 0.0,
                    "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                    "max": 0,
                    "min": 0,
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "total": 0
                },
                {
                    "avg": 0.0,
                    "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                    "max": 0,
                    "min": 0,
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "total": 0
                },
                {
                    "avg": 0.0,
                    "friendly_name": "Busy",
                    "max": 0,
                    "min": 0,
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "total": 0
                },
                {
                    "avg": 0.0,
                    "friendly_name": "Idle",
                    "max": 0,
                    "min": 0,
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "total": 0
                },
                {
                    "avg": 0.0,
                    "friendly_name": "Offline",
                    "max": 0,
                    "min": 0,
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "total": 0
                },
                {
                    "avg": 0.0,
                    "friendly_name": "Reserved",
                    "max": 0,
                    "min": 0,
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "total": 0
                }
            ],
            "end_time": "2015-08-18T16:35:33Z",
            "reservations_accepted": 0,
            "reservations_canceled": 0,
            "reservations_created": 0,
            "reservations_rejected": 0,
            "reservations_rescinded": 0,
            "reservations_timed_out": 0,
            "start_time": "2015-08-18T16:20:33Z",
            "tasks_assigned": 0
        }, instance.cumulative)
        self.assertIsNotNone(instance.realtime)
        self.assertEqual({
            "activity_statistics": [
                {
                    "friendly_name": "Offline",
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workers": 1
                },
                {
                    "friendly_name": "Idle",
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workers": 0
                },
                {
                    "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workers": 0
                },
                {
                    "friendly_name": "Reserved",
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workers": 0
                },
                {
                    "friendly_name": "Busy",
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workers": 0
                },
                {
                    "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workers": 0
                }
            ],
            "total_workers": 1
        }, instance.realtime)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)
