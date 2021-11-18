from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type

"""
Esta clase gestiona SessionEndedRequest. 
es enviada a la skill cuando el usuario no responde o responde algo que no es reconocido por la skill o hay un error. 
Cerrar la skill de esta forma no permite la utilización de speak o cards 
(para enviar información a la aplicación de Alexa del móvil).
"""


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        handler_input.response_builder.response
