from uuid import uuid4
from src.logger import _locals

class ContextMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        correlation_id = uuid4()
        tenant_id = uuid4()
        user_id = uuid4()
        _locals.correlation_id = correlation_id
        _locals.tenant_id = tenant_id
        _locals.user_id = user_id
        response = self.get_response(request)
        return response