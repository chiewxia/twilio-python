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


class ApplicationIntegrationTest(unittest.TestCase):

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
            "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
            "friendly_name": "Application Friendly Name",
            "message_status_callback": "http://www.example.com/sms-status-callback",
            "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "GET",
            "sms_fallback_url": "http://www.example.com/sms-fallback",
            "sms_method": "GET",
            "sms_status_callback": "http://www.example.com/sms-status-callback",
            "sms_url": "http://example.com",
            "status_callback": "http://example.com",
            "status_callback_method": "GET",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_caller_id_lookup": false,
            "voice_fallback_method": "GET",
            "voice_fallback_url": "http://www.example.com/voice-callback",
            "voice_method": "GET",
            "voice_url": "http://example.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.create(
                "friendly_name",
                api_version="api_version",
                voice_url="https://example.com",
                voice_method="GET",
                voice_fallback_url="https://example.com",
                voice_fallback_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET",
                voice_caller_id_lookup=True,
                sms_url="https://example.com",
                sms_method="GET",
                sms_fallback_url="https://example.com",
                sms_fallback_method="GET",
                sms_status_callback="https://example.com",
                message_status_callback="https://example.com"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ApiVersion": "api_version",
                "FriendlyName": "friendly_name",
                "MessageStatusCallback": "https://example.com",
                "SmsFallbackMethod": "GET",
                "SmsFallbackUrl": "https://example.com",
                "SmsMethod": "GET",
                "SmsStatusCallback": "https://example.com",
                "SmsUrl": "https://example.com",
                "StatusCallback": "https://example.com",
                "StatusCallbackMethod": "GET",
                "VoiceCallerIdLookup": "true",
                "VoiceFallbackMethod": "GET",
                "VoiceFallbackUrl": "https://example.com",
                "VoiceMethod": "GET",
                "VoiceUrl": "https://example.com"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
            "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
            "friendly_name": "Application Friendly Name",
            "message_status_callback": "http://www.example.com/sms-status-callback",
            "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "GET",
            "sms_fallback_url": "http://www.example.com/sms-fallback",
            "sms_method": "GET",
            "sms_status_callback": "http://www.example.com/sms-status-callback",
            "sms_url": "http://example.com",
            "status_callback": "http://example.com",
            "status_callback_method": "GET",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_caller_id_lookup": false,
            "voice_fallback_method": "GET",
            "voice_fallback_url": "http://www.example.com/voice-callback",
            "voice_method": "GET",
            "voice_url": "http://example.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.create(
                "friendly_name",
                api_version="api_version",
                voice_url="https://example.com",
                voice_method="GET",
                voice_fallback_url="https://example.com",
                voice_fallback_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET",
                voice_caller_id_lookup=True,
                sms_url="https://example.com",
                sms_method="GET",
                sms_fallback_url="https://example.com",
                sms_fallback_method="GET",
                sms_status_callback="https://example.com",
                message_status_callback="https://example.com"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Mon, 22 Aug 2011 20:59:45 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 16:48:57 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Application Friendly Name", instance.friendly_name)
        self.assertIsNotNone(instance.message_status_callback)
        self.assertEqual(u"http://www.example.com/sms-status-callback", instance.message_status_callback)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.sms_fallback_method)
        self.assertEqual(u"GET", instance.sms_fallback_method)
        self.assertIsNotNone(instance.sms_fallback_url)
        self.assertEqual(u"http://www.example.com/sms-fallback", instance.sms_fallback_url)
        self.assertIsNotNone(instance.sms_method)
        self.assertEqual(u"GET", instance.sms_method)
        self.assertIsNotNone(instance.sms_status_callback)
        self.assertEqual(u"http://www.example.com/sms-status-callback", instance.sms_status_callback)
        self.assertIsNotNone(instance.sms_url)
        self.assertEqual(u"http://example.com", instance.sms_url)
        self.assertIsNotNone(instance.status_callback)
        self.assertEqual(u"http://example.com", instance.status_callback)
        self.assertIsNotNone(instance.status_callback_method)
        self.assertEqual(u"GET", instance.status_callback_method)
        self.assertIsNotNone(instance.voice_caller_id_lookup)
        self.assertEqual(False, instance.voice_caller_id_lookup)
        self.assertIsNotNone(instance.voice_fallback_method)
        self.assertEqual(u"GET", instance.voice_fallback_method)
        self.assertIsNotNone(instance.voice_fallback_url)
        self.assertEqual(u"http://www.example.com/voice-callback", instance.voice_fallback_url)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"GET", instance.voice_method)
        self.assertIsNotNone(instance.voice_url)
        self.assertEqual(u"http://example.com", instance.voice_url)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.delete("APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .applications.delete("APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
            "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
            "friendly_name": "Application Friendly Name",
            "message_status_callback": "http://www.example.com/sms-status-callback",
            "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "GET",
            "sms_fallback_url": "http://www.example.com/sms-fallback",
            "sms_method": "GET",
            "sms_status_callback": "http://www.example.com/sms-status-callback",
            "sms_url": "http://example.com",
            "status_callback": "http://example.com",
            "status_callback_method": "GET",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_caller_id_lookup": false,
            "voice_fallback_method": "GET",
            "voice_fallback_url": "http://www.example.com/voice-callback",
            "voice_method": "GET",
            "voice_url": "http://example.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.get("APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "api_version": "2010-04-01",
            "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
            "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
            "friendly_name": "Application Friendly Name",
            "message_status_callback": "http://www.example.com/sms-status-callback",
            "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "GET",
            "sms_fallback_url": "http://www.example.com/sms-fallback",
            "sms_method": "GET",
            "sms_status_callback": "http://www.example.com/sms-status-callback",
            "sms_url": "http://example.com",
            "status_callback": "http://example.com",
            "status_callback_method": "GET",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_caller_id_lookup": false,
            "voice_fallback_method": "GET",
            "voice_fallback_url": "http://www.example.com/voice-callback",
            "voice_method": "GET",
            "voice_url": "http://example.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.get("APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Mon, 22 Aug 2011 20:59:45 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 16:48:57 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Application Friendly Name", instance.friendly_name)
        self.assertIsNotNone(instance.message_status_callback)
        self.assertEqual(u"http://www.example.com/sms-status-callback", instance.message_status_callback)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.sms_fallback_method)
        self.assertEqual(u"GET", instance.sms_fallback_method)
        self.assertIsNotNone(instance.sms_fallback_url)
        self.assertEqual(u"http://www.example.com/sms-fallback", instance.sms_fallback_url)
        self.assertIsNotNone(instance.sms_method)
        self.assertEqual(u"GET", instance.sms_method)
        self.assertIsNotNone(instance.sms_status_callback)
        self.assertEqual(u"http://www.example.com/sms-status-callback", instance.sms_status_callback)
        self.assertIsNotNone(instance.sms_url)
        self.assertEqual(u"http://example.com", instance.sms_url)
        self.assertIsNotNone(instance.status_callback)
        self.assertEqual(u"http://example.com", instance.status_callback)
        self.assertIsNotNone(instance.status_callback_method)
        self.assertEqual(u"GET", instance.status_callback_method)
        self.assertIsNotNone(instance.voice_caller_id_lookup)
        self.assertEqual(False, instance.voice_caller_id_lookup)
        self.assertIsNotNone(instance.voice_fallback_method)
        self.assertEqual(u"GET", instance.voice_fallback_method)
        self.assertIsNotNone(instance.voice_fallback_url)
        self.assertEqual(u"http://www.example.com/voice-callback", instance.voice_fallback_url)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"GET", instance.voice_method)
        self.assertIsNotNone(instance.voice_url)
        self.assertEqual(u"http://example.com", instance.voice_url)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "applications": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "date_created": "Fri, 21 Aug 2015 00:07:25 +0000",
                    "date_updated": "Fri, 21 Aug 2015 00:07:25 +0000",
                    "friendly_name": "d8821fb7-4d01-48b2-bdc5-34e46252b90b",
                    "message_status_callback": null,
                    "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sms_fallback_method": "POST",
                    "sms_fallback_url": null,
                    "sms_method": "POST",
                    "sms_status_callback": null,
                    "sms_url": null,
                    "status_callback": null,
                    "status_callback_method": "POST",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "voice_caller_id_lookup": false,
                    "voice_fallback_method": "POST",
                    "voice_fallback_url": null,
                    "voice_method": "POST",
                    "voice_url": null
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=35",
            "next_page_uri": null,
            "num_pages": 36,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 36,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.list(friendly_name="friendly_name")
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2015 00:07:25 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Fri, 21 Aug 2015 00:07:25 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"d8821fb7-4d01-48b2-bdc5-34e46252b90b", instances[0].friendly_name)
        self.assertIsNone(instances[0].message_status_callback)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].sms_fallback_method)
        self.assertEqual(u"POST", instances[0].sms_fallback_method)
        self.assertIsNone(instances[0].sms_fallback_url)
        self.assertIsNotNone(instances[0].sms_method)
        self.assertEqual(u"POST", instances[0].sms_method)
        self.assertIsNone(instances[0].sms_status_callback)
        self.assertIsNone(instances[0].sms_url)
        self.assertIsNone(instances[0].status_callback)
        self.assertIsNotNone(instances[0].status_callback_method)
        self.assertEqual(u"POST", instances[0].status_callback_method)
        self.assertIsNotNone(instances[0].voice_caller_id_lookup)
        self.assertEqual(False, instances[0].voice_caller_id_lookup)
        self.assertIsNotNone(instances[0].voice_fallback_method)
        self.assertEqual(u"POST", instances[0].voice_fallback_method)
        self.assertIsNone(instances[0].voice_fallback_url)
        self.assertIsNotNone(instances[0].voice_method)
        self.assertEqual(u"POST", instances[0].voice_method)
        self.assertIsNone(instances[0].voice_url)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "applications": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "date_created": "Fri, 21 Aug 2015 00:07:25 +0000",
                    "date_updated": "Fri, 21 Aug 2015 00:07:25 +0000",
                    "friendly_name": "d8821fb7-4d01-48b2-bdc5-34e46252b90b",
                    "message_status_callback": null,
                    "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sms_fallback_method": "POST",
                    "sms_fallback_url": null,
                    "sms_method": "POST",
                    "sms_status_callback": null,
                    "sms_url": null,
                    "status_callback": null,
                    "status_callback_method": "POST",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "voice_caller_id_lookup": false,
                    "voice_fallback_method": "POST",
                    "voice_fallback_url": null,
                    "voice_method": "POST",
                    "voice_url": null
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=35",
            "next_page_uri": null,
            "num_pages": 36,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 36,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.list(friendly_name="friendly_name")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "applications": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=35",
            "next_page_uri": null,
            "num_pages": 36,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 36,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.list(friendly_name="friendly_name")
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "applications": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=35",
            "next_page_uri": null,
            "num_pages": 36,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 36,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.list(friendly_name="friendly_name")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name"
            },
        )

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
            "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
            "friendly_name": "Application Friendly Name",
            "message_status_callback": "http://www.example.com/sms-status-callback",
            "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "GET",
            "sms_fallback_url": "http://www.example.com/sms-fallback",
            "sms_method": "GET",
            "sms_status_callback": "http://www.example.com/sms-status-callback",
            "sms_url": "http://example.com",
            "status_callback": "http://example.com",
            "status_callback_method": "GET",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_caller_id_lookup": false,
            "voice_fallback_method": "GET",
            "voice_fallback_url": "http://www.example.com/voice-callback",
            "voice_method": "GET",
            "voice_url": "http://example.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.update(
                "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                api_version="api_version",
                voice_url="https://example.com",
                voice_method="GET",
                voice_fallback_url="https://example.com",
                voice_fallback_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET",
                voice_caller_id_lookup=True,
                sms_url="https://example.com",
                sms_method="GET",
                sms_fallback_url="https://example.com",
                sms_fallback_method="GET",
                sms_status_callback="https://example.com",
                message_status_callback="https://example.com"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ApiVersion": "api_version",
                "FriendlyName": "friendly_name",
                "MessageStatusCallback": "https://example.com",
                "SmsFallbackMethod": "GET",
                "SmsFallbackUrl": "https://example.com",
                "SmsMethod": "GET",
                "SmsStatusCallback": "https://example.com",
                "SmsUrl": "https://example.com",
                "StatusCallback": "https://example.com",
                "StatusCallbackMethod": "GET",
                "VoiceCallerIdLookup": "true",
                "VoiceFallbackMethod": "GET",
                "VoiceFallbackUrl": "https://example.com",
                "VoiceMethod": "GET",
                "VoiceUrl": "https://example.com"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
            "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
            "friendly_name": "Application Friendly Name",
            "message_status_callback": "http://www.example.com/sms-status-callback",
            "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "GET",
            "sms_fallback_url": "http://www.example.com/sms-fallback",
            "sms_method": "GET",
            "sms_status_callback": "http://www.example.com/sms-status-callback",
            "sms_url": "http://example.com",
            "status_callback": "http://example.com",
            "status_callback_method": "GET",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_caller_id_lookup": false,
            "voice_fallback_method": "GET",
            "voice_fallback_url": "http://www.example.com/voice-callback",
            "voice_method": "GET",
            "voice_url": "http://example.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .applications.update(
                "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                api_version="api_version",
                voice_url="https://example.com",
                voice_method="GET",
                voice_fallback_url="https://example.com",
                voice_fallback_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET",
                voice_caller_id_lookup=True,
                sms_url="https://example.com",
                sms_method="GET",
                sms_fallback_url="https://example.com",
                sms_fallback_method="GET",
                sms_status_callback="https://example.com",
                message_status_callback="https://example.com"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Mon, 22 Aug 2011 20:59:45 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 16:48:57 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Application Friendly Name", instance.friendly_name)
        self.assertIsNotNone(instance.message_status_callback)
        self.assertEqual(u"http://www.example.com/sms-status-callback", instance.message_status_callback)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.sms_fallback_method)
        self.assertEqual(u"GET", instance.sms_fallback_method)
        self.assertIsNotNone(instance.sms_fallback_url)
        self.assertEqual(u"http://www.example.com/sms-fallback", instance.sms_fallback_url)
        self.assertIsNotNone(instance.sms_method)
        self.assertEqual(u"GET", instance.sms_method)
        self.assertIsNotNone(instance.sms_status_callback)
        self.assertEqual(u"http://www.example.com/sms-status-callback", instance.sms_status_callback)
        self.assertIsNotNone(instance.sms_url)
        self.assertEqual(u"http://example.com", instance.sms_url)
        self.assertIsNotNone(instance.status_callback)
        self.assertEqual(u"http://example.com", instance.status_callback)
        self.assertIsNotNone(instance.status_callback_method)
        self.assertEqual(u"GET", instance.status_callback_method)
        self.assertIsNotNone(instance.voice_caller_id_lookup)
        self.assertEqual(False, instance.voice_caller_id_lookup)
        self.assertIsNotNone(instance.voice_fallback_method)
        self.assertEqual(u"GET", instance.voice_fallback_method)
        self.assertIsNotNone(instance.voice_fallback_url)
        self.assertEqual(u"http://www.example.com/voice-callback", instance.voice_fallback_url)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"GET", instance.voice_method)
        self.assertIsNotNone(instance.voice_url)
        self.assertEqual(u"http://example.com", instance.voice_url)
