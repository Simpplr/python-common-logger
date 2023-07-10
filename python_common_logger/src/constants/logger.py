from enum import Enum

class ContextConfig(Enum):
    DISABLE_TID = 'disable_tid'
    DISABLE_UID = 'disable_uid'
    DISABLE_CID = 'disable_cid'

class LoggerKeys(Enum):
    CORRELATION_ID = 'cid'
    TENANT_ID = 'tid'
    USER_ID = 'uid'