from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_intent_name
import logging
from random import sample, random
from diccionario import objetos
import six

"""
clase que define realmente lo que hace nuestra skill
"""


class ListItemsIntent(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("ListItemsIntent")(handler_input)

    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots

        for slotName, currentSlot in six.iteritems(slots):
            if slotName == 'letra':
                if currentSlot.value:
                    objs_could_see = random.choice(objetos.get(currentSlot.value))
                else:
                    #objs_could_see = sample(self.searchObjects, defaultObjsToSearch)
                    logging.error("No se ha detectado la letra indicada")
        speech_text = "<say-as interpret-as=\"interjection\">Magnífico!</say-as>. Aquí van, prestad atención: {0}. A " \
                      "divertirse!. <say-as interpret-as=\"interjection\">Suerte!</say-as>." \
            .format(", ".join(objs_could_see))

        logging.info(objs_could_see)
        logging.info(speech_text)

        return handler_input.response_builder.speak(speech_text).response
