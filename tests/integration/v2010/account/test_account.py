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


class AccountIntegrationTest(unittest.TestCase):

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "auth_token": "AUTHTOKEN",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Wed, 25 Aug 2010 01:30:09 +0000",
            "friendly_name": "Test Account",
            "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "active",
            "subresource_uris": {
                "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"
            },
            "type": "Full",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.create(friendly_name="friendly_name")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "FriendlyName": "friendly_name"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "auth_token": "AUTHTOKEN",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Wed, 25 Aug 2010 01:30:09 +0000",
            "friendly_name": "Test Account",
            "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "active",
            "subresource_uris": {
                "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"
            },
            "type": "Full",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.create(friendly_name="friendly_name")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.auth_token)
        self.assertEqual(u"AUTHTOKEN", instance.auth_token)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 15 Mar 2009 02:08:47 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Wed, 25 Aug 2010 01:30:09 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Test Account", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"active", instance.status)
        self.assertIsNotNone(instance.type)
        self.assertEqual(u"Full", instance.type)

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "auth_token": "AUTHTOKEN",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Wed, 25 Aug 2010 01:30:09 +0000",
            "friendly_name": "Test Account",
            "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "active",
            "subresource_uris": {
                "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"
            },
            "type": "Full",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "auth_token": "AUTHTOKEN",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Wed, 25 Aug 2010 01:30:09 +0000",
            "friendly_name": "Test Account",
            "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "active",
            "subresource_uris": {
                "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"
            },
            "type": "Full",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.auth_token)
        self.assertEqual(u"AUTHTOKEN", instance.auth_token)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 15 Mar 2009 02:08:47 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Wed, 25 Aug 2010 01:30:09 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Test Account", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"active", instance.status)
        self.assertIsNotNone(instance.type)
        self.assertEqual(u"Full", instance.type)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "accounts": [
                {
                    "auth_token": "foobar",
                    "date_created": "Tue, 23 Aug 2011 20:58:45 +0000",
                    "date_updated": "Fri, 04 Sep 2015 22:53:32 +0000",
                    "friendly_name": "Sub account for testing requests authed with parent account",
                    "owner_account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "active",
                    "subresource_uris": {
                        "applications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json",
                        "authorized_connect_apps": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AuthorizedConnectApps.json",
                        "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                        "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                        "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                        "connect_apps": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json",
                        "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json",
                        "messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json",
                        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                        "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                        "queues": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json",
                        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                        "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                        "sip": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP.json",
                        "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",
                        "usage": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage.json"
                    },
                    "type": "Full",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts.json?PageSize=1&Page=4",
            "next_page_uri": null,
            "num_pages": 5,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 5,
            "uri": "/2010-04-01/Accounts.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].auth_token)
        self.assertEqual(u"foobar", instances[0].auth_token)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Tue, 23 Aug 2011 20:58:45 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Fri, 04 Sep 2015 22:53:32 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"Sub account for testing requests authed with parent account", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].owner_account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].owner_account_sid)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].status)
        self.assertEqual(u"active", instances[0].status)
        self.assertIsNotNone(instances[0].type)
        self.assertEqual(u"Full", instances[0].type)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "accounts": [
                {
                    "auth_token": "foobar",
                    "date_created": "Tue, 23 Aug 2011 20:58:45 +0000",
                    "date_updated": "Fri, 04 Sep 2015 22:53:32 +0000",
                    "friendly_name": "Sub account for testing requests authed with parent account",
                    "owner_account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "active",
                    "subresource_uris": {
                        "applications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json",
                        "authorized_connect_apps": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AuthorizedConnectApps.json",
                        "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                        "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                        "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                        "connect_apps": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json",
                        "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json",
                        "messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json",
                        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                        "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                        "queues": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json",
                        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                        "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                        "sip": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP.json",
                        "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",
                        "usage": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage.json"
                    },
                    "type": "Full",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts.json?PageSize=1&Page=4",
            "next_page_uri": null,
            "num_pages": 5,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 5,
            "uri": "/2010-04-01/Accounts.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "accounts": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts.json?PageSize=1&Page=4",
            "next_page_uri": null,
            "num_pages": 5,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 5,
            "uri": "/2010-04-01/Accounts.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "accounts": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts.json?PageSize=1&Page=4",
            "next_page_uri": null,
            "num_pages": 5,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 5,
            "uri": "/2010-04-01/Accounts.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "auth_token": "AUTHTOKEN",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Wed, 25 Aug 2010 01:30:09 +0000",
            "friendly_name": "Test Account",
            "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "active",
            "subresource_uris": {
                "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"
            },
            "type": "Full",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.update(
                "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                status="active"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "FriendlyName": "friendly_name",
                "Status": "active"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "auth_token": "AUTHTOKEN",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Wed, 25 Aug 2010 01:30:09 +0000",
            "friendly_name": "Test Account",
            "sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "active",
            "subresource_uris": {
                "available_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json",
                "calls": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json",
                "conferences": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json",
                "incoming_phone_numbers": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json",
                "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
                "outgoing_caller_ids": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json",
                "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",
                "sandbox": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                "sms_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
                "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"
            },
            "type": "Full",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.update(
                "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                status="active"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.auth_token)
        self.assertEqual(u"AUTHTOKEN", instance.auth_token)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 15 Mar 2009 02:08:47 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Wed, 25 Aug 2010 01:30:09 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Test Account", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"active", instance.status)
        self.assertIsNotNone(instance.type)
        self.assertEqual(u"Full", instance.type)
