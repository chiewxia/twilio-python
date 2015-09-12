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

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0",
                "key": "task_queues_statistics",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0"
            },
            "task_queues_statistics": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "cumulative": {
                        "avg_task_acceptance_time": 0.0,
                        "end_time": "2015-08-18T00:46:15Z",
                        "reservations_accepted": 0,
                        "reservations_canceled": 0,
                        "reservations_created": 0,
                        "reservations_rejected": 0,
                        "reservations_rescinded": 0,
                        "reservations_timed_out": 0,
                        "start_time": "2015-08-18T00:31:15Z",
                        "tasks_canceled": 0,
                        "tasks_deleted": 0,
                        "tasks_entered": 0,
                        "tasks_moved": 0
                    },
                    "realtime": {
                        "activity_statistics": [
                            {
                                "friendly_name": "Offline",
                                "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                "workers": 0
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
                        "longest_task_waiting_age": 0,
                        "longest_task_waiting_sid": null,
                        "tasks_by_status": {
                            "assigned": 0,
                            "pending": 0,
                            "reserved": 0
                        },
                        "total_available_workers": 0,
                        "total_eligible_workers": 0,
                        "total_tasks": 0
                    },
                    "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues \
            .statistics.list(
                end_date=datetime(2008, 1, 2, 0, 0),
                friendly_name="friendly_name",
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].cumulative)
        self.assertEqual({
            "avg_task_acceptance_time": 0.0,
            "end_time": "2015-08-18T00:46:15Z",
            "reservations_accepted": 0,
            "reservations_canceled": 0,
            "reservations_created": 0,
            "reservations_rejected": 0,
            "reservations_rescinded": 0,
            "reservations_timed_out": 0,
            "start_time": "2015-08-18T00:31:15Z",
            "tasks_canceled": 0,
            "tasks_deleted": 0,
            "tasks_entered": 0,
            "tasks_moved": 0
        }, instances[0].cumulative)
        self.assertIsNotNone(instances[0].realtime)
        self.assertEqual({
            "activity_statistics": [
                {
                    "friendly_name": "Offline",
                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workers": 0
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
            "longest_task_waiting_age": 0,
            "longest_task_waiting_sid": None,
            "tasks_by_status": {
                "assigned": 0,
                "pending": 0,
                "reserved": 0
            },
            "total_available_workers": 0,
            "total_eligible_workers": 0,
            "total_tasks": 0
        }, instances[0].realtime)
        self.assertIsNotNone(instances[0].task_queue_sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].task_queue_sid)
        self.assertIsNotNone(instances[0].workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].workspace_sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0",
                "key": "task_queues_statistics",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0"
            },
            "task_queues_statistics": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "cumulative": {
                        "avg_task_acceptance_time": 0.0,
                        "end_time": "2015-08-18T00:46:15Z",
                        "reservations_accepted": 0,
                        "reservations_canceled": 0,
                        "reservations_created": 0,
                        "reservations_rejected": 0,
                        "reservations_rescinded": 0,
                        "reservations_timed_out": 0,
                        "start_time": "2015-08-18T00:31:15Z",
                        "tasks_canceled": 0,
                        "tasks_deleted": 0,
                        "tasks_entered": 0,
                        "tasks_moved": 0
                    },
                    "realtime": {
                        "activity_statistics": [
                            {
                                "friendly_name": "Offline",
                                "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                "workers": 0
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
                        "longest_task_waiting_age": 0,
                        "longest_task_waiting_sid": null,
                        "tasks_by_status": {
                            "assigned": 0,
                            "pending": 0,
                            "reserved": 0
                        },
                        "total_available_workers": 0,
                        "total_eligible_workers": 0,
                        "total_tasks": 0
                    },
                    "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues \
            .statistics.list(
                end_date=datetime(2008, 1, 2, 0, 0),
                friendly_name="friendly_name",
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndDate": "2008-01-02",
                "FriendlyName": "friendly_name",
                "Minutes": 1,
                "StartDate": "2008-01-02"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0",
                "key": "task_queues_statistics",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0"
            },
            "task_queues_statistics": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues \
            .statistics.list(
                end_date=datetime(2008, 1, 2, 0, 0),
                friendly_name="friendly_name",
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0",
                "key": "task_queues_statistics",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0"
            },
            "task_queues_statistics": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues \
            .statistics.list(
                end_date=datetime(2008, 1, 2, 0, 0),
                friendly_name="friendly_name",
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndDate": "2008-01-02",
                "FriendlyName": "friendly_name",
                "Minutes": 1,
                "StartDate": "2008-01-02"
            },
        )
