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


class NotificationIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Mon, 13 Sep 2010 20:02:01 +0000",
            "date_updated": "Mon, 13 Sep 2010 20:02:01 +0000",
            "error_code": "11200",
            "log": "0",
            "message_date": "Mon, 13 Sep 2010 20:02:00 +0000",
            "message_text": "EmailNotification=false&LogLevel=ERROR&sourceComponent=12000&Msg=&httpResponse=500&ErrorCode=11200&url=http%3A%2F%2Fvoiceforms4000.appspot.com%2Ftwiml",
            "more_info": "http://www.twilio.com/docs/errors/11200",
            "request_method": "get",
            "request_url": "https://voiceforms4000.appspot.com/twiml/9436/question/0",
            "request_variables": "AccountSid=ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&CallStatus=in-progress&ToZip=94937&ToCity=INVERNESS&ToState=CA&Called=%2B14156694923&To=%2B14156694923&ToCountry=US&CalledZip=94937&Direction=inbound&ApiVersion=2010-04-01&Caller=%2B17378742833&CalledCity=INVERNESS&CalledCountry=US&CallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&CalledState=CA&From=%2B17378742833",
            "response_body": "blah blah",
            "response_headers": "Date=Mon%2C+13+Sep+2010+20%3A02%3A00+GMT&Content-Length=466&Connection=close&Content-Type=text%2Fhtml%3B+charset%3DUTF-8&Server=Google+Frontend",
            "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.get("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Mon, 13 Sep 2010 20:02:01 +0000",
            "date_updated": "Mon, 13 Sep 2010 20:02:01 +0000",
            "error_code": "11200",
            "log": "0",
            "message_date": "Mon, 13 Sep 2010 20:02:00 +0000",
            "message_text": "EmailNotification=false&LogLevel=ERROR&sourceComponent=12000&Msg=&httpResponse=500&ErrorCode=11200&url=http%3A%2F%2Fvoiceforms4000.appspot.com%2Ftwiml",
            "more_info": "http://www.twilio.com/docs/errors/11200",
            "request_method": "get",
            "request_url": "https://voiceforms4000.appspot.com/twiml/9436/question/0",
            "request_variables": "AccountSid=ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&CallStatus=in-progress&ToZip=94937&ToCity=INVERNESS&ToState=CA&Called=%2B14156694923&To=%2B14156694923&ToCountry=US&CalledZip=94937&Direction=inbound&ApiVersion=2010-04-01&Caller=%2B17378742833&CalledCity=INVERNESS&CalledCountry=US&CallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&CalledState=CA&From=%2B17378742833",
            "response_body": "blah blah",
            "response_headers": "Date=Mon%2C+13+Sep+2010+20%3A02%3A00+GMT&Content-Length=466&Connection=close&Content-Type=text%2Fhtml%3B+charset%3DUTF-8&Server=Google+Frontend",
            "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.get("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.call_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Mon, 13 Sep 2010 20:02:01 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Mon, 13 Sep 2010 20:02:01 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.error_code)
        self.assertEqual(u"11200", instance.error_code)
        self.assertIsNotNone(instance.log)
        self.assertEqual(u"0", instance.log)
        self.assertIsNotNone(instance.message_date)
        self.assertEqual(parse_iso_date("Mon, 13 Sep 2010 20:02:00 +0000"), instance.message_date)
        self.assertIsNotNone(instance.message_text)
        self.assertEqual(u"EmailNotification=false&LogLevel=ERROR&sourceComponent=12000&Msg=&httpResponse=500&ErrorCode=11200&url=http%3A%2F%2Fvoiceforms4000.appspot.com%2Ftwiml", instance.message_text)
        self.assertIsNotNone(instance.more_info)
        self.assertEqual(u"http://www.twilio.com/docs/errors/11200", instance.more_info)
        self.assertIsNotNone(instance.request_method)
        self.assertEqual(u"get", instance.request_method)
        self.assertIsNotNone(instance.request_url)
        self.assertEqual(u"https://voiceforms4000.appspot.com/twiml/9436/question/0", instance.request_url)
        self.assertIsNotNone(instance.request_variables)
        self.assertEqual(u"AccountSid=ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&CallStatus=in-progress&ToZip=94937&ToCity=INVERNESS&ToState=CA&Called=%2B14156694923&To=%2B14156694923&ToCountry=US&CalledZip=94937&Direction=inbound&ApiVersion=2010-04-01&Caller=%2B17378742833&CalledCity=INVERNESS&CalledCountry=US&CallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&CalledState=CA&From=%2B17378742833", instance.request_variables)
        self.assertIsNotNone(instance.response_body)
        self.assertEqual(u"blah blah", instance.response_body)
        self.assertIsNotNone(instance.response_headers)
        self.assertEqual(u"Date=Mon%2C+13+Sep+2010+20%3A02%3A00+GMT&Content-Length=466&Connection=close&Content-Type=text%2Fhtml%3B+charset%3DUTF-8&Server=Google+Frontend", instance.response_headers)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.delete("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            .notifications.delete("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=100",
            "next_page_uri": null,
            "notifications": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2008-08-01",
                    "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Thu, 30 Apr 2015 16:47:33 +0000",
                    "date_updated": "Thu, 30 Apr 2015 16:47:35 +0000",
                    "error_code": "21609",
                    "log": "1",
                    "message_date": "Thu, 30 Apr 2015 16:47:32 +0000",
                    "message_text": "LogLevel=WARN&invalidStatusCallbackUrl=&Msg=Invalid+Url+for+callSid%3A+CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa+invalid+statusCallbackUrl%3A+&ErrorCode=21609",
                    "more_info": "https://www.twilio.com/docs/errors/21609",
                    "request_method": null,
                    "request_url": "",
                    "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "num_pages": 101,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 101,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.list(
                log=1,
                message_date=datetime(2008, 1, 2, 0, 0),
                message_date_before=datetime(2008, 1, 1, 0, 0),
                message_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2008-08-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].call_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Thu, 30 Apr 2015 16:47:33 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Thu, 30 Apr 2015 16:47:35 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].error_code)
        self.assertEqual(u"21609", instances[0].error_code)
        self.assertIsNotNone(instances[0].log)
        self.assertEqual(u"1", instances[0].log)
        self.assertIsNotNone(instances[0].message_date)
        self.assertEqual(parse_iso_date("Thu, 30 Apr 2015 16:47:32 +0000"), instances[0].message_date)
        self.assertIsNotNone(instances[0].message_text)
        self.assertEqual(u"LogLevel=WARN&invalidStatusCallbackUrl=&Msg=Invalid+Url+for+callSid%3A+CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa+invalid+statusCallbackUrl%3A+&ErrorCode=21609", instances[0].message_text)
        self.assertIsNotNone(instances[0].more_info)
        self.assertEqual(u"https://www.twilio.com/docs/errors/21609", instances[0].more_info)
        self.assertIsNone(instances[0].request_method)
        self.assertIsNotNone(instances[0].request_url)
        self.assertEqual(u"", instances[0].request_url)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=100",
            "next_page_uri": null,
            "notifications": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2008-08-01",
                    "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Thu, 30 Apr 2015 16:47:33 +0000",
                    "date_updated": "Thu, 30 Apr 2015 16:47:35 +0000",
                    "error_code": "21609",
                    "log": "1",
                    "message_date": "Thu, 30 Apr 2015 16:47:32 +0000",
                    "message_text": "LogLevel=WARN&invalidStatusCallbackUrl=&Msg=Invalid+Url+for+callSid%3A+CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa+invalid+statusCallbackUrl%3A+&ErrorCode=21609",
                    "more_info": "https://www.twilio.com/docs/errors/21609",
                    "request_method": null,
                    "request_url": "",
                    "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "num_pages": 101,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 101,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.list(
                log=1,
                message_date=datetime(2008, 1, 2, 0, 0),
                message_date_before=datetime(2008, 1, 1, 0, 0),
                message_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Log": 1,
                "MessageDate": "2008-01-02",
                "MessageDate<": "2008-01-01",
                "MessageDate>": "2008-01-03"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=100",
            "next_page_uri": null,
            "notifications": [],
            "num_pages": 101,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 101,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.list(
                log=1,
                message_date=datetime(2008, 1, 2, 0, 0),
                message_date_before=datetime(2008, 1, 1, 0, 0),
                message_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=100",
            "next_page_uri": null,
            "notifications": [],
            "num_pages": 101,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 101,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=1&Page=0"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.list(
                log=1,
                message_date=datetime(2008, 1, 2, 0, 0),
                message_date_before=datetime(2008, 1, 1, 0, 0),
                message_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Log": 1,
                "MessageDate": "2008-01-02",
                "MessageDate<": "2008-01-01",
                "MessageDate>": "2008-01-03"
            },
        )
