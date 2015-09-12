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
from twilio.rest.pricing.client import PricingClient
from twilio.rest.http import Response


class NumberIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = PricingClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "country": "United States",
            "inbound_call_price": {
                "base_price": null,
                "current_price": null,
                "number_type": null
            },
            "iso_country": "US",
            "number": "+987654321",
            "outbound_call_price": {
                "base_price": "0.015",
                "current_price": "0.015"
            },
            "price_unit": "USD",
            "url": "https://pricing.twilio.com/v1/Voice/Numbers/+987654321"
        }
        """))
        
        query = client \
            .voice \
            .numbers.get("+987654321")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://pricing.twilio.com/v1/Voice/Numbers/+987654321",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = PricingClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "country": "United States",
            "inbound_call_price": {
                "base_price": null,
                "current_price": null,
                "number_type": null
            },
            "iso_country": "US",
            "number": "+987654321",
            "outbound_call_price": {
                "base_price": "0.015",
                "current_price": "0.015"
            },
            "price_unit": "USD",
            "url": "https://pricing.twilio.com/v1/Voice/Numbers/+987654321"
        }
        """))
        
        query = client \
            .voice \
            .numbers.get("+987654321")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.country)
        self.assertEqual(u"United States", instance.country)
        self.assertIsNotNone(instance.iso_country)
        self.assertEqual(u"US", instance.iso_country)
        self.assertIsNotNone(instance.number)
        self.assertEqual(u"+987654321", instance.number)
        self.assertIsNotNone(instance.price_unit)
        self.assertEqual(u"USD", instance.price_unit)
