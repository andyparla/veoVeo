from ask_sdk_core.dispatch_components import AbstractExceptionHandler

"""
Esta clase gestiona las excepciones, 
se puede decir que es un CatchAll para lo que sea que la skill no comprenda. 
Es por esto que simplemente devolvemos True en can_handle indicando que gestionamos cualquier cosa
"""


class AllExceptionsHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        speech_text = "Lo siento, no he comprendido lo que me has dicho. Di, ayuda, para obtener más información " \
                      "sobre cómo jugar. "

        return handler_input.response_builder.speak(speech_text).response
