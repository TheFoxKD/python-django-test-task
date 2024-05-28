from dataclasses import dataclass


@dataclass
class AuthenticationException(Exception):
    message: str = 'Authentication failed'


@dataclass
class UserNotFoundException(AuthenticationException):
    message: str = 'User not found'


@dataclass
class InvalidPasswordException(AuthenticationException):
    message: str = 'Invalid password'
