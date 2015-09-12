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


class WorkspaceIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:38Z",
            "date_updated": "2015-08-03T17:31:38Z",
            "default_activity_name": "Offline",
            "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "event_callback_url": "",
            "friendly_name": "8064de33-3a05-11e5-8bae-98e0d9a1eb73",
            "links": {
                "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows"
            },
            "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout_activity_name": "Offline",
            "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
            "date_created": "2015-08-03T17:31:38Z",
            "date_updated": "2015-08-03T17:31:38Z",
            "default_activity_name": "Offline",
            "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "event_callback_url": "",
            "friendly_name": "8064de33-3a05-11e5-8bae-98e0d9a1eb73",
            "links": {
                "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows"
            },
            "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout_activity_name": "Offline",
            "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:38Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:38Z"), instance.date_updated)
        self.assertIsNotNone(instance.default_activity_name)
        self.assertEqual(u"Offline", instance.default_activity_name)
        self.assertIsNotNone(instance.default_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.default_activity_sid)
        self.assertIsNotNone(instance.event_callback_url)
        self.assertEqual(u"", instance.event_callback_url)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"8064de33-3a05-11e5-8bae-98e0d9a1eb73", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.timeout_activity_name)
        self.assertEqual(u"Offline", instance.timeout_activity_name)
        self.assertIsNotNone(instance.timeout_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.timeout_activity_sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:38Z",
            "date_updated": "2015-08-03T17:31:38Z",
            "default_activity_name": "Offline",
            "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "event_callback_url": "",
            "friendly_name": "8064de33-3a05-11e5-8bae-98e0d9a1eb73",
            "links": {
                "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows"
            },
            "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout_activity_name": "Offline",
            "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.update(
                "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                default_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                event_callback_url="/example",
                friendly_name="friendly_name",
                timeout_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "DefaultActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "EventCallbackUrl": "/example",
                "FriendlyName": "friendly_name",
                "TimeoutActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:38Z",
            "date_updated": "2015-08-03T17:31:38Z",
            "default_activity_name": "Offline",
            "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "event_callback_url": "",
            "friendly_name": "8064de33-3a05-11e5-8bae-98e0d9a1eb73",
            "links": {
                "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows"
            },
            "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout_activity_name": "Offline",
            "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.update(
                "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                default_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                event_callback_url="/example",
                friendly_name="friendly_name",
                timeout_activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:38Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:38Z"), instance.date_updated)
        self.assertIsNotNone(instance.default_activity_name)
        self.assertEqual(u"Offline", instance.default_activity_name)
        self.assertIsNotNone(instance.default_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.default_activity_sid)
        self.assertIsNotNone(instance.event_callback_url)
        self.assertEqual(u"", instance.event_callback_url)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"8064de33-3a05-11e5-8bae-98e0d9a1eb73", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.timeout_activity_name)
        self.assertEqual(u"Offline", instance.timeout_activity_name)
        self.assertIsNotNone(instance.timeout_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.timeout_activity_sid)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=1&Page=0",
                "key": "workspaces",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=1&Page=0"
            },
            "workspaces": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2015-05-27T00:48:50Z",
                    "date_updated": "2015-05-27T00:48:50Z",
                    "default_activity_name": "Offline",
                    "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "event_callback_url": "",
                    "friendly_name": "cce151db-4644-4d48-95a1-d962829b69f0",
                    "links": {
                        "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                        "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                        "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                        "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                        "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                        "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows"
                    },
                    "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "timeout_activity_name": "Offline",
                    "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.list(friendly_name="friendly_name")
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2015-05-27T00:48:50Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("2015-05-27T00:48:50Z"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].default_activity_name)
        self.assertEqual(u"Offline", instances[0].default_activity_name)
        self.assertIsNotNone(instances[0].default_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].default_activity_sid)
        self.assertIsNotNone(instances[0].event_callback_url)
        self.assertEqual(u"", instances[0].event_callback_url)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"cce151db-4644-4d48-95a1-d962829b69f0", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].timeout_activity_name)
        self.assertEqual(u"Offline", instances[0].timeout_activity_name)
        self.assertIsNotNone(instances[0].timeout_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].timeout_activity_sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=1&Page=0",
                "key": "workspaces",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=1&Page=0"
            },
            "workspaces": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2015-05-27T00:48:50Z",
                    "date_updated": "2015-05-27T00:48:50Z",
                    "default_activity_name": "Offline",
                    "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "event_callback_url": "",
                    "friendly_name": "cce151db-4644-4d48-95a1-d962829b69f0",
                    "links": {
                        "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                        "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                        "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                        "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                        "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                        "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows"
                    },
                    "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "timeout_activity_name": "Offline",
                    "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.list(friendly_name="friendly_name")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=1&Page=0",
                "key": "workspaces",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=1&Page=0"
            },
            "workspaces": []
        }
        """))
        
        query = client \
            .workspaces.list(friendly_name="friendly_name")
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=1&Page=0",
                "key": "workspaces",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=1&Page=0"
            },
            "workspaces": []
        }
        """))
        
        query = client \
            .workspaces.list(friendly_name="friendly_name")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name"
            },
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:38Z",
            "date_updated": "2015-08-03T17:31:38Z",
            "default_activity_name": "Offline",
            "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "event_callback_url": "",
            "friendly_name": "8064de33-3a05-11e5-8bae-98e0d9a1eb73",
            "links": {
                "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows"
            },
            "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout_activity_name": "Offline",
            "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.create(
                "friendly_name",
                event_callback_url="/example",
                template="template"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "EventCallbackUrl": "/example",
                "FriendlyName": "friendly_name",
                "Template": "template"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "2015-08-03T17:31:38Z",
            "date_updated": "2015-08-03T17:31:38Z",
            "default_activity_name": "Offline",
            "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "event_callback_url": "",
            "friendly_name": "8064de33-3a05-11e5-8bae-98e0d9a1eb73",
            "links": {
                "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows"
            },
            "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "timeout_activity_name": "Offline",
            "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.create(
                "friendly_name",
                event_callback_url="/example",
                template="template"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:38Z"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2015-08-03T17:31:38Z"), instance.date_updated)
        self.assertIsNotNone(instance.default_activity_name)
        self.assertEqual(u"Offline", instance.default_activity_name)
        self.assertIsNotNone(instance.default_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.default_activity_sid)
        self.assertIsNotNone(instance.event_callback_url)
        self.assertEqual(u"", instance.event_callback_url)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"8064de33-3a05-11e5-8bae-98e0d9a1eb73", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.timeout_activity_name)
        self.assertEqual(u"Offline", instance.timeout_activity_name)
        self.assertIsNotNone(instance.timeout_activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.timeout_activity_sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .workspaces.delete("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_delete_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .workspaces.delete("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())
