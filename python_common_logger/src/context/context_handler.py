from .execution_context import ExecutionContext

from threading import local

_locals = local()

def get_thread_execution_context(key='execution_context') -> ExecutionContext:
    """
    Fetches the execution context from the thread local. If absent, initialises and returns an empty one.

    Args:
        key (str, optional): key. Defaults to 'execution_context'.
    
    Returns:
        ExecutionContext: Thread local execution context.
    """
    return getattr(_locals, key, ExecutionContext({}))

def update_execution_context(execution_context: ExecutionContext, key='execution_context', reset=False) -> ExecutionContext:
    """
    Updates the execution context.

    Args:
        execution_context (ExecutionContext): Execution context to be updated.
        key (str, optional): key. Defaults to 'execution_context'.
        reset (bool, optional): Reset the entire context. Defaults to False.

    Returns:
        ExecutionContext: Updated execution context
    """
    current_execution_context: ExecutionContext = get_thread_execution_context()
    
    current_execution_context.update(execution_context.get_context(), reset)

    setattr(_locals, key, current_execution_context)

    return current_execution_context