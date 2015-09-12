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


class TaskQueueIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_activity_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
            "assignment_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:41Z",
            "date_updated": "2015-08-03T17:31:41Z",
            "friendly_name": "81f96435-3a05-11e5-9f81-98e0d9a1eb73",
            "links": {
                "assignment_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reservation_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_activity_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
            "reservation_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "target_workers": null,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.get("WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_activity_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
            "assignment_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:41Z",
            "date_updated": "2015-08-03T17:31:41Z",
            "friendly_name": "81f96435-3a05-11e5-9f81-98e0d9a1eb73",
            "links": {
                "assignment_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reservation_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_activity_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
            "reservation_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "target_workers": null,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.get("WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.assignment_activity_name)
        self.assertEqual(u"817ca1c5-3a05-11e5-9292-98e0d9a1eb73", instance.assignment_activity_name)
        self.assertIsNotNone(instance.assignment_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.assignment_activity_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:41Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:41Z"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"81f96435-3a05-11e5-9f81-98e0d9a1eb73", instance.friendly_name)
        self.assertIsNotNone(instance.reservation_activity_name)
        self.assertEqual(u"80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73", instance.reservation_activity_name)
        self.assertIsNotNone(instance.reservation_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.reservation_activity_sid)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNone(instance.target_workers)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_activity_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
            "assignment_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:41Z",
            "date_updated": "2015-08-03T17:31:41Z",
            "friendly_name": "81f96435-3a05-11e5-9f81-98e0d9a1eb73",
            "links": {
                "assignment_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reservation_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_activity_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
            "reservation_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "target_workers": null,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.update(
                "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                target_workers="target_workers",
                reservation_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                assignment_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                max_reserved_workers=1
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "AssignmentActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "FriendlyName": "friendly_name",
                "MaxReservedWorkers": 1,
                "ReservationActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "TargetWorkers": "target_workers"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_activity_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
            "assignment_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:41Z",
            "date_updated": "2015-08-03T17:31:41Z",
            "friendly_name": "81f96435-3a05-11e5-9f81-98e0d9a1eb73",
            "links": {
                "assignment_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reservation_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_activity_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
            "reservation_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "target_workers": null,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.update(
                "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                target_workers="target_workers",
                reservation_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                assignment_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                max_reserved_workers=1
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.assignment_activity_name)
        self.assertEqual(u"817ca1c5-3a05-11e5-9292-98e0d9a1eb73", instance.assignment_activity_name)
        self.assertIsNotNone(instance.assignment_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.assignment_activity_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:41Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:41Z"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"81f96435-3a05-11e5-9f81-98e0d9a1eb73", instance.friendly_name)
        self.assertIsNotNone(instance.reservation_activity_name)
        self.assertEqual(u"80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73", instance.reservation_activity_name)
        self.assertIsNotNone(instance.reservation_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.reservation_activity_sid)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNone(instance.target_workers)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues?PageSize=50&Page=0",
                "key": "task_queues",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues?PageSize=50&Page=0"
            },
            "task_queues": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "assignment_activity_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                    "assignment_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2015-08-03T17:31:41Z",
                    "date_updated": "2015-08-03T17:31:41Z",
                    "friendly_name": "81f96435-3a05-11e5-9f81-98e0d9a1eb73",
                    "links": {
                        "assignment_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "reservation_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    "reservation_activity_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                    "reservation_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "target_workers": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.list(
                friendly_name="friendly_name",
                evaluate_worker_attributes="evaluate_worker_attributes"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].assignment_activity_name)
        self.assertEqual(u"817ca1c5-3a05-11e5-9292-98e0d9a1eb73", instances[0].assignment_activity_name)
        self.assertIsNotNone(instances[0].assignment_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].assignment_activity_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:41Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:41Z"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"81f96435-3a05-11e5-9f81-98e0d9a1eb73", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].reservation_activity_name)
        self.assertEqual(u"80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73", instances[0].reservation_activity_name)
        self.assertIsNotNone(instances[0].reservation_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].reservation_activity_sid)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNone(instances[0].target_workers)
        self.assertIsNotNone(instances[0].workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].workspace_sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues?PageSize=50&Page=0",
                "key": "task_queues",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues?PageSize=50&Page=0"
            },
            "task_queues": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "assignment_activity_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                    "assignment_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2015-08-03T17:31:41Z",
                    "date_updated": "2015-08-03T17:31:41Z",
                    "friendly_name": "81f96435-3a05-11e5-9f81-98e0d9a1eb73",
                    "links": {
                        "assignment_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "reservation_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    "reservation_activity_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                    "reservation_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "target_workers": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.list(
                friendly_name="friendly_name",
                evaluate_worker_attributes="evaluate_worker_attributes"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EvaluateWorkerAttributes": "evaluate_worker_attributes",
                "FriendlyName": "friendly_name"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues?PageSize=50&Page=0",
                "key": "task_queues",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues?PageSize=50&Page=0"
            },
            "task_queues": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.list(
                friendly_name="friendly_name",
                evaluate_worker_attributes="evaluate_worker_attributes"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues?PageSize=50&Page=0",
                "key": "task_queues",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues?PageSize=50&Page=0"
            },
            "task_queues": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.list(
                friendly_name="friendly_name",
                evaluate_worker_attributes="evaluate_worker_attributes"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EvaluateWorkerAttributes": "evaluate_worker_attributes",
                "FriendlyName": "friendly_name"
            },
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_activity_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
            "assignment_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:41Z",
            "date_updated": "2015-08-03T17:31:41Z",
            "friendly_name": "81f96435-3a05-11e5-9f81-98e0d9a1eb73",
            "links": {
                "assignment_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reservation_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_activity_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
            "reservation_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "target_workers": null,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.create(
                "friendly_name",
                "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                target_workers="target_workers",
                max_reserved_workers=1
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "AssignmentActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "FriendlyName": "friendly_name",
                "MaxReservedWorkers": 1,
                "ReservationActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "TargetWorkers": "target_workers"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "assignment_activity_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
            "assignment_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:41Z",
            "date_updated": "2015-08-03T17:31:41Z",
            "friendly_name": "81f96435-3a05-11e5-9f81-98e0d9a1eb73",
            "links": {
                "assignment_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reservation_activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "reservation_activity_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
            "reservation_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "target_workers": null,
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.create(
                "friendly_name",
                "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                target_workers="target_workers",
                max_reserved_workers=1
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.assignment_activity_name)
        self.assertEqual(u"817ca1c5-3a05-11e5-9292-98e0d9a1eb73", instance.assignment_activity_name)
        self.assertIsNotNone(instance.assignment_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.assignment_activity_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:41Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:41Z"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"81f96435-3a05-11e5-9f81-98e0d9a1eb73", instance.friendly_name)
        self.assertIsNotNone(instance.reservation_activity_name)
        self.assertEqual(u"80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73", instance.reservation_activity_name)
        self.assertIsNotNone(instance.reservation_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.reservation_activity_sid)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNone(instance.target_workers)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.delete("WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_delete_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .task_queues.delete("WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())
