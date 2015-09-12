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


class CredentialIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "credentials": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "credential_list_sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Wed, 19 Aug 2015 19:48:45 +0000",
                    "date_updated": "Wed, 19 Aug 2015 19:48:45 +0000",
                    "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "username": "1440013725.28"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].credential_list_sid)
        self.assertEqual(u"CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].credential_list_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Wed, 19 Aug 2015 19:48:45 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Wed, 19 Aug 2015 19:48:45 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].username)
        self.assertEqual(u"1440013725.28", instances[0].username)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "credentials": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "credential_list_sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Wed, 19 Aug 2015 19:48:45 +0000",
                    "date_updated": "Wed, 19 Aug 2015 19:48:45 +0000",
                    "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "username": "1440013725.28"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "credentials": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "credentials": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json",
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
            "credential_list_sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Wed, 19 Aug 2015 19:48:45 +0000",
            "date_updated": "Wed, 19 Aug 2015 19:48:45 +0000",
            "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "username": "1440013725.28"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.create(
                "username",
                "password"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "Password": "password",
                "Username": "username"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "credential_list_sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Wed, 19 Aug 2015 19:48:45 +0000",
            "date_updated": "Wed, 19 Aug 2015 19:48:45 +0000",
            "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "username": "1440013725.28"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.create(
                "username",
                "password"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.credential_list_sid)
        self.assertEqual(u"CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.credential_list_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Wed, 19 Aug 2015 19:48:45 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Wed, 19 Aug 2015 19:48:45 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.username)
        self.assertEqual(u"1440013725.28", instance.username)

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "credential_list_sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Wed, 19 Aug 2015 19:48:45 +0000",
            "date_updated": "Wed, 19 Aug 2015 19:48:45 +0000",
            "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "username": "1440013725.28"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.get("CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "credential_list_sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Wed, 19 Aug 2015 19:48:45 +0000",
            "date_updated": "Wed, 19 Aug 2015 19:48:45 +0000",
            "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "username": "1440013725.28"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.get("CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.credential_list_sid)
        self.assertEqual(u"CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.credential_list_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Wed, 19 Aug 2015 19:48:45 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Wed, 19 Aug 2015 19:48:45 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.username)
        self.assertEqual(u"1440013725.28", instance.username)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "credential_list_sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Wed, 19 Aug 2015 19:48:45 +0000",
            "date_updated": "Wed, 19 Aug 2015 19:48:45 +0000",
            "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "username": "1440013725.28"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.update(
                "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "username",
                "password"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "Password": "password",
                "Username": "username"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "credential_list_sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Wed, 19 Aug 2015 19:48:45 +0000",
            "date_updated": "Wed, 19 Aug 2015 19:48:45 +0000",
            "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "username": "1440013725.28"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.update(
                "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "username",
                "password"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.credential_list_sid)
        self.assertEqual(u"CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.credential_list_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Wed, 19 Aug 2015 19:48:45 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Wed, 19 Aug 2015 19:48:45 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.username)
        self.assertEqual(u"1440013725.28", instance.username)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sip \
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.delete("CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .credential_lists.get("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .credentials.delete("CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())
