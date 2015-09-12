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


class ShortCodeIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "date_created": null,
            "date_updated": null,
            "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",
            "short_code": "99990",
            "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "POST",
            "sms_fallback_url": null,
            "sms_method": "POST",
            "sms_url": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .short_codes.get("SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "date_created": null,
            "date_updated": null,
            "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",
            "short_code": "99990",
            "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "POST",
            "sms_fallback_url": null,
            "sms_method": "POST",
            "sms_url": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .short_codes.get("SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNone(instance.date_created)
        self.assertIsNone(instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"API_CLUSTER_TEST_SHORT_CODE", instance.friendly_name)
        self.assertIsNotNone(instance.short_code)
        self.assertEqual(u"99990", instance.short_code)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.sms_fallback_method)
        self.assertEqual(u"POST", instance.sms_fallback_method)
        self.assertIsNone(instance.sms_fallback_url)
        self.assertIsNotNone(instance.sms_method)
        self.assertEqual(u"POST", instance.sms_method)
        self.assertIsNone(instance.sms_url)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "date_created": null,
            "date_updated": null,
            "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",
            "short_code": "99990",
            "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "POST",
            "sms_fallback_url": null,
            "sms_method": "POST",
            "sms_url": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .short_codes.update(
                "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                api_version="api_version",
                sms_url="https://example.com",
                sms_method="GET",
                sms_fallback_url="https://example.com",
                sms_fallback_method="GET"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ApiVersion": "api_version",
                "FriendlyName": "friendly_name",
                "SmsFallbackMethod": "GET",
                "SmsFallbackUrl": "https://example.com",
                "SmsMethod": "GET",
                "SmsUrl": "https://example.com"
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
            "date_created": null,
            "date_updated": null,
            "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",
            "short_code": "99990",
            "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_fallback_method": "POST",
            "sms_fallback_url": null,
            "sms_method": "POST",
            "sms_url": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .short_codes.update(
                "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                api_version="api_version",
                sms_url="https://example.com",
                sms_method="GET",
                sms_fallback_url="https://example.com",
                sms_fallback_method="GET"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNone(instance.date_created)
        self.assertIsNone(instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"API_CLUSTER_TEST_SHORT_CODE", instance.friendly_name)
        self.assertIsNotNone(instance.short_code)
        self.assertEqual(u"99990", instance.short_code)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.sms_fallback_method)
        self.assertEqual(u"POST", instance.sms_fallback_method)
        self.assertIsNone(instance.sms_fallback_url)
        self.assertIsNotNone(instance.sms_method)
        self.assertEqual(u"POST", instance.sms_method)
        self.assertIsNone(instance.sms_url)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "short_codes": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "date_created": null,
                    "date_updated": null,
                    "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",
                    "short_code": "99990",
                    "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sms_fallback_method": "POST",
                    "sms_fallback_url": null,
                    "sms_method": "POST",
                    "sms_url": null,
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .short_codes.list(
                friendly_name="friendly_name",
                short_code="short_code"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNone(instances[0].date_created)
        self.assertIsNone(instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"API_CLUSTER_TEST_SHORT_CODE", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].short_code)
        self.assertEqual(u"99990", instances[0].short_code)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].sms_fallback_method)
        self.assertEqual(u"POST", instances[0].sms_fallback_method)
        self.assertIsNone(instances[0].sms_fallback_url)
        self.assertIsNotNone(instances[0].sms_method)
        self.assertEqual(u"POST", instances[0].sms_method)
        self.assertIsNone(instances[0].sms_url)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "short_codes": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "date_created": null,
                    "date_updated": null,
                    "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",
                    "short_code": "99990",
                    "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sms_fallback_method": "POST",
                    "sms_fallback_url": null,
                    "sms_method": "POST",
                    "sms_url": null,
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .short_codes.list(
                friendly_name="friendly_name",
                short_code="short_code"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name",
                "ShortCode": "short_code"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "short_codes": [],
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .short_codes.list(
                friendly_name="friendly_name",
                short_code="short_code"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "short_codes": [],
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sms \
            .short_codes.list(
                friendly_name="friendly_name",
                short_code="short_code"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "FriendlyName": "friendly_name",
                "ShortCode": "short_code"
            },
        )
