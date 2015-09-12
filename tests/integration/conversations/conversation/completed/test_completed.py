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
from twilio.rest.conversations.client import ConversationsClient
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class CompletedIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "conversations": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2015-05-12T21:08:50Z",
                    "duration": 60,
                    "end_time": "2015-05-12T21:09:50Z",
                    "links": {
                        "participants": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
                    },
                    "sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "start_time": "2015-05-12T21:08:50Z",
                    "status": "completed",
                    "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "meta": {
                "first_page_url": "https://conversations.twilio.com/v1/Conversations/Completed?PageSize=50&Page=0",
                "key": "conversations",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://conversations.twilio.com/v1/Conversations/Completed?PageSize=50&Page=0"
            }
        }
        """))
        
        query = client \
            .conversations \
            .completed.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2015-05-12T21:08:50Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].duration)
        self.assertEqual(60, instances[0].duration)
        self.assertIsNotNone(instances[0].end_time)
        self.assertEqual(parse_iso_date("2015-05-12T21:09:50Z"), instances[0].end_time)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].start_time)
        self.assertEqual(parse_iso_date("2015-05-12T21:08:50Z"), instances[0].start_time)
        self.assertIsNotNone(instances[0].status)
        self.assertEqual(u"completed", instances[0].status)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "conversations": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "2015-05-12T21:08:50Z",
                    "duration": 60,
                    "end_time": "2015-05-12T21:09:50Z",
                    "links": {
                        "participants": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
                    },
                    "sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "start_time": "2015-05-12T21:08:50Z",
                    "status": "completed",
                    "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "meta": {
                "first_page_url": "https://conversations.twilio.com/v1/Conversations/Completed?PageSize=50&Page=0",
                "key": "conversations",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://conversations.twilio.com/v1/Conversations/Completed?PageSize=50&Page=0"
            }
        }
        """))
        
        query = client \
            .conversations \
            .completed.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://conversations.twilio.com/v1/Conversations/Completed",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "conversations": [],
            "meta": {
                "first_page_url": "https://conversations.twilio.com/v1/Conversations/Completed?PageSize=50&Page=0",
                "key": "conversations",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://conversations.twilio.com/v1/Conversations/Completed?PageSize=50&Page=0"
            }
        }
        """))
        
        query = client \
            .conversations \
            .completed.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = ConversationsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "conversations": [],
            "meta": {
                "first_page_url": "https://conversations.twilio.com/v1/Conversations/Completed?PageSize=50&Page=0",
                "key": "conversations",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://conversations.twilio.com/v1/Conversations/Completed?PageSize=50&Page=0"
            }
        }
        """))
        
        query = client \
            .conversations \
            .completed.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://conversations.twilio.com/v1/Conversations/Completed",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )
