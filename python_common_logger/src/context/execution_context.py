import copy

from ..exceptions.validation_error import ValidationException
from ..constants.context import ExecutionContextType

class ExecutionContext:
    """
    Stores the Execution context and provides helper methods to manage it.

    Methods
    -------
    update(execution_context:dict, reset:bool=False):
        Updates the Execution Context.

    get_context_by_key(key:str):
        Returns the execution context stored for the provided key.

    get_context() -> dict:
        Returns the entire execution context.
    
    reset(key:str):
        Resets the context.
    """
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
        """
        Updates the execution context.

        Args:
            execution_context (dict): Execution context to be updated.
            reset (bool, optional): If True, replaces the entire context. If False, updates only the provided values. Defaults to False.

        Raises:
            ValidationException: If an invalid key is provided.
        """
        if reset:
            self.reset()

        for key in execution_context.keys():
            if key  not in self.ALLOWED_KEYS:
                raise ValidationException(f'Invalid execution context type: {key}')
            else:
                self._context[key] = execution_context[key]
    
    def get_context_by_key(self, key: str) -> str:
        """
        Returns the execution context for the specified key

        Args:
            key (str): key

        Returns:
            any: Execution Context
        """
        return copy.deepcopy(self._context.get(key))

    def get_context(self) -> dict:
        """
        Returns the execution context.

        Returns:
            dict: Entire execution context
        """
        return copy.deepcopy(self._context)
    
    def reset(self):
        """
        Resets the execution context.
        """
        self._context = {}
