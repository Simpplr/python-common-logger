from enum import Enum

class ExecutionContextType(Enum):
    CORRELATION_ID = 'correlation_id'
    TENANT_ID = 'tenant_id'
    USER_ID = 'user_id'