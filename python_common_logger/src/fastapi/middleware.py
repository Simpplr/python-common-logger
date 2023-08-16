from uuid import uuid4
from ..context.context_handler import update_execution_context
from ..context.execution_context import ExecutionContext
from starlette.middleware.base import BaseHTTPMiddleware

from ..constants.request import RequestHeaderKeys
from ..constants.context import ExecutionContextType


class FastapiContextMiddleware(BaseHTTPMiddleware):
    """
    Fastapi Context Middle. Extracts the headers from the request and populates the execution context
    in contextvars.
    """
    async def dispatch(self, request, call_next):
        # Extract required headers from the incoming request
        correlation_id = request.headers.get(RequestHeaderKeys.CORRELATION_ID.value)
        account_id = request.headers.get(RequestHeaderKeys.ACCOUNT_ID.value)
        user_id = request.headers.get(RequestHeaderKeys.USER_ID.value)

        # Construct execution_context dictionary with the extracted headers
        execution_context = {}
        if correlation_id:
            execution_context[ExecutionContextType.CORRELATION_ID.value] = correlation_id
        else:
            execution_context[ExecutionContextType.CORRELATION_ID.value] = uuid4()

        if account_id:
            execution_context[ExecutionContextType.TENANT_ID.value] = account_id

        if user_id:
            execution_context[ExecutionContextType.USER_ID.value] = user_id

        # Pass the execution context to update_execution_context
        update_execution_context(ExecutionContext(execution_context))

        # Continue processing the request
        response = await call_next(request)

        return response
