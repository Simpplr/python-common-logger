import copy

from ..exceptions.validation_error import ValidationException
from ..constants.context import ExecutionContextType

class ExecutionContext:
    ALLOWED_KEYS = [e.value for e in ExecutionContextType]

    def __init__(self, execution_context: dict):
        self._context = {}
        for key in execution_context.keys():
            if key  not in self.ALLOWED_KEYS:
                # TODO: Create Validation error
                raise ValidationException(f'Invalid execution context type: {key}')
            else:
                self._context[key] = execution_context[key]

    def update(self, execution_context: dict, reset=False):
        if reset:
            self.reset()

        for key in execution_context.keys():
            if key  not in self.ALLOWED_KEYS:
                # TODO: Create Validation error
                raise ValidationException(f'Invalid execution context type: {key}')
            else:
                self._context[key] = execution_context[key]
    
    def get_context_by_key(self, key: str) -> str:
        return copy.deepcopy(self._context[key])

    def get_context(self) -> dict:
        return copy.deepcopy(self._context)
    
    def reset(self):
        self._context = {}