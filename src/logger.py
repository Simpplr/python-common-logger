import logging 
import json
import sys
from threading import local

_locals = local()

class ContextFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'correlation_id'):
                record.correlation_id = ""
        if hasattr(_locals, 'correlation_id'):
            record.correlation_id = _locals.correlation_id
        
        if not hasattr(record, 'tenant_id'):
                record.tenant_id = ""
        if hasattr(_locals, 'tenant_id'):
            record.tenant_id = _locals.tenant_id
        
        if not hasattr(record, 'user_id'):
                record.user_id = ""
        if hasattr(_locals, 'user_id'):
            record.user_id = _locals.user_id
        return True

def initialise(service_name, level=logging.DEBUG):
    logger = logging.getLogger(service_name)
    
    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)

    # Populate Context Filter in Record
    # logger.addFilter(ContextFilter())
    
    # Create formatters and add it to handlers
    c_format = logging.Formatter(json.dumps({
        "source": "%(name)s",
        "cid": "%(correlation_id)s",
        "tid": "%(tenant_id)s",
        "uid": "%(user_id)s",
        "time": "%(asctime)s",
        "log": {
            "message": "%(message)s"
        } 
    }), datefmt='%Y-%m-%dT%H:%M:%S%z')

    c_handler.setFormatter(c_format)
    c_handler.addFilter(ContextFilter())

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.setLevel(level)
    
    return logger
