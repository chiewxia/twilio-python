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


class DomainIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "domains": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "auth_type": "",
                    "date_created": "Fri, 06 Sep 2013 18:48:50 -0000",
                    "date_updated": "Fri, 06 Sep 2013 18:48:50 -0000",
                    "domain_name": "dunder-mifflin-scranton.api.twilio.com",
                    "friendly_name": "Scranton Office",
                    "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "subresource_uris": {
                        "credential_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialListMappings.json",
                        "ip_access_control_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlListMappings.json"
                    },
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "voice_fallback_method": "POST",
                    "voice_fallback_url": null,
                    "voice_method": "POST",
                    "voice_status_callback_method": "POST",
                    "voice_status_callback_url": null,
                    "voice_url": "https://dundermifflin.example.com/twilio/app.php"
                }
            ],
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].auth_type)
        self.assertEqual(u"", instances[0].auth_type)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Fri, 06 Sep 2013 18:48:50 -0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Fri, 06 Sep 2013 18:48:50 -0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].domain_name)
        self.assertEqual(u"dunder-mifflin-scranton.api.twilio.com", instances[0].domain_name)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"Scranton Office", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].voice_fallback_method)
        self.assertEqual(u"POST", instances[0].voice_fallback_method)
        self.assertIsNone(instances[0].voice_fallback_url)
        self.assertIsNotNone(instances[0].voice_method)
        self.assertEqual(u"POST", instances[0].voice_method)
        self.assertIsNotNone(instances[0].voice_status_callback_method)
        self.assertEqual(u"POST", instances[0].voice_status_callback_method)
        self.assertIsNone(instances[0].voice_status_callback_url)
        self.assertIsNotNone(instances[0].voice_url)
        self.assertEqual(u"https://dundermifflin.example.com/twilio/app.php", instances[0].voice_url)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "domains": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "auth_type": "",
                    "date_created": "Fri, 06 Sep 2013 18:48:50 -0000",
                    "date_updated": "Fri, 06 Sep 2013 18:48:50 -0000",
                    "domain_name": "dunder-mifflin-scranton.api.twilio.com",
                    "friendly_name": "Scranton Office",
                    "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "subresource_uris": {
                        "credential_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialListMappings.json",
                        "ip_access_control_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlListMappings.json"
                    },
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "voice_fallback_method": "POST",
                    "voice_fallback_url": null,
                    "voice_method": "POST",
                    "voice_status_callback_method": "POST",
                    "voice_status_callback_url": null,
                    "voice_url": "https://dundermifflin.example.com/twilio/app.php"
                }
            ],
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "domains": [],
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "domains": [],
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "auth_type": "IP_ACL",
            "date_created": "Fri, 06 Sep 2013 19:18:30 -0000",
            "date_updated": "Fri, 06 Sep 2013 19:18:30 -0000",
            "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
            "friendly_name": "Scranton Office",
            "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "subresource_uris": {
                "credential_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialListMappings.json",
                "ip_access_control_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlListMappings.json"
            },
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_fallback_method": "POST",
            "voice_fallback_url": null,
            "voice_method": "POST",
            "voice_status_callback_method": "POST",
            "voice_status_callback_url": null,
            "voice_url": "https://dundermifflin.example.com/twilio/app.php"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.create(
                "domain_name",
                friendly_name="friendly_name",
                voice_url="https://example.com",
                voice_method="GET",
                voice_fallback_url="https://example.com",
                voice_fallback_method="GET",
                voice_status_callback_url="https://example.com",
                voice_status_callback_method="GET"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "DomainName": "domain_name",
                "FriendlyName": "friendly_name",
                "VoiceFallbackMethod": "GET",
                "VoiceFallbackUrl": "https://example.com",
                "VoiceMethod": "GET",
                "VoiceStatusCallbackMethod": "GET",
                "VoiceStatusCallbackUrl": "https://example.com",
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
            "auth_type": "IP_ACL",
            "date_created": "Fri, 06 Sep 2013 19:18:30 -0000",
            "date_updated": "Fri, 06 Sep 2013 19:18:30 -0000",
            "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
            "friendly_name": "Scranton Office",
            "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "subresource_uris": {
                "credential_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialListMappings.json",
                "ip_access_control_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlListMappings.json"
            },
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_fallback_method": "POST",
            "voice_fallback_url": null,
            "voice_method": "POST",
            "voice_status_callback_method": "POST",
            "voice_status_callback_url": null,
            "voice_url": "https://dundermifflin.example.com/twilio/app.php"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.create(
                "domain_name",
                friendly_name="friendly_name",
                voice_url="https://example.com",
                voice_method="GET",
                voice_fallback_url="https://example.com",
                voice_fallback_method="GET",
                voice_status_callback_url="https://example.com",
                voice_status_callback_method="GET"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.auth_type)
        self.assertEqual(u"IP_ACL", instance.auth_type)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 06 Sep 2013 19:18:30 -0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 06 Sep 2013 19:18:30 -0000"), instance.date_updated)
        self.assertIsNotNone(instance.domain_name)
        self.assertEqual(u"dunder-mifflin-scranton.sip.twilio.com", instance.domain_name)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Scranton Office", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.voice_fallback_method)
        self.assertEqual(u"POST", instance.voice_fallback_method)
        self.assertIsNone(instance.voice_fallback_url)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"POST", instance.voice_method)
        self.assertIsNotNone(instance.voice_status_callback_method)
        self.assertEqual(u"POST", instance.voice_status_callback_method)
        self.assertIsNone(instance.voice_status_callback_url)
        self.assertIsNotNone(instance.voice_url)
        self.assertEqual(u"https://dundermifflin.example.com/twilio/app.php", instance.voice_url)

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "auth_type": "IP_ACL",
            "date_created": "Fri, 06 Sep 2013 19:18:30 -0000",
            "date_updated": "Fri, 06 Sep 2013 19:18:30 -0000",
            "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
            "friendly_name": "Scranton Office",
            "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "subresource_uris": {
                "credential_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialListMappings.json",
                "ip_access_control_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlListMappings.json"
            },
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_fallback_method": "POST",
            "voice_fallback_url": null,
            "voice_method": "POST",
            "voice_status_callback_method": "POST",
            "voice_status_callback_url": null,
            "voice_url": "https://dundermifflin.example.com/twilio/app.php"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.get("SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "auth_type": "IP_ACL",
            "date_created": "Fri, 06 Sep 2013 19:18:30 -0000",
            "date_updated": "Fri, 06 Sep 2013 19:18:30 -0000",
            "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
            "friendly_name": "Scranton Office",
            "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "subresource_uris": {
                "credential_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialListMappings.json",
                "ip_access_control_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlListMappings.json"
            },
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_fallback_method": "POST",
            "voice_fallback_url": null,
            "voice_method": "POST",
            "voice_status_callback_method": "POST",
            "voice_status_callback_url": null,
            "voice_url": "https://dundermifflin.example.com/twilio/app.php"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.get("SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.auth_type)
        self.assertEqual(u"IP_ACL", instance.auth_type)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 06 Sep 2013 19:18:30 -0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 06 Sep 2013 19:18:30 -0000"), instance.date_updated)
        self.assertIsNotNone(instance.domain_name)
        self.assertEqual(u"dunder-mifflin-scranton.sip.twilio.com", instance.domain_name)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Scranton Office", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.voice_fallback_method)
        self.assertEqual(u"POST", instance.voice_fallback_method)
        self.assertIsNone(instance.voice_fallback_url)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"POST", instance.voice_method)
        self.assertIsNotNone(instance.voice_status_callback_method)
        self.assertEqual(u"POST", instance.voice_status_callback_method)
        self.assertIsNone(instance.voice_status_callback_url)
        self.assertIsNotNone(instance.voice_url)
        self.assertEqual(u"https://dundermifflin.example.com/twilio/app.php", instance.voice_url)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2010-04-01",
            "auth_type": "IP_ACL",
            "date_created": "Fri, 06 Sep 2013 19:18:30 -0000",
            "date_updated": "Fri, 06 Sep 2013 19:18:30 -0000",
            "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
            "friendly_name": "Scranton Office",
            "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "subresource_uris": {
                "credential_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialListMappings.json",
                "ip_access_control_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlListMappings.json"
            },
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_fallback_method": "POST",
            "voice_fallback_url": null,
            "voice_method": "POST",
            "voice_status_callback_method": "POST",
            "voice_status_callback_url": null,
            "voice_url": "https://dundermifflin.example.com/twilio/app.php"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.update(
                "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                api_version="api_version",
                friendly_name="friendly_name",
                voice_fallback_method="GET",
                voice_fallback_url="https://example.com",
                voice_method="GET",
                voice_status_callback_method="GET",
                voice_status_callback_url="https://example.com",
                voice_url="https://example.com"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ApiVersion": "api_version",
                "FriendlyName": "friendly_name",
                "VoiceFallbackMethod": "GET",
                "VoiceFallbackUrl": "https://example.com",
                "VoiceMethod": "GET",
                "VoiceStatusCallbackMethod": "GET",
                "VoiceStatusCallbackUrl": "https://example.com",
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
            "auth_type": "IP_ACL",
            "date_created": "Fri, 06 Sep 2013 19:18:30 -0000",
            "date_updated": "Fri, 06 Sep 2013 19:18:30 -0000",
            "domain_name": "dunder-mifflin-scranton.sip.twilio.com",
            "friendly_name": "Scranton Office",
            "sid": "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "subresource_uris": {
                "credential_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialListMappings.json",
                "ip_access_control_list_mappings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlListMappings.json"
            },
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_fallback_method": "POST",
            "voice_fallback_url": null,
            "voice_method": "POST",
            "voice_status_callback_method": "POST",
            "voice_status_callback_url": null,
            "voice_url": "https://dundermifflin.example.com/twilio/app.php"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.update(
                "SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                api_version="api_version",
                friendly_name="friendly_name",
                voice_fallback_method="GET",
                voice_fallback_url="https://example.com",
                voice_method="GET",
                voice_status_callback_method="GET",
                voice_status_callback_url="https://example.com",
                voice_url="https://example.com"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.auth_type)
        self.assertEqual(u"IP_ACL", instance.auth_type)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 06 Sep 2013 19:18:30 -0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 06 Sep 2013 19:18:30 -0000"), instance.date_updated)
        self.assertIsNotNone(instance.domain_name)
        self.assertEqual(u"dunder-mifflin-scranton.sip.twilio.com", instance.domain_name)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Scranton Office", instance.friendly_name)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.voice_fallback_method)
        self.assertEqual(u"POST", instance.voice_fallback_method)
        self.assertIsNone(instance.voice_fallback_url)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"POST", instance.voice_method)
        self.assertIsNotNone(instance.voice_status_callback_method)
        self.assertEqual(u"POST", instance.voice_status_callback_method)
        self.assertIsNone(instance.voice_status_callback_url)
        self.assertIsNotNone(instance.voice_url)
        self.assertEqual(u"https://dundermifflin.example.com/twilio/app.php", instance.voice_url)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .domains.delete("SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .sip \
            .domains.delete("SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())
