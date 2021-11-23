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
        #session_attr = handler_input.attributes_manager.session_attributes
        letra_escogida = None
        objs_could_see = None
        if slots is not None:
            for slotName, currentSlot in six.iteritems(slots):
                if slotName == 'letra':
                    if currentSlot.value:
                        if currentSlot.value in objetos.keys():
                            objs_could_see = self.buscar_objeto(currentSlot.value)
                        else:
                            letra_escogida = currentSlot.value
                    else:
                        letra_escogida = currentSlot.value
                        logging.error(f"No se ha detectado la letra {currentSlot.value}")
        else:
            #letra_escogida = session_attr.get("letraEscogida")
            objs_could_see = self.buscar_objeto(letra_escogida)

        respuesta = "No se me ocurre nada que empiece por la letra {0}".format(letra_escogida)

        if objs_could_see is not None:
            #session_attr["letraEscogida"] = objs_could_see
            respuesta = "<say-as interpret-as=\"interjection\">Creo que es {0}.</say-as> ¿Es correcto?".format(
                objs_could_see)

        speech_text = respuesta

        logging.info(objs_could_see)
        logging.info(speech_text)

        return handler_input.response_builder.speak(speech_text).response

    def buscar_objeto(self, letra_escogida):
        return random.choice(objetos.get(letra_escogida))
