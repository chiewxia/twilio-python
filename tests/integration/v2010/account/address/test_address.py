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


class AddressIntegrationTest(unittest.TestCase):

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "city": "SF",
            "customer_name": "name",
            "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
            "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
            "friendly_name": null,
            "iso_country": "US",
            "postal_code": "94019",
            "region": "CA",
            "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "street": "4th",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.create(
                "customer_name",
                "street",
                "city",
                "region",
                "postal_code",
                "US",
                friendly_name="friendly_name"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "City": "city",
                "CustomerName": "customer_name",
                "FriendlyName": "friendly_name",
                "IsoCountry": "US",
                "PostalCode": "postal_code",
                "Region": "region",
                "Street": "street"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "city": "SF",
            "customer_name": "name",
            "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
            "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
            "friendly_name": null,
            "iso_country": "US",
            "postal_code": "94019",
            "region": "CA",
            "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "street": "4th",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.create(
                "customer_name",
                "street",
                "city",
                "region",
                "postal_code",
                "US",
                friendly_name="friendly_name"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.city)
        self.assertEqual(u"SF", instance.city)
        self.assertIsNotNone(instance.customer_name)
        self.assertEqual(u"name", instance.customer_name)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 17:07:30 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 17:07:30 +0000"), instance.date_updated)
        self.assertIsNone(instance.friendly_name)
        self.assertIsNotNone(instance.iso_country)
        self.assertEqual(u"US", instance.iso_country)
        self.assertIsNotNone(instance.postal_code)
        self.assertEqual(u"94019", instance.postal_code)
        self.assertIsNotNone(instance.region)
        self.assertEqual(u"CA", instance.region)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.street)
        self.assertEqual(u"4th", instance.street)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.delete("ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .addresses.delete("ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "city": "SF",
            "customer_name": "name",
            "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
            "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
            "friendly_name": null,
            "iso_country": "US",
            "postal_code": "94019",
            "region": "CA",
            "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "street": "4th",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.get("ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "city": "SF",
            "customer_name": "name",
            "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
            "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
            "friendly_name": null,
            "iso_country": "US",
            "postal_code": "94019",
            "region": "CA",
            "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "street": "4th",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.get("ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.city)
        self.assertEqual(u"SF", instance.city)
        self.assertIsNotNone(instance.customer_name)
        self.assertEqual(u"name", instance.customer_name)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 17:07:30 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 17:07:30 +0000"), instance.date_updated)
        self.assertIsNone(instance.friendly_name)
        self.assertIsNotNone(instance.iso_country)
        self.assertEqual(u"US", instance.iso_country)
        self.assertIsNotNone(instance.postal_code)
        self.assertEqual(u"94019", instance.postal_code)
        self.assertIsNotNone(instance.region)
        self.assertEqual(u"CA", instance.region)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.street)
        self.assertEqual(u"4th", instance.street)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "city": "SF",
            "customer_name": "name",
            "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
            "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
            "friendly_name": null,
            "iso_country": "US",
            "postal_code": "94019",
            "region": "CA",
            "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "street": "4th",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.update(
                "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                customer_name="customer_name",
                street="street",
                city="city",
                region="region",
                postal_code="postal_code"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "City": "city",
                "CustomerName": "customer_name",
                "FriendlyName": "friendly_name",
                "PostalCode": "postal_code",
                "Region": "region",
                "Street": "street"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "city": "SF",
            "customer_name": "name",
            "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
            "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
            "friendly_name": null,
            "iso_country": "US",
            "postal_code": "94019",
            "region": "CA",
            "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "street": "4th",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.update(
                "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                friendly_name="friendly_name",
                customer_name="customer_name",
                street="street",
                city="city",
                region="region",
                postal_code="postal_code"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.city)
        self.assertEqual(u"SF", instance.city)
        self.assertIsNotNone(instance.customer_name)
        self.assertEqual(u"name", instance.customer_name)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 17:07:30 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 17:07:30 +0000"), instance.date_updated)
        self.assertIsNone(instance.friendly_name)
        self.assertIsNotNone(instance.iso_country)
        self.assertEqual(u"US", instance.iso_country)
        self.assertIsNotNone(instance.postal_code)
        self.assertEqual(u"94019", instance.postal_code)
        self.assertIsNotNone(instance.region)
        self.assertEqual(u"CA", instance.region)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.street)
        self.assertEqual(u"4th", instance.street)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "addresses": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "city": "SF",
                    "customer_name": "name",
                    "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
                    "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
                    "friendly_name": null,
                    "iso_country": "US",
                    "postal_code": "94019",
                    "region": "CA",
                    "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "street": "4th",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.list(
                customer_name="customer_name",
                friendly_name="friendly_name",
                iso_country="US"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].city)
        self.assertEqual(u"SF", instances[0].city)
        self.assertIsNotNone(instances[0].customer_name)
        self.assertEqual(u"name", instances[0].customer_name)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 17:07:30 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 17:07:30 +0000"), instances[0].date_updated)
        self.assertIsNone(instances[0].friendly_name)
        self.assertIsNotNone(instances[0].iso_country)
        self.assertEqual(u"US", instances[0].iso_country)
        self.assertIsNotNone(instances[0].postal_code)
        self.assertEqual(u"94019", instances[0].postal_code)
        self.assertIsNotNone(instances[0].region)
        self.assertEqual(u"CA", instances[0].region)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].street)
        self.assertEqual(u"4th", instances[0].street)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "addresses": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "city": "SF",
                    "customer_name": "name",
                    "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
                    "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
                    "friendly_name": null,
                    "iso_country": "US",
                    "postal_code": "94019",
                    "region": "CA",
                    "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "street": "4th",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.list(
                customer_name="customer_name",
                friendly_name="friendly_name",
                iso_country="US"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "CustomerName": "customer_name",
                "FriendlyName": "friendly_name",
                "IsoCountry": "US"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "addresses": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.list(
                customer_name="customer_name",
                friendly_name="friendly_name",
                iso_country="US"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "addresses": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?PageSize=50&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.list(
                customer_name="customer_name",
                friendly_name="friendly_name",
                iso_country="US"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "CustomerName": "customer_name",
                "FriendlyName": "friendly_name",
                "IsoCountry": "US"
            },
        )
