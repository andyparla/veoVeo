from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_intent_name

"""
Se encarga de gestionar la respuesta a la solicitud AMAZON.HelpIntent
que sucede cuando el usuario dice, por ejemplo, ayuda
"""


class NoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        session_attr = handler_input.attributes_manager.session_attributes
        if "letraEscogida" in session_attr:
            fav_color = session_attr["letraEscogida"]
        speech_text = "¡ohhh! Déjame intentarlo de nuevo."

        return handler_input.response_builder.speak(speech_text).response
