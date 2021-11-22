from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
import logging
import random
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
        letra_escogida = None
        objs_could_see = None
        for slotName, currentSlot in six.iteritems(slots):
            if slotName == 'letra':
                if currentSlot.value:
                    if currentSlot.value in objetos.keys():
                        objs_could_see = random.choice(objetos.get(currentSlot.value))
                    else:
                        letra_escogida = currentSlot.value
                else:
                    letra_escogida = currentSlot.value
                    logging.error(f"No se ha detectado la letra {currentSlot.value}")
        alexa_dice = "No se me ocurre nada que empiece por la letra {0}".format(letra_escogida)

        if objs_could_see is not None:
            alexa_dice = "Creo que es : {0}. Es correcto?".format(objs_could_see)

        speech_text = alexa_dice

        logging.info(objs_could_see)
        logging.info(speech_text)

        return handler_input.response_builder.speak(speech_text).response
