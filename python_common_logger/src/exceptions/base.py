class BaseException(Exception):
    """
    A class used to represent an Exception with code

    Attributes
    ----------
    message : str
        Message to describe the exception
    code : int
        Represents the integer code. Usually the HTTP error code.
    """
    def __init__(self, message, code=500):
        super().__init__(message)
        self.code = code