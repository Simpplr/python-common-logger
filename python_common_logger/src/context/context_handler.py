from .execution_context import ExecutionContext

from threading import local

_locals = local()

def get_thread_execution_context() -> ExecutionContext:
    return getattr(_locals, 'execution_context', ExecutionContext({}))

def update_execution_context(execution_context: ExecutionContext, reset=False):
    current_execution_context: ExecutionContext = get_thread_execution_context()
    
    current_execution_context.update(execution_context.get_context(), reset)

    setattr(_locals, 'execution_context', current_execution_context)
    return current_execution_context