from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
import six

"""
clase que define realmente lo que hace nuestra skill
"""


class CositaIntent(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("CositaIntent")(handler_input)

    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        palabra_dicha = None
        for slotName, currentSlot in six.iteritems(slots):
            if slotName == 'cosita' and currentSlot.value:
                palabra_dicha = currentSlot.value

        respuesta = "¿Qué es?"
        if palabra_dicha is not None:
            respuesta = "¿Qué {0} es?".format(palabra_dicha)
        speech_text = respuesta

        return handler_input.response_builder.speak(speech_text).response
