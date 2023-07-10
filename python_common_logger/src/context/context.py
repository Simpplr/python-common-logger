
class SimpplrLogContext:
    def __init__(self, correlation_id, tenant_id, user_id):
        self.correlation_id = correlation_id
        self.tenant_id = tenant_id
        self.user_id = user_id