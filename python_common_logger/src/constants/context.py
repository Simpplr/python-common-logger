from enum import Enum

class ExecutionContextType(Enum):
    """
    ExecutionContextType

    Attributes
    ----------
    CORRELATION_ID : str
        Correlation Id
    TENANT_ID : str
        Tenant Id
    USER_ID : str
        User Id
    """
    CORRELATION_ID = 'correlation_id'
    TENANT_ID = 'tenant_id'
    USER_ID = 'user_id'