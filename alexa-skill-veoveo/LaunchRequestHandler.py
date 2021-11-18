from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name

"""
esta clase se encarga de responder a una solicitud de inicio de la skill,
 lo que vamos a hacer es saludar al usuario.
"""


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        """
        speech_text = "<say-as interpret-as=\"interjection\">¿Qué ves?</say-as>, espero estéis listos para " \
                      "una nueva aventura. ¿Cuántos objetos queréis buscar hoy?. "

        re_prompt = "<say-as interpret-as=\"interjection\">Venga exploradores!</say-as>. A la aventura, ¿Cuantos " \
                    "objetos queréis buscar hoy? "
        """

        speech_text = "<say-as interpret-as=\"interjection\">¿Qué ves?</say-as>"
        re_prompt = "<say-as interpret-as=\"interjection\">¡tengo que adivinar lo que ves!</say-as>"

        return handler_input.response_builder.speak(speech_text).ask(re_prompt).set_should_end_session(False).response
