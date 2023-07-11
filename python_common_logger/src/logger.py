import logging 
import json
import sys

from .context.context_handler import get_thread_execution_context
from .context.execution_context import ExecutionContext, ExecutionContextType

from .constants.logger import LoggerKeys, LoggerContextConfigKeys
from .constants.context import ExecutionContextType

class ContextFilter(logging.Filter):
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
    logger = logging.getLogger(logger_name)
    
    # Create handlers
    log_handler = logging.StreamHandler(sys.stdout)

    log_format = {
        "source": f"{service_name}",
        "time": "%(asctime)s",
        "log": {
            "message": "%(message)s"
        },
        "logLevel": "%(levelname)s"
    }

    if not context_config:
        context_config = {}

    if not context_config.get(LoggerContextConfigKeys.DISABLE_CID.value):
        log_format[LoggerKeys.CORRELATION_ID.value] = f"%({ExecutionContextType.CORRELATION_ID.value})s"
    
    if not context_config.get(LoggerContextConfigKeys.DISABLE_TID.value):
        log_format[LoggerKeys.TENANT_ID.value] = f"%({ExecutionContextType.TENANT_ID.value})s"
    
    if not context_config.get(LoggerContextConfigKeys.DISABLE_UID.value):
        log_format[LoggerKeys.USER_ID.value] = f"%({ExecutionContextType.USER_ID.value})s"
    
    # Create formatters and add it to handlers
    log_formatter = logging.Formatter(json.dumps(log_format), datefmt='%Y-%m-%dT%H:%M:%S%z')
    log_handler.setFormatter(log_formatter)
    
    # Populate Context Filter in Record
    log_handler.addFilter(ContextFilter())

    logger.addHandler(log_handler)

    logger.setLevel(level)
    
    return logger
