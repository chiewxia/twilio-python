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


class TriggerIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "callback_method": "GET",
            "callback_url": "http://cap.com/streetfight",
            "current_value": "0",
            "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",
            "date_fired": null,
            "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",
            "friendly_name": "raphael-cluster-1441544325.86",
            "recurring": "yearly",
            "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "trigger_by": "price",
            "trigger_value": "50",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "usage_category": "totalprice",
            "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.get("UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "callback_method": "GET",
            "callback_url": "http://cap.com/streetfight",
            "current_value": "0",
            "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",
            "date_fired": null,
            "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",
            "friendly_name": "raphael-cluster-1441544325.86",
            "recurring": "yearly",
            "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "trigger_by": "price",
            "trigger_value": "50",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "usage_category": "totalprice",
            "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.get("UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.callback_method)
        self.assertEqual(u"GET", instance.callback_method)
        self.assertIsNotNone(instance.callback_url)
        self.assertEqual(u"http://cap.com/streetfight", instance.callback_url)
        self.assertIsNotNone(instance.current_value)
        self.assertEqual(u"0", instance.current_value)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 06 Sep 2015 12:58:45 +0000"), instance.date_created)
        self.assertIsNone(instance.date_fired)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Sun, 06 Sep 2015 12:58:45 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"raphael-cluster-1441544325.86", instance.friendly_name)
        self.assertIsNotNone(instance.recurring)
        self.assertEqual(u"yearly", instance.recurring)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.trigger_by)
        self.assertEqual(u"price", instance.trigger_by)
        self.assertIsNotNone(instance.trigger_value)
        self.assertEqual(u"50", instance.trigger_value)
        self.assertIsNotNone(instance.usage_category)
        self.assertEqual(u"totalprice", instance.usage_category)
        self.assertIsNotNone(instance.usage_record_uri)
        self.assertEqual(u"/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice", instance.usage_record_uri)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "callback_method": "GET",
            "callback_url": "http://cap.com/streetfight",
            "current_value": "0",
            "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",
            "date_fired": null,
            "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",
            "friendly_name": "raphael-cluster-1441544325.86",
            "recurring": "yearly",
            "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "trigger_by": "price",
            "trigger_value": "50",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "usage_category": "totalprice",
            "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.update(
                "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                callback_method="GET",
                callback_url="https://example.com",
                friendly_name="friendly_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "CallbackMethod": "GET",
                "CallbackUrl": "https://example.com",
                "FriendlyName": "friendly_name"
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
            "callback_method": "GET",
            "callback_url": "http://cap.com/streetfight",
            "current_value": "0",
            "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",
            "date_fired": null,
            "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",
            "friendly_name": "raphael-cluster-1441544325.86",
            "recurring": "yearly",
            "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "trigger_by": "price",
            "trigger_value": "50",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "usage_category": "totalprice",
            "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.update(
                "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                callback_method="GET",
                callback_url="https://example.com",
                friendly_name="friendly_name"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.callback_method)
        self.assertEqual(u"GET", instance.callback_method)
        self.assertIsNotNone(instance.callback_url)
        self.assertEqual(u"http://cap.com/streetfight", instance.callback_url)
        self.assertIsNotNone(instance.current_value)
        self.assertEqual(u"0", instance.current_value)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 06 Sep 2015 12:58:45 +0000"), instance.date_created)
        self.assertIsNone(instance.date_fired)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Sun, 06 Sep 2015 12:58:45 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"raphael-cluster-1441544325.86", instance.friendly_name)
        self.assertIsNotNone(instance.recurring)
        self.assertEqual(u"yearly", instance.recurring)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.trigger_by)
        self.assertEqual(u"price", instance.trigger_by)
        self.assertIsNotNone(instance.trigger_value)
        self.assertEqual(u"50", instance.trigger_value)
        self.assertIsNotNone(instance.usage_category)
        self.assertEqual(u"totalprice", instance.usage_category)
        self.assertIsNotNone(instance.usage_record_uri)
        self.assertEqual(u"/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice", instance.usage_record_uri)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.delete("UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .usage \
            .triggers.delete("UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "callback_method": "GET",
            "callback_url": "http://cap.com/streetfight",
            "current_value": "0",
            "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",
            "date_fired": null,
            "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",
            "friendly_name": "raphael-cluster-1441544325.86",
            "recurring": "yearly",
            "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "trigger_by": "price",
            "trigger_value": "50",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "usage_category": "totalprice",
            "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.create(
                "https://example.com",
                "trigger_value",
                "calleridlookups",
                callback_method="GET",
                friendly_name="friendly_name",
                recurring="daily",
                trigger_by="count"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "CallbackMethod": "GET",
                "CallbackUrl": "https://example.com",
                "FriendlyName": "friendly_name",
                "Recurring": "daily",
                "TriggerBy": "count",
                "TriggerValue": "trigger_value",
                "UsageCategory": "calleridlookups"
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
            "callback_method": "GET",
            "callback_url": "http://cap.com/streetfight",
            "current_value": "0",
            "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",
            "date_fired": null,
            "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",
            "friendly_name": "raphael-cluster-1441544325.86",
            "recurring": "yearly",
            "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "trigger_by": "price",
            "trigger_value": "50",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "usage_category": "totalprice",
            "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.create(
                "https://example.com",
                "trigger_value",
                "calleridlookups",
                callback_method="GET",
                friendly_name="friendly_name",
                recurring="daily",
                trigger_by="count"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.callback_method)
        self.assertEqual(u"GET", instance.callback_method)
        self.assertIsNotNone(instance.callback_url)
        self.assertEqual(u"http://cap.com/streetfight", instance.callback_url)
        self.assertIsNotNone(instance.current_value)
        self.assertEqual(u"0", instance.current_value)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 06 Sep 2015 12:58:45 +0000"), instance.date_created)
        self.assertIsNone(instance.date_fired)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Sun, 06 Sep 2015 12:58:45 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"raphael-cluster-1441544325.86", instance.friendly_name)
        self.assertIsNotNone(instance.recurring)
        self.assertEqual(u"yearly", instance.recurring)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.trigger_by)
        self.assertEqual(u"price", instance.trigger_by)
        self.assertIsNotNone(instance.trigger_value)
        self.assertEqual(u"50", instance.trigger_value)
        self.assertIsNotNone(instance.usage_category)
        self.assertEqual(u"totalprice", instance.usage_category)
        self.assertIsNotNone(instance.usage_record_uri)
        self.assertEqual(u"/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice", instance.usage_record_uri)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers?PageSize=1&Page=626",
            "next_page_uri": null,
            "num_pages": 627,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 627,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers",
            "usage_triggers": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "callback_method": "GET",
                    "callback_url": "http://cap.com/streetfight",
                    "current_value": "0",
                    "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",
                    "date_fired": null,
                    "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",
                    "friendly_name": "raphael-cluster-1441544325.86",
                    "recurring": "yearly",
                    "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "trigger_by": "price",
                    "trigger_value": "50",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "usage_category": "totalprice",
                    "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice"
                }
            ]
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.list(
                recurring="daily",
                trigger_by="count",
                usage_category="calleridlookups"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].callback_method)
        self.assertEqual(u"GET", instances[0].callback_method)
        self.assertIsNotNone(instances[0].callback_url)
        self.assertEqual(u"http://cap.com/streetfight", instances[0].callback_url)
        self.assertIsNotNone(instances[0].current_value)
        self.assertEqual(u"0", instances[0].current_value)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Sun, 06 Sep 2015 12:58:45 +0000"), instances[0].date_created)
        self.assertIsNone(instances[0].date_fired)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Sun, 06 Sep 2015 12:58:45 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"raphael-cluster-1441544325.86", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].recurring)
        self.assertEqual(u"yearly", instances[0].recurring)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].trigger_by)
        self.assertEqual(u"price", instances[0].trigger_by)
        self.assertIsNotNone(instances[0].trigger_value)
        self.assertEqual(u"50", instances[0].trigger_value)
        self.assertIsNotNone(instances[0].usage_category)
        self.assertEqual(u"totalprice", instances[0].usage_category)
        self.assertIsNotNone(instances[0].usage_record_uri)
        self.assertEqual(u"/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice", instances[0].usage_record_uri)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers?PageSize=1&Page=626",
            "next_page_uri": null,
            "num_pages": 627,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 627,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers",
            "usage_triggers": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "callback_method": "GET",
                    "callback_url": "http://cap.com/streetfight",
                    "current_value": "0",
                    "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",
                    "date_fired": null,
                    "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",
                    "friendly_name": "raphael-cluster-1441544325.86",
                    "recurring": "yearly",
                    "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "trigger_by": "price",
                    "trigger_value": "50",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "usage_category": "totalprice",
                    "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice"
                }
            ]
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.list(
                recurring="daily",
                trigger_by="count",
                usage_category="calleridlookups"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Recurring": "daily",
                "TriggerBy": "count",
                "UsageCategory": "calleridlookups"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers?PageSize=1&Page=626",
            "next_page_uri": null,
            "num_pages": 627,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 627,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers",
            "usage_triggers": []
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.list(
                recurring="daily",
                trigger_by="count",
                usage_category="calleridlookups"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers?PageSize=1&Page=626",
            "next_page_uri": null,
            "num_pages": 627,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 627,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers",
            "usage_triggers": []
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .triggers.list(
                recurring="daily",
                trigger_by="count",
                usage_category="calleridlookups"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Recurring": "daily",
                "TriggerBy": "count",
                "UsageCategory": "calleridlookups"
            },
        )
