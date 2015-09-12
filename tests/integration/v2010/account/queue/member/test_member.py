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
from twilio.rest.v2010.client import V2010Client
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class MemberIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_enqueued": "Tue, 07 Aug 2012 22:57:41 +0000",
            "position": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "wait_time": 143
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .members.get()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_enqueued": "Tue, 07 Aug 2012 22:57:41 +0000",
            "position": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "wait_time": 143
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .members.get()
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.call_sid)
        self.assertIsNotNone(instance.date_enqueued)
        self.assertEqual(parse_iso_date("Tue, 07 Aug 2012 22:57:41 +0000"), instance.date_enqueued)
        self.assertIsNotNone(instance.position)
        self.assertEqual(1, instance.position)
        self.assertIsNotNone(instance.wait_time)
        self.assertEqual(143, instance.wait_time)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_enqueued": "Tue, 07 Aug 2012 22:57:41 +0000",
            "position": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "wait_time": 143
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .members.update(
                "https://example.com",
                "GET"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "Method": "GET",
                "Url": "https://example.com"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_enqueued": "Tue, 07 Aug 2012 22:57:41 +0000",
            "position": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "wait_time": 143
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .members.update(
                "https://example.com",
                "GET"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.call_sid)
        self.assertIsNotNone(instance.date_enqueued)
        self.assertEqual(parse_iso_date("Tue, 07 Aug 2012 22:57:41 +0000"), instance.date_enqueued)
        self.assertIsNotNone(instance.position)
        self.assertEqual(1, instance.position)
        self.assertIsNotNone(instance.wait_time)
        self.assertEqual(143, instance.wait_time)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "queue_members": [
                {
                    "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_enqueued": "Tue, 07 Aug 2012 22:57:41 +0000",
                    "position": 1,
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "wait_time": 124
                }
            ],
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .members.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].call_sid)
        self.assertIsNotNone(instances[0].date_enqueued)
        self.assertEqual(parse_iso_date("Tue, 07 Aug 2012 22:57:41 +0000"), instances[0].date_enqueued)
        self.assertIsNotNone(instances[0].position)
        self.assertEqual(1, instances[0].position)
        self.assertIsNotNone(instances[0].wait_time)
        self.assertEqual(124, instances[0].wait_time)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "queue_members": [
                {
                    "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_enqueued": "Tue, 07 Aug 2012 22:57:41 +0000",
                    "position": 1,
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "wait_time": 124
                }
            ],
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .members.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "queue_members": [],
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .members.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "queue_members": [],
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .queues.get("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .members.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )
