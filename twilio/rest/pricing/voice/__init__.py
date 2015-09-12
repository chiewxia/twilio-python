# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.resources.base import NextGenListResource
from twilio.rest.pricing.voice.number import (
    Numbers,
    Number,
)
from twilio.rest.pricing.voice.country import (
    Countries,
    Country,
)


class Voice(NextGenInstanceResource):
    """
    .. attribute:: name
    
        The name
    
    .. attribute:: url
    
        The url
    
    .. attribute:: links
    
        The links
    """
    id_key = "sid"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(Voice, self).__init__(parent, None)


class Voices(NextGenListResource):
    name = "Voice"
    mount_name = "voice"
    key = "voice"
    instance = Voice

    def __init__(self, *args, **kwargs):
        super(Voices, self).__init__(*args, **kwargs)
        self.numbers = Numbers(*args, **kwargs)
        self.countries = Countries(*args, **kwargs)

    def load_instance(self, data):
        """ Override because Voice does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
