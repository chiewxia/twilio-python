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
from twilio.rest.v2010.account.incoming_phone_number.local import (
    Locals,
    Local,
)
from twilio.rest.v2010.account.incoming_phone_number.mobile import (
    Mobiles,
    Mobile,
)
from twilio.rest.v2010.account.incoming_phone_number.toll_free import (
    TollFrees,
    TollFree,
)


class IncomingPhoneNumber(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account responsible for this phone number.
    
    .. attribute:: address_requirements
    
        This indicates whether the phone number requires you or your customer to
        have an Address registered with Twilio. Possible values are `none`,
        `any`, `local`, or `foreign`.
    
    .. attribute:: api_version
    
        Calls to this phone number will start a new TwiML session with this API
        version.
    
    .. attribute:: beta
    
        Phone numbers new to the Twilio platform are marked as beta. Possible
        values are either true or `false`.
    
    .. attribute:: capabilities
    
        This is a set of boolean properties that indicate whether a phone number
        can receive calls or messages.  Possible capabilities are  `Voice`,
        `SMS`, and `MMS` with each having a value of either `true` or `false`.
    
    .. attribute:: date_created
    
        The date that this resource was created, given as GMT RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given as GMT RFC 2822
        format.
    
    .. attribute:: friendly_name
    
        A human readable descriptive text for this resource, up to 64 characters
        long. By default, the `FriendlyName` is a nicely formatted version of
        the phone number.
    
    .. attribute:: phone_number
    
        The incoming phone number. e.g., +16175551212 (E.164 format)
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: sms_application_sid
    
        The 34 character sid of the application Twilio should use to handle SMSs
        sent to this number. If a `SmsApplicationSid` is present, Twilio will
        ignore all of the SMS urls above and use those set on the application.
    
    .. attribute:: sms_fallback_method
    
        The HTTP method Twilio will use when requesting the above URL. Either
        `GET` or `POST`.
    
    .. attribute:: sms_fallback_url
    
        The URL that Twilio will request if an error occurs retrieving or
        executing the TwiML from `SmsUrl`.
    
    .. attribute:: sms_method
    
        The HTTP method Twilio will use when making requests to the `SmsUrl`.
        Either `GET` or `POST`.
    
    .. attribute:: sms_url
    
        The URL Twilio will request when receiving an incoming SMS message to
        this number.
    
    .. attribute:: status_callback
    
        The URL that Twilio will request to pass status parameters (such as call
        ended) to your application.
    
    .. attribute:: status_callback_method
    
        The HTTP method Twilio will use to make requests to the `StatusCallback`
        URL. Either `GET` or `POST`.
    
    .. attribute:: uri
    
        he URI for this resource, relative to `https://api.twilio.com`.
    
    .. attribute:: voice_application_sid
    
        The 34 character sid of the application Twilio should use to handle
        phone calls to this number. If a `VoiceApplicationSid` is present,
        Twilio will ignore all of the voice urls above and use those set on the
        application. Setting a `VoiceApplicationSid` will automatically delete
        your `TrunkSid` and vice versa.
    
    .. attribute:: voice_caller_id_lookup
    
        Look up the caller's caller-ID name from the CNAM database ($0.01 per
        look up). Either `true` or `false`.
    
    .. attribute:: voice_fallback_method
    
        The HTTP method Twilio will use when requesting the `VoiceFallbackUrl`.
        Either `GET` or `POST`.
    
    .. attribute:: voice_fallback_url
    
        The URL that Twilio will request if an error occurs retrieving or
        executing the TwiML requested by `Url`.
    
    .. attribute:: voice_method
    
        The HTTP method Twilio will use when requesting the above `Url`. Either
        `GET` or `POST`.
    
    .. attribute:: voice_url
    
        The URL Twilio will request when this phone number receives a call. The
        VoiceURL will  no longer be used if a `VoiceApplicationSid` or a
        `TrunkSid` is set.
    """
    id_key = "sid"
    ANY = "any"
    FOREIGN = "foreign"
    LOCAL = "local"
    NONE = "none"

    def load(self, *args, **kwargs):
        super(IncomingPhoneNumber, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update an incoming-phone-number instance
        
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID name from the
            CNAM database ($0.01 per look up). Either `true` or `false`.
        :param str account_sid: The unique id of the Account to which you wish to
            transfer this phnoe number
        :param str api_version: Calls to this phone number will start a new TwiML
            session with this API version.
        :param str friendly_name: A human readable descriptive text for this resource,
            up to 64 characters long. By default, the `FriendlyName` is a nicely formatted
            version of the phone number.
        :param str sms_application_sid: The 34 character sid of the application Twilio
            should use to handle SMSs sent to this number. If a `SmsApplicationSid` is
            present, Twilio will ignore all of the SMS urls above and use those set on the
            application.
        :param str sms_fallback_method: The HTTP method Twilio will use when requesting
            the above URL. Either `GET` or `POST`.
        :param str sms_fallback_url: The URL that Twilio will request if an error occurs
            retrieving or executing the TwiML from `SmsUrl`.
        :param str sms_method: The HTTP method Twilio will use when making requests to
            the `SmsUrl`. Either `GET` or `POST`.
        :param str sms_url: The URL Twilio will request when receiving an incoming SMS
            message to this number.
        :param str status_callback: The URL that Twilio will request to pass status
            parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method Twilio will use to make
            requests to the `StatusCallback` URL. Either `GET` or `POST`.
        :param str voice_application_sid: The 34 character sid of the application Twilio
            should use to handle phone calls to this number. If a `VoiceApplicationSid` is
            present, Twilio will ignore all of the voice urls above and use those set on the
            application. Setting a `VoiceApplicationSid` will automatically delete your
            `TrunkSid` and vice versa.
        :param str voice_fallback_method: The HTTP method Twilio will use when
            requesting the `VoiceFallbackUrl`. Either `GET` or `POST`.
        :param str voice_fallback_url: The URL that Twilio will request if an error
            occurs retrieving or executing the TwiML requested by `Url`.
        :param str voice_method: The HTTP method Twilio will use when requesting the
            above `Url`. Either `GET` or `POST`.
        :param str voice_url: The URL Twilio will request when this phone number
            receives a call. The VoiceURL will  no longer be used if a `VoiceApplicationSid`
            or a `TrunkSid` is set.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`IncomingPhoneNumber`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Delete a phone-numbers belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class IncomingPhoneNumbers(ListResource):
    name = "IncomingPhoneNumbers"
    mount_name = "incoming_phone_numbers"
    key = "incoming_phone_numbers"
    instance = IncomingPhoneNumber

    def __init__(self, *args, **kwargs):
        super(IncomingPhoneNumbers, self).__init__(*args, **kwargs)
        self.local = Locals(*args, **kwargs)
        self.mobile = Mobiles(*args, **kwargs)
        self.toll_free = TollFrees(*args, **kwargs)

    def update(self, sid, **kwargs):
        """
        Update an incoming-phone-number instance
        
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID name from the
            CNAM database ($0.01 per look up). Either `true` or `false`.
        :param str account_sid: The unique id of the Account to which you wish to
            transfer this phnoe number
        :param str api_version: Calls to this phone number will start a new TwiML
            session with this API version.
        :param str friendly_name: A human readable descriptive text for this resource,
            up to 64 characters long. By default, the `FriendlyName` is a nicely formatted
            version of the phone number.
        :param str sid: The sid
        :param str sms_application_sid: The 34 character sid of the application Twilio
            should use to handle SMSs sent to this number. If a `SmsApplicationSid` is
            present, Twilio will ignore all of the SMS urls above and use those set on the
            application.
        :param str sms_fallback_method: The HTTP method Twilio will use when requesting
            the above URL. Either `GET` or `POST`.
        :param str sms_fallback_url: The URL that Twilio will request if an error occurs
            retrieving or executing the TwiML from `SmsUrl`.
        :param str sms_method: The HTTP method Twilio will use when making requests to
            the `SmsUrl`. Either `GET` or `POST`.
        :param str sms_url: The URL Twilio will request when receiving an incoming SMS
            message to this number.
        :param str status_callback: The URL that Twilio will request to pass status
            parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method Twilio will use to make
            requests to the `StatusCallback` URL. Either `GET` or `POST`.
        :param str voice_application_sid: The 34 character sid of the application Twilio
            should use to handle phone calls to this number. If a `VoiceApplicationSid` is
            present, Twilio will ignore all of the voice urls above and use those set on the
            application. Setting a `VoiceApplicationSid` will automatically delete your
            `TrunkSid` and vice versa.
        :param str voice_fallback_method: The HTTP method Twilio will use when
            requesting the `VoiceFallbackUrl`. Either `GET` or `POST`.
        :param str voice_fallback_url: The URL that Twilio will request if an error
            occurs retrieving or executing the TwiML requested by `Url`.
        :param str voice_method: The HTTP method Twilio will use when requesting the
            above `Url`. Either `GET` or `POST`.
        :param str voice_url: The URL Twilio will request when this phone number
            receives a call. The VoiceURL will  no longer be used if a `VoiceApplicationSid`
            or a `TrunkSid` is set.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`IncomingPhoneNumber`
        """
        return self.update_instance(sid, kwargs)

    def get(self, sid):
        """
        Fetch an incoming-phone-number belonging to the account used to make the request
        
        :param str sid: The incoming-phone-number Sid that uniquely identifies this
            resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`IncomingPhoneNumber`
        :returns: A placeholder for a :class:`IncomingPhoneNumber` resource
        """
        return self.get_instance(sid)

    def delete(self, sid):
        """
        Delete a phone-numbers belonging to the account used to make the request
        
        :param str sid: The phone-number Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of incoming-phone-numbers belonging to the account used to make the request
        
        :param bool beta: Include phone numbers new to the Twilio platform
        :param str friendly_name: Only show the incoming phone number resources with
            friendly names that exactly match this name
        :param str phone_number: Only show the incoming phone number resources that
            match this pattern
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`IncomingPhoneNumber`
        """
        return self.get_instances(kwargs)

    def create(self, **kwargs):
        """
        Purchase a phone-number for the account
        
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID name from the
            CNAM database ($0.01 per look up). Either `true` or `false`.
        :param str api_version: Calls to this phone number will start a new TwiML
            session with this API version.
        :param str area_code: The desired area code for the new phone number. Any three
            digit US or Canada rea code is valid
        :param str friendly_name: A human readable descriptive text for this resource,
            up to 64 characters long. By default, the `FriendlyName` is a nicely formatted
            version of the phone number.
        :param str phone_number: The phone number to purchase. e.g., +16175551212 (E.164
            format)
        :param str sms_application_sid: The 34 character sid of the application Twilio
            should use to handle SMSs sent to this number. If a `SmsApplicationSid` is
            present, Twilio will ignore all of the SMS urls above and use those set on the
            application.
        :param str sms_fallback_method: The HTTP method Twilio will use when requesting
            the above URL. Either `GET` or `POST`.
        :param str sms_fallback_url: The URL that Twilio will request if an error occurs
            retrieving or executing the TwiML from `SmsUrl`.
        :param str sms_method: The HTTP method Twilio will use when making requests to
            the `SmsUrl`. Either `GET` or `POST`.
        :param str sms_url: The URL Twilio will request when receiving an incoming SMS
            message to this number.
        :param str status_callback: The URL that Twilio will request to pass status
            parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method Twilio will use to make
            requests to the `StatusCallback` URL. Either `GET` or `POST`.
        :param str voice_application_sid: The 34 character sid of the application Twilio
            should use to handle phone calls to this number. If a `VoiceApplicationSid` is
            present, Twilio will ignore all of the voice urls above and use those set on the
            application. Setting a `VoiceApplicationSid` will automatically delete your
            `TrunkSid` and vice versa.
        :param str voice_fallback_method: The HTTP method Twilio will use when
            requesting the `VoiceFallbackUrl`. Either `GET` or `POST`.
        :param str voice_fallback_url: The URL that Twilio will request if an error
            occurs retrieving or executing the TwiML requested by `Url`.
        :param str voice_method: The HTTP method Twilio will use when requesting the
            above `Url`. Either `GET` or `POST`.
        :param str voice_url: The URL Twilio will request when this phone number
            receives a call. The VoiceURL will  no longer be used if a `VoiceApplicationSid`
            or a `TrunkSid` is set.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`IncomingPhoneNumber`
        """
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of incoming-phone-numbers belonging to the account used to make the request
        
        :param bool beta: Include phone numbers new to the Twilio platform
        :param str friendly_name: Only show the incoming phone number resources with
            friendly names that exactly match this name
        :param str phone_number: Only show the incoming phone number resources that
            match this pattern
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`IncomingPhoneNumber`
        """
        return super(IncomingPhoneNumbers, self).iter(**kwargs)

    def buy(self, phone_number, **kwargs):
        """ An alias to create """
        return self.create(phone_number=phone_number, **kwargs)
