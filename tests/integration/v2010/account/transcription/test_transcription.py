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


class TranscriptionIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "date_created": "Sun, 13 Feb 2011 02:12:08 +0000",
            "date_updated": "Sun, 13 Feb 2011 02:30:01 +0000",
            "duration": "1",
            "price": "-0.05000",
            "recording_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "failed",
            "transcription_text": "(blank)",
            "type": "fast",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .transcriptions.get("TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "date_created": "Sun, 13 Feb 2011 02:12:08 +0000",
            "date_updated": "Sun, 13 Feb 2011 02:30:01 +0000",
            "duration": "1",
            "price": "-0.05000",
            "recording_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "failed",
            "transcription_text": "(blank)",
            "type": "fast",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .transcriptions.get("TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 13 Feb 2011 02:12:08 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Sun, 13 Feb 2011 02:30:01 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.duration)
        self.assertEqual(u"1", instance.duration)
        self.assertIsNotNone(instance.price)
        self.assertEqual(u"-0.05000", instance.price)
        self.assertIsNotNone(instance.recording_sid)
        self.assertEqual(u"REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.recording_sid)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"failed", instance.status)
        self.assertIsNotNone(instance.transcription_text)
        self.assertEqual(u"(blank)", instance.transcription_text)
        self.assertIsNotNone(instance.type)
        self.assertEqual(u"fast", instance.type)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .transcriptions.delete("TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_delete_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .transcriptions.delete("TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=3",
            "next_page_uri": null,
            "num_pages": 4,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 4,
            "transcriptions": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2008-08-01",
                    "date_created": "Thu, 25 Aug 2011 20:59:45 +0000",
                    "date_updated": "Thu, 25 Aug 2011 20:59:45 +0000",
                    "duration": "10",
                    "price": "0.00000",
                    "price_unit": "USD",
                    "recording_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "completed",
                    "transcription_text": null,
                    "type": "fast",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .transcriptions.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2008-08-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Thu, 25 Aug 2011 20:59:45 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Thu, 25 Aug 2011 20:59:45 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].duration)
        self.assertEqual(u"10", instances[0].duration)
        self.assertIsNotNone(instances[0].price)
        self.assertEqual(u"0.00000", instances[0].price)
        self.assertIsNotNone(instances[0].price_unit)
        self.assertEqual(u"USD", instances[0].price_unit)
        self.assertIsNotNone(instances[0].recording_sid)
        self.assertEqual(u"REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].recording_sid)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].status)
        self.assertEqual(u"completed", instances[0].status)
        self.assertIsNone(instances[0].transcription_text)
        self.assertIsNotNone(instances[0].type)
        self.assertEqual(u"fast", instances[0].type)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=3",
            "next_page_uri": null,
            "num_pages": 4,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 4,
            "transcriptions": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2008-08-01",
                    "date_created": "Thu, 25 Aug 2011 20:59:45 +0000",
                    "date_updated": "Thu, 25 Aug 2011 20:59:45 +0000",
                    "duration": "10",
                    "price": "0.00000",
                    "price_unit": "USD",
                    "recording_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "completed",
                    "transcription_text": null,
                    "type": "fast",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .transcriptions.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",
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
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=3",
            "next_page_uri": null,
            "num_pages": 4,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 4,
            "transcriptions": [],
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .transcriptions.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=3",
            "next_page_uri": null,
            "num_pages": 4,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 4,
            "transcriptions": [],
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .transcriptions.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )
