from enum import Enum

class RequestHeaderKeys(Enum):
    ACCOUNT_ID = 'x-smtip-tid',
    USER_ID = 'x-smtip-uid',
    CORRELATION_ID = 'x-smtip-cid',