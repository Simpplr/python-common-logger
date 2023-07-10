import logging 
import json
import sys

from .context.context_handler import get_thread_execution_context
from .context.execution_context import ExecutionContext, ExecutionContextType

from  .constants.logger import LoggerKeys
from  .constants.context import ExecutionContextType

class ContextFilter(logging.Filter):
    def filter(self, record):
        execution_context: ExecutionContext = get_thread_execution_context()

        context_values: dict = execution_context.get_context()
        print(f'Log Filter context: {context_values}')

        for key in ExecutionContext.ALLOWED_KEYS:
            print(key)
            if key in context_values:
                setattr(record, key, context_values[key])
                print(context_values[key])
            else:
                setattr(record, key, '')
        return True

# TODO: Accept config to accept type of values to be logged
def initialise(service_name, level=logging.DEBUG):
    logger = logging.getLogger(service_name)
    
    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)

    # Populate Context Filter in Record
    log_format = {
        "source": "%(name)s",
        "time": "%(asctime)s",
        "log": {
            "message": "%(message)s"
        } 
    }

    log_format[LoggerKeys.CORRELATION_ID.value] = f"%({ExecutionContextType.CORRELATION_ID.value})s"
    log_format[LoggerKeys.TENANT_ID.value] = f"%({ExecutionContextType.TENANT_ID.value})s"
    log_format[LoggerKeys.USER_ID.value] = f"%({ExecutionContextType.USER_ID.value})s"
    
    # Create formatters and add it to handlers
    c_format = logging.Formatter(json.dumps(log_format), datefmt='%Y-%m-%dT%H:%M:%S%z')

    c_handler.setFormatter(c_format)
    c_handler.addFilter(ContextFilter())

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.setLevel(level)
    
    return logger
