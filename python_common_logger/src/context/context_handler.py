import contextvars
import copy

from .execution_context import ExecutionContext

# Define a context variable for execution context
execution_context_var = contextvars.ContextVar('execution_context', default=ExecutionContext({}))

def get_thread_execution_context() -> ExecutionContext:
    """
    Fetches the execution context from the execution_context_var. If absent, initializes and returns an empty one.
    
    Returns:
        ExecutionContext: contextvars execution context.
    """
    return copy.deepcopy(execution_context_var.get())

def update_execution_context(execution_context: ExecutionContext, reset=False) -> ExecutionContext:
    """
    Updates the execution context.

    Args:
        execution_context (ExecutionContext): Execution context to be updated.
        reset (bool, optional): Reset the entire context. Defaults to False.

    Returns:
        ExecutionContext: Updated execution context
    """
    current_execution_context: ExecutionContext = get_thread_execution_context()
    
    current_execution_context.update(execution_context.get_context(), reset)

    # Update the context variable with the updated execution context
    execution_context_var.set(current_execution_context)

    return current_execution_context