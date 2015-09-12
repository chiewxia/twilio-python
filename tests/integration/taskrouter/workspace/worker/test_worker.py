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


class WorkerIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers?PageSize=50&Page=0",
                "key": "workers",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers?PageSize=50&Page=0"
            },
            "workers": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "activity_name": "Offline",
                    "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "attributes": "{}",
                    "available": false,
                    "date_created": "2015-08-03T17:34:12Z",
                    "date_status_changed": "2015-08-03T17:34:12Z",
                    "date_updated": "2015-08-03T17:34:12Z",
                    "friendly_name": "dc7d5461-3a05-11e5-a889-98e0d9a1eb73",
                    "links": {
                        "activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.list(
                activity_name="activity_name",
                activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                available="available",
                friendly_name="friendly_name",
                target_workers_expression="target_workers_expression",
                task_queue_name="task_queue_name",
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].activity_name)
        self.assertEqual(u"Offline", instances[0].activity_name)
        self.assertIsNotNone(instances[0].activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].activity_sid)
        self.assertIsNotNone(instances[0].attributes)
        self.assertEqual(u"{}", instances[0].attributes)
        self.assertIsNotNone(instances[0].available)
        self.assertEqual(False, instances[0].available)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2015-08-03T17:34:12Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_status_changed)
        self.assertEqual(parse_iso_date("2015-08-03T17:34:12Z"), instances[0].date_status_changed)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("2015-08-03T17:34:12Z"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"dc7d5461-3a05-11e5-a889-98e0d9a1eb73", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].workspace_sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers?PageSize=50&Page=0",
                "key": "workers",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers?PageSize=50&Page=0"
            },
            "workers": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "activity_name": "Offline",
                    "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "attributes": "{}",
                    "available": false,
                    "date_created": "2015-08-03T17:34:12Z",
                    "date_status_changed": "2015-08-03T17:34:12Z",
                    "date_updated": "2015-08-03T17:34:12Z",
                    "friendly_name": "dc7d5461-3a05-11e5-a889-98e0d9a1eb73",
                    "links": {
                        "activity": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities/WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ]
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.list(
                activity_name="activity_name",
                activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                available="available",
                friendly_name="friendly_name",
                target_workers_expression="target_workers_expression",
                task_queue_name="task_queue_name",
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "ActivityName": "activity_name",
                "ActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "Available": "available",
                "FriendlyName": "friendly_name",
                "TargetWorkersExpression": "target_workers_expression",
                "TaskQueueName": "task_queue_name",
                "TaskQueueSid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers?PageSize=50&Page=0",
                "key": "workers",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers?PageSize=50&Page=0"
            },
            "workers": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.list(
                activity_name="activity_name",
                activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                available="available",
                friendly_name="friendly_name",
                target_workers_expression="target_workers_expression",
                task_queue_name="task_queue_name",
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "meta": {
                "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers?PageSize=50&Page=0",
                "key": "workers",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers?PageSize=50&Page=0"
            },
            "workers": []
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.list(
                activity_name="activity_name",
                activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                available="available",
                friendly_name="friendly_name",
                target_workers_expression="target_workers_expression",
                task_queue_name="task_queue_name",
                task_queue_sid="WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "ActivityName": "activity_name",
                "ActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "Available": "available",
                "FriendlyName": "friendly_name",
                "TargetWorkersExpression": "target_workers_expression",
                "TaskQueueName": "task_queue_name",
                "TaskQueueSid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "activity_name": "available",
            "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "attributes": "{\\"email\\": \\"test@twilio.com\\", \\"phone\\": \\"8675309\\"}",
            "available": true,
            "date_created": "2014-05-14T10:50:02Z",
            "date_status_changed": "2014-05-14T23:26:06Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "friendly_name": "Test Worker",
            "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.create(
                "friendly_name",
                activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                attributes="attributes"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "Attributes": "attributes",
                "FriendlyName": "friendly_name"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "activity_name": "available",
            "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "attributes": "{\\"email\\": \\"test@twilio.com\\", \\"phone\\": \\"8675309\\"}",
            "available": true,
            "date_created": "2014-05-14T10:50:02Z",
            "date_status_changed": "2014-05-14T23:26:06Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "friendly_name": "Test Worker",
            "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.create(
                "friendly_name",
                activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                attributes="attributes"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.activity_name)
        self.assertEqual(u"available", instance.activity_name)
        self.assertIsNotNone(instance.activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.activity_sid)
        self.assertIsNotNone(instance.attributes)
        self.assertEqual(u"{\"email\": \"test@twilio.com\", \"phone\": \"8675309\"}", instance.attributes)
        self.assertIsNotNone(instance.available)
        self.assertEqual(True, instance.available)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_status_changed)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_status_changed)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Test Worker", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "activity_name": "available",
            "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "attributes": "{\\"email\\": \\"test@twilio.com\\", \\"phone\\": \\"8675309\\"}",
            "available": true,
            "date_created": "2014-05-14T10:50:02Z",
            "date_status_changed": "2014-05-14T23:26:06Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "friendly_name": "Test Worker",
            "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.get("WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
            "activity_name": "available",
            "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "attributes": "{\\"email\\": \\"test@twilio.com\\", \\"phone\\": \\"8675309\\"}",
            "available": true,
            "date_created": "2014-05-14T10:50:02Z",
            "date_status_changed": "2014-05-14T23:26:06Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "friendly_name": "Test Worker",
            "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.get("WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.activity_name)
        self.assertEqual(u"available", instance.activity_name)
        self.assertIsNotNone(instance.activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.activity_sid)
        self.assertIsNotNone(instance.attributes)
        self.assertEqual(u"{\"email\": \"test@twilio.com\", \"phone\": \"8675309\"}", instance.attributes)
        self.assertIsNotNone(instance.available)
        self.assertEqual(True, instance.available)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_status_changed)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_status_changed)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Test Worker", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "activity_name": "available",
            "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "attributes": "{\\"email\\": \\"test@twilio.com\\", \\"phone\\": \\"8675309\\"}",
            "available": true,
            "date_created": "2014-05-14T10:50:02Z",
            "date_status_changed": "2014-05-14T23:26:06Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "friendly_name": "Test Worker",
            "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.update(
                "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                attributes="attributes",
                friendly_name="friendly_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ActivitySid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "Attributes": "attributes",
                "FriendlyName": "friendly_name"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "activity_name": "available",
            "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "attributes": "{\\"email\\": \\"test@twilio.com\\", \\"phone\\": \\"8675309\\"}",
            "available": true,
            "date_created": "2014-05-14T10:50:02Z",
            "date_status_changed": "2014-05-14T23:26:06Z",
            "date_updated": "2014-05-14T23:26:06Z",
            "friendly_name": "Test Worker",
            "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.update(
                "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                activity_sid="WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                attributes="attributes",
                friendly_name="friendly_name"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.activity_name)
        self.assertEqual(u"available", instance.activity_name)
        self.assertIsNotNone(instance.activity_sid)
        self.assertEqual(u"WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.activity_sid)
        self.assertIsNotNone(instance.attributes)
        self.assertEqual(u"{\"email\": \"test@twilio.com\", \"phone\": \"8675309\"}", instance.attributes)
        self.assertIsNotNone(instance.available)
        self.assertEqual(True, instance.available)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2014-05-14T10:50:02Z"), instance.date_created)
        self.assertIsNotNone(instance.date_status_changed)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_status_changed)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2014-05-14T23:26:06Z"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Test Worker", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.delete("WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
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
            .workers.delete("WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())
