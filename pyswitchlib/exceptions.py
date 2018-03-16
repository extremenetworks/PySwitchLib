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

class ExistingApiPortBound(PyswitchlibException):
    """If defined API port is different that existing bound port. The existing bound port should be used."""

class ApiDaemonConnectionError(PyswitchlibException):
    """If connection to the API daemon fails or API daemon cannot be found."""

class RestProtocolTypeError(PyswitchlibException):
    """If provided rest protocol type specified is invalid."""

class CACertificateNotFoundError(PyswitchlibException):
    """If provided path to the CA certificate cannot be found."""

class CACertificateNotSpecifiedError(PyswitchlibException):
    """If the CA certificate path is not specified."""

class InvalidAuthenticationCredentialsError(PyswitchlibException):
    """If the provided authentication credentials are invalid."""

