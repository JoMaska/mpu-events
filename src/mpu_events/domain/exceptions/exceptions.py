from uuid import UUID


class DomainException(Exception):
    pass


class UserNotFoundException(DomainException):
    def __init__(self, identifier: str | UUID):
        super().__init__(f"User '{identifier}' not found")


class EmailAlreadyExistsException(DomainException):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"User with email '{email}' already exists")


class EventNotFoundException(DomainException):
    def __init__(self, event_id: UUID):
        self.event_id = event_id
        super().__init__(f"Event '{event_id}' not found")


class EventFullException(DomainException):
    pass


class AlreadyRegisteredException(DomainException):
    pass


class UnauthorizedException(DomainException):
    pass