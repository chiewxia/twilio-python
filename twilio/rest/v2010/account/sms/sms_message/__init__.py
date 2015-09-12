# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.v2010.account.message.media import (
    Media,
    MediaList,
)
from twilio.rest.resources.base import ListResource


class SmsMessage(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: body
    
        The body
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: date_sent
    
        The date_sent
    
    .. attribute:: direction
    
        The direction
    
    .. attribute:: error_code
    
        The error_code
    
    .. attribute:: error_message
    
        The error_message
    
    .. attribute:: from
    
        The from
    
    .. attribute:: num_media
    
        The num_media
    
    .. attribute:: num_segments
    
        The num_segments
    
    .. attribute:: price
    
        The price
    
    .. attribute:: price_unit
    
        The price_unit
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: status
    
        The status
    
    .. attribute:: subresource_uris
    
        The subresource_uris
    
    .. attribute:: to
    
        The to
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"
    DELIVERED = "delivered"
    FAILED = "failed"
    INBOUND = "inbound"
    OUTBOUND_API = "outbound-api"
    OUTBOUND_CALL = "outbound-call"
    OUTBOUND_REPLY = "outbound-reply"
    QUEUED = "queued"
    RECEIVED = "received"
    RECEIVING = "receiving"
    SENDING = "sending"
    SENT = "sent"
    UNDELIVERED = "undelivered"
    subresources = [
        MediaList
    ]

    def load(self, *args, **kwargs):
        super(SmsMessage, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)
        
        if hasattr(self, "date_sent") and self.date_sent:
            self.date_sent = parse_iso_date(self.date_sent)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str body: The body
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`SmsMessage`
        """
        return self.update_instance(kwargs)


class SmsMessages(ListResource):
    name = "SMS/Messages"
    mount_name = "messages"
    key = "sms_messages"
    instance = SmsMessage

    def __init__(self, *args, **kwargs):
        super(SmsMessages, self).__init__(*args, **kwargs)

    def create(self, to, from_, **kwargs):
        """
        Create a new :class:`SmsMessage`
        
        :param str application_sid: The application_sid
        :param str body: The body
        :param str from_: The from
        :param str media_url: The media_url
        :param str status_callback: The status_callback
        :param str to: The to
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`SmsMessage`
        """
        kwargs["To"] = to
        kwargs["From"] = from_
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the :class:`SmsMessage`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`SmsMessage`
        :returns: A placeholder for a :class:`SmsMessage` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`SmsMessage`
        
        :param date date_sent: The date_sent
        :param date date_sent_after: The date_sent>
        :param date date_sent_before: The date_sent<
        :param str from_: The from
        :param str to: The to
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`SmsMessage`
        """
        if "from_" in kwargs:
            kwargs["From"] = kwargs["from_"]
            del kwargs["from_"]
        if "date_sent_before" in kwargs:
            kwargs["DateSent<"] = parse_date(kwargs["date_sent_before"])
            del kwargs["date_sent_before"]
        if "date_sent_after" in kwargs:
            kwargs["DateSent>"] = parse_date(kwargs["date_sent_after"])
            del kwargs["date_sent_after"]
        if "date_sent" in kwargs:
            kwargs["DateSent"] = parse_date(kwargs["date_sent"])
            del kwargs["date_sent"]
        return self.get_instances(kwargs)

    def update(self, sid, **kwargs):
        """
        Update a :class:`SmsMessage`
        
        :param str body: The body
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`SmsMessage`
        """
        return self.update_instance(sid, kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`SmsMessage` using an iterator
        
        :param date date_sent: The date_sent
        :param date date_sent_after: The date_sent>
        :param date date_sent_before: The date_sent<
        :param str from_: The from
        :param str to: The to
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`SmsMessage`
        """
        if "from_" in kwargs:
            kwargs["From"] = kwargs["from_"]
            del kwargs["from_"]
        if "date_sent_before" in kwargs:
            kwargs["DateSent<"] = parse_date(kwargs["date_sent_before"])
            del kwargs["date_sent_before"]
        if "date_sent_after" in kwargs:
            kwargs["DateSent>"] = parse_date(kwargs["date_sent_after"])
            del kwargs["date_sent_after"]
        if "date_sent" in kwargs:
            kwargs["DateSent"] = parse_date(kwargs["date_sent"])
            del kwargs["date_sent"]
        return super(SmsMessages, self).iter(**kwargs)
