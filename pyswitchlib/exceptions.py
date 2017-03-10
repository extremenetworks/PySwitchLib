"""
This is an auto-generated class for the PySwitchLib exceptions.
exceptions for PySwitchLib asset and APIs.
"""

class PyswitchlibException(Exception):
    """Base exception for errors raised by PySwitchLib."""

class RestInterfaceError(PyswitchlibException):
    """If requests module does not get a successful response from the rest URI."""

class UnsupportedOSError(PyswitchlibException):
    """If firmware version installed on asset is not supported."""

class MultipleChoicesSetError(PyswitchlibException):
    """If more than one choice kwarg is set."""

