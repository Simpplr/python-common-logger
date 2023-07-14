import logging 
import json

from logging import Handler, StreamHandler, Formatter, Filter

from .context.context_handler import get_thread_execution_context
from .context.execution_context import ExecutionContext, ExecutionContextType

from .constants.logger import LoggerKeys, LoggerContextConfigKeys
from .constants.context import ExecutionContextType
from .utils.logger import create_json_formatter, create_stream_handler

class ContextFilter(Filter):
    """
    Log filter to extract the execution context from thread locals and populate it in the log record
    """

    def filter(self, record):
        execution_context: ExecutionContext = get_thread_execution_context()

        context_values: dict = execution_context.get_context()

        for key in ExecutionContext.ALLOWED_KEYS:
            if key in context_values:
                setattr(record, key, context_values[key])
            else:
                setattr(record, key, '')
        return True

def initialise_console_logger(logger_name, service_name, level=logging.WARNING, context_config=None):
    """
    @deprecated - use initialise_logger instead
    Initialises the logger with the handler, formatter and filter to log context data along with message
    in JSON format on the console.

    Args:
        logger_name (string): Name of the logger to be initialised
        service_name (string): Service name that appears as the source in the logs
        level (int, optional): Log level. Defaults to logging.WARNING.
        context_config (dict, optional): Context config to configure logging parameters See LoggerContextConfigKeys for list of allowed params. Defaults to None.

    Returns:
        Logger: Initialised logger
    """
    return initialise_logger(logger_name, service_name, level, context_config)


def initialise_logger(logger_name, service_name, level=logging.INFO, context_config=None, use_default_json_handler=True, other_handlers: [Handler]=[], propagate_to_parent=False):
    """
    Initialises the logger.

    Args:
        logger_name (string): Name of the logger to be initialised
        service_name (string): Service name that appears as the source in the logs
        level (int, optional): Log level. Defaults to logging.INFO.
        context_config (dict, optional): Context config to configure formatter for logging parameters. See LoggerContextConfigKeys for list of allowed params. Useless if use_default_json_handler is False. Defaults to None. 
        use_default_json_handler (boolean, optional): Use the default JSON logger. Defaults to True.
        other_handlers ([Handler], optional): Handlers to be attached to the logger. Defaults to [].
        propagate_to_parent (boolean, optional): Should the log be propagated to parent. Defaults to False.

    Returns:
        Logger: Initialised logger
    """
    logger = logging.getLogger(logger_name)

    # Skip if already initialised. Helps preventing re-initialisation as Lambda instances share the logger instance.
    if hasattr(logger, 'initialized'):
        return logger

    if use_default_json_handler:
        json_formatter: Formatter = create_json_formatter(service_name, context_config)

        json_handler: Handler = create_stream_handler(json_formatter, ContextFilter())

        logger.addHandler(json_handler)
    
    for handler in other_handlers:
        logger.addHandler(handler)

    logger.setLevel(level)

    logger.propagate = propagate_to_parent
    setattr(logger, 'initialized', True)
    
    return logger