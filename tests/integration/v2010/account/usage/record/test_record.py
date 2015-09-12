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


class RecordIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Page=0&PageSize=1",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Page=68&PageSize=1",
            "next_page_uri": null,
            "num_pages": 69,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 69,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records",
            "usage_records": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "category": "totalprice",
                    "count": null,
                    "count_unit": "",
                    "description": "Total Price",
                    "end_date": "2015-09-04",
                    "price": "2192.84855",
                    "price_unit": "usd",
                    "start_date": "2011-08-23",
                    "subresource_uris": {
                        "all_time": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/AllTime.json?Category=totalprice",
                        "daily": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=totalprice",
                        "last_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=totalprice",
                        "monthly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Monthly.json?Category=totalprice",
                        "this_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/ThisMonth.json?Category=totalprice",
                        "today": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=totalprice",
                        "yearly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yearly.json?Category=totalprice",
                        "yesterday": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yesterday.json?Category=totalprice"
                    },
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice&StartDate=2011-08-23&EndDate=2015-09-04",
                    "usage": "2192.84855",
                    "usage_unit": "usd"
                }
            ]
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .records.list(
                category="calleridlookups",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].category)
        self.assertEqual(u"totalprice", instances[0].category)
        self.assertIsNone(instances[0].count)
        self.assertIsNotNone(instances[0].count_unit)
        self.assertEqual(u"", instances[0].count_unit)
        self.assertIsNotNone(instances[0].description)
        self.assertEqual(u"Total Price", instances[0].description)
        self.assertIsNotNone(instances[0].end_date)
        self.assertEqual(parse_iso_date("2015-09-04"), instances[0].end_date)
        self.assertIsNotNone(instances[0].price)
        self.assertEqual(u"2192.84855", instances[0].price)
        self.assertIsNotNone(instances[0].price_unit)
        self.assertEqual(u"usd", instances[0].price_unit)
        self.assertIsNotNone(instances[0].start_date)
        self.assertEqual(parse_iso_date("2011-08-23"), instances[0].start_date)
        self.assertIsNotNone(instances[0].usage)
        self.assertEqual(u"2192.84855", instances[0].usage)
        self.assertIsNotNone(instances[0].usage_unit)
        self.assertEqual(u"usd", instances[0].usage_unit)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Page=0&PageSize=1",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Page=68&PageSize=1",
            "next_page_uri": null,
            "num_pages": 69,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 69,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records",
            "usage_records": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2010-04-01",
                    "category": "totalprice",
                    "count": null,
                    "count_unit": "",
                    "description": "Total Price",
                    "end_date": "2015-09-04",
                    "price": "2192.84855",
                    "price_unit": "usd",
                    "start_date": "2011-08-23",
                    "subresource_uris": {
                        "all_time": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/AllTime.json?Category=totalprice",
                        "daily": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=totalprice",
                        "last_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=totalprice",
                        "monthly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Monthly.json?Category=totalprice",
                        "this_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/ThisMonth.json?Category=totalprice",
                        "today": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=totalprice",
                        "yearly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yearly.json?Category=totalprice",
                        "yesterday": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yesterday.json?Category=totalprice"
                    },
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Category=totalprice&StartDate=2011-08-23&EndDate=2015-09-04",
                    "usage": "2192.84855",
                    "usage_unit": "usd"
                }
            ]
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .records.list(
                category="calleridlookups",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Category": "calleridlookups",
                "EndDate": "2008-01-02",
                "EndDate<": "2008-01-01",
                "EndDate>": "2008-01-03",
                "StartDate": "2008-01-02",
                "StartDate<": "2008-01-01",
                "StartDate>": "2008-01-03"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Page=0&PageSize=1",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Page=68&PageSize=1",
            "next_page_uri": null,
            "num_pages": 69,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 69,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records",
            "usage_records": []
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .records.list(
                category="calleridlookups",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Page=0&PageSize=1",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records?Page=68&PageSize=1",
            "next_page_uri": null,
            "num_pages": 69,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 69,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records",
            "usage_records": []
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .usage \
            .records.list(
                category="calleridlookups",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Category": "calleridlookups",
                "EndDate": "2008-01-02",
                "EndDate<": "2008-01-01",
                "EndDate>": "2008-01-03",
                "StartDate": "2008-01-02",
                "StartDate<": "2008-01-01",
                "StartDate>": "2008-01-03"
            },
        )
