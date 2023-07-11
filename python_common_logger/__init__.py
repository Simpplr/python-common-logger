"""
Python Common Logger to log in JSON format with context data.

Check: https://simpplr.atlassian.net/wiki/spaces/SA/pages/2467365251/Logging+Strategy

Classes:
    Logger.ContextFilter
    DjangoMiddleware.ContextMiddleware
    ContextConstants.ExecutionContextType
    LoggingConstants.LoggerContextConfigKeys
    LoggingConstants.LoggerKeys
    RequestConstants.RequestHeaderKeys

Functions:
    Logger.initialise_console_logger(logger_name, service_name, level=logging.WARNING, context_config=None)
    ContextHandler.get_thread_execution_context(key='execution_context')
    ContextHandler.update_execution_context(execution_context, key='execution_context', reset=False)
"""

from .src import logger as Logger
from .src.context import context_handler as ContextHandler
from .src.django import middleware as DjangoMiddleware

from .src.constants import context as ContextConstants
from .src.constants import logger as LoggingConstants
from .src.constants import request as RequestConstants

from .src.context.execution_context import *

