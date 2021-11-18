from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_intent_name

"""
Esta clase va a gestionar dos intenciones AMAZON.CancelIntent y AMAZON.StopIntent, 
usualmente ue el usuario diga “para”, “olvídalo” o “cancela” para nosotros significa lo mismo, 
queremos detener cualquier cosa que Alexa esté haciendo en ese momento.
"""


class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speech_text = "¡Hasta la próxima!."

        return handler_input.response_builder.speak(speech_text).response
