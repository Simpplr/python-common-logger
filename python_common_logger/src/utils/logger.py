import logging 
import json
import sys

from logging import Handler, StreamHandler, Formatter, Filter
from ..constants.logger import LoggerKeys, LoggerContextConfigKeys
from ..constants.context import ExecutionContextType

DEFAULT_DATE_FORMAT='%Y-%m-%dT%H:%M:%S%z'

def create_stream_handler(formatter: Formatter, filter: Filter=None) -> StreamHandler:
    """
    Create a custom stream handler

    Args:
        formatter (Formatter): Formatter for the handler
        filter (Filter, optional): Filter for the Handler. Defaults to None.

    Returns:
        StreamHandler: Initialised Stream Handler
    """
    log_handler: StreamHandler = logging.StreamHandler(sys.stdout)

    if filter:
        log_handler.addFilter(filter)

    log_handler.setFormatter(formatter)

    return log_handler

def create_json_formatter(service_name: str, context_config:dict=None, date_format:str=DEFAULT_DATE_FORMAT) -> Formatter:
    """
    Create a custom JSON Formatter

    Args:
        service_name (string): Service Name
        context_config (dict, optional): Context data config. Defaults to None.
        date_format (str, optional): Date format for the logs. Defaults to DEFAULT_DATE_FORMAT.

    Returns:
        Formatter: Log formatter
    """
    log_format = {
        "src": f"{service_name}",
        "time": "%(asctime)s",
        "log": {
            "message": "%(message)s",
            "filename": "%(filename)s",
            "funcName": "%(funcName)s",
            "lineno": "%(lineno)s"
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
    
    log_formatter = logging.Formatter(json.dumps(log_format), datefmt=date_format)

    return log_formatter

def create_simple_handler(date_format:str=DEFAULT_DATE_FORMAT) -> StreamHandler:
    """
    Creates a Simple Handler.
    Can be used for dev / local testing, for better readability.

    Args:
        date_format (str, optional): Date format for the logs. Defaults to DEFAULT_DATE_FORMAT.

    Returns:
        StreamHandler: Log Handler
    """
    log_formatter = create_simple_formatter(date_format)
    
    log_handler = create_stream_handler(log_formatter)

    return log_handler

def create_simple_formatter(date_format:str=DEFAULT_DATE_FORMAT) -> Formatter:
    """
    Creates a Simple Formatter.
    Can be used for dev / local testing, for better readability. 

    Args:
        date_format (str, optional): Date format for the logs. Defaults to DEFAULT_DATE_FORMAT.

    Returns:
        Formatter: Log formatter
    """
    log_format = "%(asctime)s %(levelname)s [%(filename)s:%(funcName)s:%(lineno)s] %(message)s"
    
    log_formatter = logging.Formatter(log_format, datefmt=date_format)

    return log_formatter

