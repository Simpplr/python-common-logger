from .base import BaseException

class ValidationException(BaseException):
    """
    A class used to represent a Validation Error.
    """
    def __init__(self, message, code=400):
        super().__init__(message, code)