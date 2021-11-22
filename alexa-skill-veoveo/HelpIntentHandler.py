from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_intent_name

"""
Se encarga de gestionar la respuesta a la solicitud AMAZON.HelpIntent
que sucede cuando el usuario dice, por ejemplo, ayuda
"""


class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = "¡Bienvenidos a la aplicación Veo Veo!. Comienza diciendo veo veo, después debes decirme una " \
                      "letra y adivinaré lo que ves "

        return handler_input.response_builder.speak(speech_text).response
