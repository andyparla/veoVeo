from ask_sdk_core.skill_builder import SkillBuilder
from LaunchRequestHandler import LaunchRequestHandler
from HelpIntentHandler import HelpIntentHandler
from CancelAndStopIntentHandler import CancelAndStopIntentHandler
from SessionEndedRequestHandler import SessionEndedRequestHandler
from ListItemsIntent import ListItemsIntent
from AllExceptionsHandler import AllExceptionsHandler
import logging

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(ListItemsIntent())
sb.add_exception_handler(AllExceptionsHandler())

handler = sb.lambda_handler()
logging.basicConfig(level=logging.INFO)
