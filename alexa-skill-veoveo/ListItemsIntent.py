from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_intent_name
import logging
from random import sample
import six

"""
clase que define realmente lo que hace nuestra skill
"""


class ListItemsIntent(AbstractRequestHandler):
    def __init__(self):
        self.searchObjects = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                         "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                         "t", "u", "v", "w", "x", "y", "z"]

    def can_handle(self, handler_input):
        return is_intent_name("ListItemsIntent")(handler_input)

    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        defaultObjsToSearch = 3

        for slotName, currentSlot in six.iteritems(slots):
            if slotName == 'letra':
                if currentSlot.value:
                    objs_to_search = sample(self.searchObjects, int(currentSlot.value))
                else:
                    objs_to_search = sample(self.searchObjects, defaultObjsToSearch)
        speech_text = "<say-as interpret-as=\"interjection\">Magnífico!</say-as>. Aquí van, prestad atención: {0}. A " \
                      "divertirse!. <say-as interpret-as=\"interjection\">Suerte!</say-as>." \
            .format(", ".join(objs_to_search))

        logging.info(objs_to_search)
        logging.info(speech_text)

        return handler_input.response_builder.speak(speech_text).response
