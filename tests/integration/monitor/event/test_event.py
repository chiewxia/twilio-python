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
from twilio.rest.monitor.client import MonitorClient
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class EventIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "actor_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "actor_type": "account",
            "description": null,
            "event_data": {
                "friendly_name": {
                    "previous": "SubAccount Created at 2014-10-03 09:48 am",
                    "updated": "Mr. Friendly"
                }
            },
            "event_date": "2014-10-03T16:48:25Z",
            "event_type": "account.updated",
            "links": {
                "actor": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "resource": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "resource_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "resource_type": "account",
            "sid": "AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "source": "api",
            "source_ip_address": "10.86.6.250",
            "url": "https://monitor.twilio.com/v1/Events/AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .events.get("AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://monitor.twilio.com/v1/Events/AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "actor_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "actor_type": "account",
            "description": null,
            "event_data": {
                "friendly_name": {
                    "previous": "SubAccount Created at 2014-10-03 09:48 am",
                    "updated": "Mr. Friendly"
                }
            },
            "event_date": "2014-10-03T16:48:25Z",
            "event_type": "account.updated",
            "links": {
                "actor": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "resource": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "resource_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "resource_type": "account",
            "sid": "AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "source": "api",
            "source_ip_address": "10.86.6.250",
            "url": "https://monitor.twilio.com/v1/Events/AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .events.get("AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.actor_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.actor_sid)
        self.assertIsNotNone(instance.actor_type)
        self.assertEqual(u"account", instance.actor_type)
        self.assertIsNone(instance.description)
        self.assertIsNotNone(instance.event_date)
        self.assertEqual(parse_iso_date("2014-10-03T16:48:25Z"), instance.event_date)
        self.assertIsNotNone(instance.event_type)
        self.assertEqual(u"account.updated", instance.event_type)
        self.assertIsNotNone(instance.resource_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.resource_sid)
        self.assertIsNotNone(instance.resource_type)
        self.assertEqual(u"account", instance.resource_type)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.source)
        self.assertEqual(u"api", instance.source)
        self.assertIsNotNone(instance.source_ip_address)
        self.assertEqual(u"10.86.6.250", instance.source_ip_address)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "events": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "actor_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "actor_type": "account",
                    "description": null,
                    "event_data": {
                        "friendly_name": {
                            "previous": "SubAccount Created at 2014-10-03 09:48 am",
                            "updated": "Mr. Friendly"
                        }
                    },
                    "event_date": "2014-10-03T16:48:25Z",
                    "event_type": "account.updated",
                    "links": {
                        "actor": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "resource": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    "resource_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "resource_type": "account",
                    "sid": "AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "source": "api",
                    "source_ip_address": "10.86.6.250",
                    "url": "https://monitor.twilio.com/v1/Events/AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "meta": {
                "first_page_url": "https://monitor.twilio.com/v1/Events?PageSize=50&Page=0",
                "key": "events",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://monitor.twilio.com/v1/Events?PageSize=50&Page=0"
            }
        }
        """))
        
        query = client \
            .events.list(
                actor_sid="USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0),
                event_type="event_type",
                resource_sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                source_ip_address="source_ip_address",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].actor_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].actor_sid)
        self.assertIsNotNone(instances[0].actor_type)
        self.assertEqual(u"account", instances[0].actor_type)
        self.assertIsNone(instances[0].description)
        self.assertIsNotNone(instances[0].event_date)
        self.assertEqual(parse_iso_date("2014-10-03T16:48:25Z"), instances[0].event_date)
        self.assertIsNotNone(instances[0].event_type)
        self.assertEqual(u"account.updated", instances[0].event_type)
        self.assertIsNotNone(instances[0].resource_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].resource_sid)
        self.assertIsNotNone(instances[0].resource_type)
        self.assertEqual(u"account", instances[0].resource_type)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].source)
        self.assertEqual(u"api", instances[0].source)
        self.assertIsNotNone(instances[0].source_ip_address)
        self.assertEqual(u"10.86.6.250", instances[0].source_ip_address)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "events": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "actor_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "actor_type": "account",
                    "description": null,
                    "event_data": {
                        "friendly_name": {
                            "previous": "SubAccount Created at 2014-10-03 09:48 am",
                            "updated": "Mr. Friendly"
                        }
                    },
                    "event_date": "2014-10-03T16:48:25Z",
                    "event_type": "account.updated",
                    "links": {
                        "actor": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "resource": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    "resource_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "resource_type": "account",
                    "sid": "AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "source": "api",
                    "source_ip_address": "10.86.6.250",
                    "url": "https://monitor.twilio.com/v1/Events/AEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "meta": {
                "first_page_url": "https://monitor.twilio.com/v1/Events?PageSize=50&Page=0",
                "key": "events",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://monitor.twilio.com/v1/Events?PageSize=50&Page=0"
            }
        }
        """))
        
        query = client \
            .events.list(
                actor_sid="USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0),
                event_type="event_type",
                resource_sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                source_ip_address="source_ip_address",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://monitor.twilio.com/v1/Events",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "ActorSid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "EndDate": "2008-01-02",
                "EndDate<": "2008-01-01",
                "EndDate>": "2008-01-03",
                "EventType": "event_type",
                "ResourceSid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "SourceIpAddress": "source_ip_address",
                "StartDate": "2008-01-02",
                "StartDate<": "2008-01-01",
                "StartDate>": "2008-01-03"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "events": [],
            "meta": {
                "first_page_url": "https://monitor.twilio.com/v1/Events?PageSize=50&Page=0",
                "key": "events",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://monitor.twilio.com/v1/Events?PageSize=50&Page=0"
            }
        }
        """))
        
        query = client \
            .events.list(
                actor_sid="USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0),
                event_type="event_type",
                resource_sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                source_ip_address="source_ip_address",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "events": [],
            "meta": {
                "first_page_url": "https://monitor.twilio.com/v1/Events?PageSize=50&Page=0",
                "key": "events",
                "next_page_url": null,
                "page": 0,
                "page_size": 50,
                "previous_page_url": null,
                "url": "https://monitor.twilio.com/v1/Events?PageSize=50&Page=0"
            }
        }
        """))
        
        query = client \
            .events.list(
                actor_sid="USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0),
                event_type="event_type",
                resource_sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                source_ip_address="source_ip_address",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://monitor.twilio.com/v1/Events",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "ActorSid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "EndDate": "2008-01-02",
                "EndDate<": "2008-01-01",
                "EndDate>": "2008-01-03",
                "EventType": "event_type",
                "ResourceSid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "SourceIpAddress": "source_ip_address",
                "StartDate": "2008-01-02",
                "StartDate<": "2008-01-01",
                "StartDate>": "2008-01-03"
            },
        )
