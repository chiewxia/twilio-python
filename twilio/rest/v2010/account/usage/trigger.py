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
from twilio.rest.resources.base import ListResource


class Trigger(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account this trigger monitors.
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: callback_method
    
        The HTTP method Twilio will use when making a request to the
        CallbackUrl.  GET or POST.
    
    .. attribute:: callback_url
    
        Twilio will make a request to this url when the trigger fires.
    
    .. attribute:: current_value
    
        The current value of the field the trigger is watching.
    
    .. attribute:: date_created
    
        The date the trigger was created, given as GMT RFC 2822 format.
    
    .. attribute:: date_fired
    
        The date the trigger was last fired, given as GMT RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date the trigger was last updated, given as GMT RFC 2822 format.
    
    .. attribute:: friendly_name
    
        A user-specified, human-readable name for the trigger.
    
    .. attribute:: recurring
    
        How this trigger recurs. Empty for non-recurring triggers. One of
        `daily`, `monthly`, or `yearly` for recurring triggers.  A trigger will
        only fire once during each recurring period.  Recurring periods are in
        GMT.
    
    .. attribute:: sid
    
        The trigger's unique Sid
    
    .. attribute:: trigger_by
    
        The field in the UsageRecord that fires the trigger. One of `count`,
        `usage`, or `price`
    
    .. attribute:: trigger_value
    
        The value at which the trigger will fire.  Must be a positive numeric
        value.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`.
    
    .. attribute:: usage_category
    
        The usage category the trigger watches
    
    .. attribute:: usage_record_uri
    
        The URI of the UsageRecord this trigger is watching, relative to
        `https://api.twilio.com`.
    """
    id_key = "sid"
    ALLTIME = "alltime"
    CALLERIDLOOKUPS = "calleridlookups"
    CALLS = "calls"
    CALLS_CLIENT = "calls-client"
    CALLS_INBOUND = "calls-inbound"
    CALLS_INBOUND_LOCAL = "calls-inbound-local"
    CALLS_INBOUND_TOLLFREE = "calls-inbound-tollfree"
    CALLS_OUTBOUND = "calls-outbound"
    CALLS_SIP = "calls-sip"
    COUNT = "count"
    DAILY = "daily"
    MONTHLY = "monthly"
    PHONENUMBERS = "phonenumbers"
    PHONENUMBERS_LOCAL = "phonenumbers-local"
    PHONENUMBERS_TOLLFREE = "phonenumbers-tollfree"
    PRICE = "price"
    RECORDINGS = "recordings"
    RECORDINGSTORAGE = "recordingstorage"
    SHORTCODES = "shortcodes"
    SHORTCODES_CUSTOMEROWNED = "shortcodes-customerowned"
    SHORTCODES_RANDOM = "shortcodes-random"
    SHORTCODES_VANITY = "shortcodes-vanity"
    SMS = "sms"
    SMS_INBOUND = "sms-inbound"
    SMS_INBOUND_LONGCODE = "sms-inbound-longcode"
    SMS_INBOUND_SHORTCODE = "sms-inbound-shortcode"
    SMS_OUTBOUND = "sms-outbound"
    SMS_OUTBOUND_LONGCODE = "sms-outbound-longcode"
    SMS_OUTBOUND_SHORTCODE = "sms-outbound-shortcode"
    TOTALPRICE = "totalprice"
    TRANSCRIPTIONS = "transcriptions"
    USAGE = "usage"
    YEARLY = "yearly"

    def load(self, *args, **kwargs):
        super(Trigger, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_fired") and self.date_fired:
            self.date_fired = parse_iso_date(self.date_fired)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update an instance of a usage trigger
        
        :param str callback_method: The HTTP method Twilio will use when making a
            request to the CallbackUrl.  GET or POST.
        :param str callback_url: Twilio will make a request to this url when the trigger
            fires.
        :param str friendly_name: A user-specified, human-readable name for the trigger.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Trigger`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Triggers(ListResource):
    name = "Usage/Triggers"
    mount_name = "triggers"
    key = "usage_triggers"
    instance = Trigger

    def __init__(self, *args, **kwargs):
        super(Triggers, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch and instance of a usage-trigger
        
        :param str sid: The usage-trigger Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Trigger`
        :returns: A placeholder for a :class:`Trigger` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update an instance of a usage trigger
        
        :param str callback_method: The HTTP method Twilio will use when making a
            request to the CallbackUrl.  GET or POST.
        :param str callback_url: Twilio will make a request to this url when the trigger
            fires.
        :param str friendly_name: A user-specified, human-readable name for the trigger.
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Trigger`
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Trigger`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def create(self, callback_url, trigger_value, usage_category, **kwargs):
        """
        Create a new UsageTrigger
        
        :param str callback_method: The HTTP method Twilio will use when making a
            request to the CallbackUrl.  GET or POST.
        :param str callback_url: Twilio will make a request to this url when the trigger
            fires.
        :param str friendly_name: A user-specified, human-readable name for the trigger.
        :param str trigger_value: The value at which the trigger will fire.  Must be a
            positive numeric value.
        :param trigger.recurring recurring: How this trigger recurs. Empty for
            non-recurring triggers. One of `daily`, `monthly`, or `yearly` for recurring
            triggers.  A trigger will only fire once during each recurring period. 
            Recurring periods are in GMT.
        :param trigger.trigger_field trigger_by: The field in the UsageRecord that fires
            the trigger. One of `count`, `usage`, or `price`
        :param trigger.usage_category usage_category: The usage category the trigger
            watches
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Trigger`
        """
        kwargs["CallbackUrl"] = callback_url
        kwargs["TriggerValue"] = trigger_value
        kwargs["UsageCategory"] = usage_category
        return self.create_instance(kwargs)

    def list(self, **kwargs):
        """
        Retrieve a list of usage-triggers belonging to the account used to make the request
        
        :param trigger.recurring recurring: Only show UsageTriggers that count over this
            interval. One of daily, monthly, or yearly
        :param trigger.trigger_field trigger_by: Only show UsageTriggers that trigger by
            this field in the UsagRecord
        :param trigger.usage_category usage_category: Only show UsageTriggers that watch
            this usage category
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Trigger`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of usage-triggers belonging to the account used to make the request
        
        :param trigger.recurring recurring: Only show UsageTriggers that count over this
            interval. One of daily, monthly, or yearly
        :param trigger.trigger_field trigger_by: Only show UsageTriggers that trigger by
            this field in the UsagRecord
        :param trigger.usage_category usage_category: Only show UsageTriggers that watch
            this usage category
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Trigger`
        """
        return super(Triggers, self).iter(**kwargs)
