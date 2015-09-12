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
from twilio.ext.holodeck import Holodeck
from twilio.rest.v2010.client import V2010Client
from twilio.rest.http import Response


class LocalIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "available_phone_numbers": [
                {
                    "address_requirements": "none",
                    "beta": false,
                    "capabilities": {
                        "MMS": true,
                        "SMS": false,
                        "voice": true
                    },
                    "friendly_name": "(808) 925-1571",
                    "iso_country": "US",
                    "lata": "834",
                    "latitude": "19.720000",
                    "longitude": "-155.090000",
                    "phone_number": "+18089251571",
                    "postal_code": "96720",
                    "rate_center": "HILO",
                    "region": "HI"
                }
            ],
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .available_phone_numbers.get("US") \
            .local.list(beta=True)
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].address_requirements)
        self.assertEqual(u"none", instances[0].address_requirements)
        self.assertIsNotNone(instances[0].beta)
        self.assertEqual(False, instances[0].beta)
        self.assertIsNotNone(instances[0].capabilities)
        self.assertEqual({
            "MMS": True,
            "SMS": False,
            "voice": True
        }, instances[0].capabilities)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"(808) 925-1571", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].iso_country)
        self.assertEqual(u"US", instances[0].iso_country)
        self.assertIsNotNone(instances[0].lata)
        self.assertEqual(u"834", instances[0].lata)
        self.assertIsNotNone(instances[0].latitude)
        self.assertEqual(u"19.720000", instances[0].latitude)
        self.assertIsNotNone(instances[0].longitude)
        self.assertEqual(u"-155.090000", instances[0].longitude)
        self.assertIsNotNone(instances[0].phone_number)
        self.assertEqual(u"+18089251571", instances[0].phone_number)
        self.assertIsNotNone(instances[0].postal_code)
        self.assertEqual(u"96720", instances[0].postal_code)
        self.assertIsNotNone(instances[0].rate_center)
        self.assertEqual(u"HILO", instances[0].rate_center)
        self.assertIsNotNone(instances[0].region)
        self.assertEqual(u"HI", instances[0].region)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "available_phone_numbers": [
                {
                    "address_requirements": "none",
                    "beta": false,
                    "capabilities": {
                        "MMS": true,
                        "SMS": false,
                        "voice": true
                    },
                    "friendly_name": "(808) 925-1571",
                    "iso_country": "US",
                    "lata": "834",
                    "latitude": "19.720000",
                    "longitude": "-155.090000",
                    "phone_number": "+18089251571",
                    "postal_code": "96720",
                    "rate_center": "HILO",
                    "region": "HI"
                }
            ],
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .available_phone_numbers.get("US") \
            .local.list(beta=True)
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Beta": "true"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "available_phone_numbers": [],
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .available_phone_numbers.get("US") \
            .local.list(beta=True)
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "available_phone_numbers": [],
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .available_phone_numbers.get("US") \
            .local.list(beta=True)
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Beta": "true"
            },
        )
