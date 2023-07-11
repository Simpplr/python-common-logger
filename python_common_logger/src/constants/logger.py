from enum import Enum

class LoggerContextConfigKeys(Enum):
    """
    Context Config Keys

    Attributes
    ----------
    DISABLE_TID : str
        Disable Tenant Id
    DISABLE_UID : str
        Disable User Id
    DISABLE_CID : str
        Disable Correlation Id
    """
    DISABLE_TID = 'disable_tid'
    DISABLE_UID = 'disable_uid'
    DISABLE_CID = 'disable_cid'

class LoggerKeys(Enum):
    """
    Logging Key

    Attributes
    ----------
    CORRELATION_ID : str
        Correlation Id
    TENANT_ID : str
        Tenant Id
    USER_ID : str
        User Id
    """
    CORRELATION_ID = 'cid'
    TENANT_ID = 'tid'
    USER_ID = 'uid'