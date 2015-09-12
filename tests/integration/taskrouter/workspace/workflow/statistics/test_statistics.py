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
                "avg_task_acceptance_time": 0.0,
                "end_time": "2014-08-06T22:39:00Z",
                "reservations_accepted": 0,
                "reservations_rejected": 0,
                "reservations_timed_out": 0,
                "start_time": "2014-08-06T22:24:00Z",
                "tasks_canceled": 0,
                "tasks_entered": 0,
                "tasks_moved": 0,
                "tasks_timed_out_in_workflow": 0
            },
            "realtime": {
                "longest_task_waiting_age": 0,
                "longest_task_waiting_sid": null,
                "tasks_by_status": {
                    "assigned": 1,
                    "pending": 0,
                    "reserved": 0
                },
                "total_tasks": 1
            },
            "workflow_sid": "WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.get("WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .statistics.get(
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndDate": "2008-01-02",
                "Minutes": 1,
                "StartDate": "2008-01-02"
            },
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "cumulative": {
                "avg_task_acceptance_time": 0.0,
                "end_time": "2014-08-06T22:39:00Z",
                "reservations_accepted": 0,
                "reservations_rejected": 0,
                "reservations_timed_out": 0,
                "start_time": "2014-08-06T22:24:00Z",
                "tasks_canceled": 0,
                "tasks_entered": 0,
                "tasks_moved": 0,
                "tasks_timed_out_in_workflow": 0
            },
            "realtime": {
                "longest_task_waiting_age": 0,
                "longest_task_waiting_sid": null,
                "tasks_by_status": {
                    "assigned": 1,
                    "pending": 0,
                    "reserved": 0
                },
                "total_tasks": 1
            },
            "workflow_sid": "WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workflows.get("WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .statistics.get(
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0)
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.workflow_sid)
        self.assertEqual(u"WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workflow_sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)
