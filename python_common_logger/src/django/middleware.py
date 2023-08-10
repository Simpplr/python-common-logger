from uuid import uuid4
from ..context.context_handler import update_execution_context
from ..context.execution_context import ExecutionContext

from ..constants.request import RequestHeaderKeys
from ..constants.context import ExecutionContextType

class ContextMiddleware():
    """
    Django Context Middle. Extracts the headers from the request and populates the execution context
    in thread local data.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        execution_context = {}

        cid_django_header = convert_to_django_header(RequestHeaderKeys.CORRELATION_ID.value)
        tid_django_header = convert_to_django_header(RequestHeaderKeys.ACCOUNT_ID.value)
        uid_django_header = convert_to_django_header(RequestHeaderKeys.USER_ID.value)

        if cid_django_header in request.META:
            execution_context[ExecutionContextType.CORRELATION_ID.value] = request.META[cid_django_header]
        else:
            execution_context[ExecutionContextType.CORRELATION_ID.value] = uuid4()
        
        if tid_django_header in request.META:
            execution_context[ExecutionContextType.TENANT_ID.value] = request.META[tid_django_header]
        
        if uid_django_header in request.META:
            execution_context[ExecutionContextType.USER_ID.value] = request.META[uid_django_header]

        update_execution_context(ExecutionContext(execution_context))

        response = self.get_response(request)

        return response

"""
Convert header keys as Django converts the received headers.
See: https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.META
"""
def convert_to_django_header(header_key: str) -> str:
    return f'HTTP_{header_key.replace("-", "_").upper()}'