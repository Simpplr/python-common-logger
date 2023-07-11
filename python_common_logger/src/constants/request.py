from enum import Enum

class RequestHeaderKeys(Enum):
    """
    Header keys

    Attributes
    ----------
    ACCOUNT_ID : str
        Account Id / Tenant ID
    USER_ID : str
        User Id
    CORRELATION_ID : str
        Correlation Id
    """
    ACCOUNT_ID = 'x-smtip-tid',
    USER_ID = 'x-smtip-uid',
    CORRELATION_ID = 'x-smtip-cid',