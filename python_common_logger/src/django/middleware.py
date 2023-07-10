from uuid import uuid4
from ..context.context_handler import update_execution_context
from ..context.execution_context import ExecutionContext

from ..constants.request import RequestHeaderKeys
from ..constants.context import ExecutionContextType

class ContextMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        execution_context = {}
        
        if RequestHeaderKeys.CORRELATION_ID.value in request.META:
            execution_context[ExecutionContextType.CORRELATION_ID.value] = request.META[RequestHeaderKeys.CORRELATION_ID.value]
        else:
            execution_context[ExecutionContextType.CORRELATION_ID.value] = uuid4()
        
        if RequestHeaderKeys.ACCOUNT_ID.value in request.META:
            execution_context[ExecutionContextType.TENANT_ID.value] = request.META[RequestHeaderKeys.ACCOUNT_ID.value]
        
        if RequestHeaderKeys.USER_ID.value in request.META:
            execution_context[ExecutionContextType.USER_ID.value] = request.META[RequestHeaderKeys.USER_ID.value]

        update_execution_context(ExecutionContext(execution_context))

        response = self.get_response(request)

        return response