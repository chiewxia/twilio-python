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


class SmsMessageIntegrationTest(unittest.TestCase):

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "body": "n",
            "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
            "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
            "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
            "direction": "outbound-api",
            "from": "+141586753093",
            "price": "-0.03000",
            "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "sent",
            "to": "+141586753096",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.create(
                "+123456789",
                "+987654321",
                body="body",
                media_url=['https://example.com'],
                status_callback="https://example.com",
                application_sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "Body": "body",
                "From": "+987654321",
                "MediaUrl": [
                    "https://example.com"
                ],
                "StatusCallback": "https://example.com",
                "To": "+123456789"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "body": "n",
            "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
            "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
            "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
            "direction": "outbound-api",
            "from": "+141586753093",
            "price": "-0.03000",
            "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "sent",
            "to": "+141586753096",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.create(
                "+123456789",
                "+987654321",
                body="body",
                media_url=['https://example.com'],
                status_callback="https://example.com",
                application_sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.body)
        self.assertEqual(u"n", instance.body)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:42 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_sent)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:44 +0000"), instance.date_sent)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:44 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.direction)
        self.assertEqual(u"outbound-api", instance.direction)
        self.assertIsNotNone(instance.from_)
        self.assertEqual(u"+141586753093", instance.from_)
        self.assertIsNotNone(instance.price)
        self.assertEqual(u"-0.03000", instance.price)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"sent", instance.status)
        self.assertIsNotNone(instance.to)
        self.assertEqual(u"+141586753096", instance.to)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.delete("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .sms \
            .messages.delete("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "body": "n",
            "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
            "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
            "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
            "direction": "outbound-api",
            "from": "+141586753093",
            "price": "-0.03000",
            "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "sent",
            "to": "+141586753096",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "body": "n",
            "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
            "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
            "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
            "direction": "outbound-api",
            "from": "+141586753093",
            "price": "-0.03000",
            "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "sent",
            "to": "+141586753096",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.get("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.body)
        self.assertEqual(u"n", instance.body)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:42 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_sent)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:44 +0000"), instance.date_sent)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:44 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.direction)
        self.assertEqual(u"outbound-api", instance.direction)
        self.assertIsNotNone(instance.from_)
        self.assertEqual(u"+141586753093", instance.from_)
        self.assertIsNotNone(instance.price)
        self.assertEqual(u"-0.03000", instance.price)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"sent", instance.status)
        self.assertIsNotNone(instance.to)
        self.assertEqual(u"+141586753096", instance.to)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=119771",
            "next_page_uri": null,
            "num_pages": 119772,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "sms_messages": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "body": "O Slash: \u00d8, PoP: \ud83d\udca9",
                    "date_created": "Fri, 04 Sep 2015 22:54:39 +0000",
                    "date_sent": "Fri, 04 Sep 2015 22:54:41 +0000",
                    "date_updated": "Fri, 04 Sep 2015 22:54:41 +0000",
                    "direction": "outbound-api",
                    "from": "+14155552345",
                    "num_segments": "1",
                    "price": "-0.00750",
                    "price_unit": "USD",
                    "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "sent",
                    "to": "+14155552345",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "start": 0,
            "total": 119772,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.list(
                to="+123456789",
                from_="+987654321",
                date_sent=datetime(2008, 1, 2, 0, 0),
                date_sent_before=datetime(2008, 1, 1, 0, 0),
                date_sent_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].body)
        self.assertEqual(u"O Slash: Ø, PoP: 💩", instances[0].body)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Fri, 04 Sep 2015 22:54:39 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_sent)
        self.assertEqual(parse_iso_date("Fri, 04 Sep 2015 22:54:41 +0000"), instances[0].date_sent)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Fri, 04 Sep 2015 22:54:41 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].direction)
        self.assertEqual(u"outbound-api", instances[0].direction)
        self.assertIsNotNone(instances[0].from_)
        self.assertEqual(u"+14155552345", instances[0].from_)
        self.assertIsNotNone(instances[0].num_segments)
        self.assertEqual(u"1", instances[0].num_segments)
        self.assertIsNotNone(instances[0].price)
        self.assertEqual(u"-0.00750", instances[0].price)
        self.assertIsNotNone(instances[0].price_unit)
        self.assertEqual(u"USD", instances[0].price_unit)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].status)
        self.assertEqual(u"sent", instances[0].status)
        self.assertIsNotNone(instances[0].to)
        self.assertEqual(u"+14155552345", instances[0].to)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=119771",
            "next_page_uri": null,
            "num_pages": 119772,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "sms_messages": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "body": "O Slash: \u00d8, PoP: \ud83d\udca9",
                    "date_created": "Fri, 04 Sep 2015 22:54:39 +0000",
                    "date_sent": "Fri, 04 Sep 2015 22:54:41 +0000",
                    "date_updated": "Fri, 04 Sep 2015 22:54:41 +0000",
                    "direction": "outbound-api",
                    "from": "+14155552345",
                    "num_segments": "1",
                    "price": "-0.00750",
                    "price_unit": "USD",
                    "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "sent",
                    "to": "+14155552345",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "start": 0,
            "total": 119772,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.list(
                to="+123456789",
                from_="+987654321",
                date_sent=datetime(2008, 1, 2, 0, 0),
                date_sent_before=datetime(2008, 1, 1, 0, 0),
                date_sent_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "DateSent": "2008-01-02",
                "DateSent<": "2008-01-01",
                "DateSent>": "2008-01-03",
                "From": "+987654321",
                "To": "+123456789"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=119771",
            "next_page_uri": null,
            "num_pages": 119772,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "sms_messages": [],
            "start": 0,
            "total": 119772,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.list(
                to="+123456789",
                from_="+987654321",
                date_sent=datetime(2008, 1, 2, 0, 0),
                date_sent_before=datetime(2008, 1, 1, 0, 0),
                date_sent_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=119771",
            "next_page_uri": null,
            "num_pages": 119772,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "sms_messages": [],
            "start": 0,
            "total": 119772,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.list(
                to="+123456789",
                from_="+987654321",
                date_sent=datetime(2008, 1, 2, 0, 0),
                date_sent_before=datetime(2008, 1, 1, 0, 0),
                date_sent_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "DateSent": "2008-01-02",
                "DateSent<": "2008-01-01",
                "DateSent>": "2008-01-03",
                "From": "+987654321",
                "To": "+123456789"
            },
        )

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "body": "n",
            "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
            "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
            "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
            "direction": "outbound-api",
            "from": "+141586753093",
            "price": "-0.03000",
            "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "sent",
            "to": "+141586753096",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.update(
                "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                body="body"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "Body": "body"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "body": "n",
            "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
            "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
            "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
            "direction": "outbound-api",
            "from": "+141586753093",
            "price": "-0.03000",
            "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "status": "sent",
            "to": "+141586753096",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .messages.update(
                "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                body="body"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.body)
        self.assertEqual(u"n", instance.body)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:42 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_sent)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:44 +0000"), instance.date_sent)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Mon, 26 Jul 2010 21:46:44 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.direction)
        self.assertEqual(u"outbound-api", instance.direction)
        self.assertIsNotNone(instance.from_)
        self.assertEqual(u"+141586753093", instance.from_)
        self.assertIsNotNone(instance.price)
        self.assertEqual(u"-0.03000", instance.price)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.status)
        self.assertEqual(u"sent", instance.status)
        self.assertIsNotNone(instance.to)
        self.assertEqual(u"+141586753096", instance.to)
