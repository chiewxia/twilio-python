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


class Participant(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account that created this conference
    
    .. attribute:: call_sid
    
        A 34 character string that uniquely identifies the call that is
        connected to this conference
    
    .. attribute:: conference_sid
    
        A 34 character string that identifies the conference this participant is
        in
    
    .. attribute:: date_created
    
        The date that this resource was created, given in RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given in RFC 2822 format.
    
    .. attribute:: end_conference_on_exit
    
        Was the `endConferenceOnExit` set on this participant (`true` or
        `false`)?
    
    .. attribute:: muted
    
        `true` if this participant is currently muted. `false` otherwise.
    
    .. attribute:: parent_sid
    
        The parent_sid
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: start_conference_on_enter
    
        Was the `startConferenceOnEnter` attribute set on this participant
        (`true` or `false`)?
    
    .. attribute:: uri
    
        he URI for this resource, relative to `https://api.twilio.com`.
    """
    id_key = "call_sid"

    def load(self, *args, **kwargs):
        super(Participant, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the properties of this participant
        
        :param bool muted: Indicates if the participant should be muted
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Participant`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Kick a participant from a given conference
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()

    def mute(self, **kwargs):
        """ An alias to update """
        return self.update(muted=True, **kwargs)

    def unmute(self, **kwargs):
        """ An alias to update """
        return self.update(muted=False, **kwargs)

    def kick(self):
        """ An alias to delete """
        return self.delete()


class Participants(ListResource):
    name = "Participants"
    mount_name = "participants"
    key = "participants"
    instance = Participant

    def __init__(self, *args, **kwargs):
        super(Participants, self).__init__(*args, **kwargs)

    def get(self):
        """
        Fetch an instance of a participant
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Participant`
        :returns: A placeholder for a :class:`Participant` resource
        """
        return self.get_instance()

    def update(self, muted, **kwargs):
        """
        Update the properties of this participant
        
        :param bool muted: Indicates if the participant should be muted
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Participant`
        """
        kwargs["Muted"] = muted
        return self.update_instance(, kwargs)

    def delete(self):
        """
        Kick a participant from a given conference
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()

    def list(self, **kwargs):
        """
        Retrieve a list of participants belonging to the account used to make the request
        
        :param bool muted: Only show participants that are muted or unmuted
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Participant`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of participants belonging to the account used to make the request
        
        :param bool muted: Only show participants that are muted or unmuted
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Participant`
        """
        return super(Participants, self).iter(**kwargs)

    def mute(self, sid, **kwargs):
        """ An alias to update """
        return self.update(sid, muted=True, **kwargs)

    def unmute(self, sid, **kwargs):
        """ An alias to update """
        return self.update(sid, muted=False, **kwargs)

    def kick(self, sid):
        """ An alias to delete """
        return self.delete(sid)
