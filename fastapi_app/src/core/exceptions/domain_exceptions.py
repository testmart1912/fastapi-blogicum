class BaseDomainException(Exception):
    def __init__(self, detail: str) -> None:
        self._detail = detail

    def get_detail(self) -> str:
        return self._detail


class UserNotFoundByLoginException(BaseDomainException):
    _exception_text_template = 'User with login {username} not found'

    def __init__(self, username: str) -> None:
        self._exception_text_template = self._exception_text_template.format(username=username)
        super().__init__(detail=self._exception_text_template)


class PostNotFoundByIdException(BaseDomainException):
    _exception_text_template = 'Post with id {id} not found'

    def __init__(self, id: int) -> None:
        self._exception_text_template = self._exception_text_template.format(id=id)
        super().__init__(detail=self._exception_text_template)


class CategoryNotFoundByIdException(BaseDomainException):
    _exception_text_template = 'Category with id {id} not found'

    def __init__(self, id: int) -> None:
        self._exception_text_template = self._exception_text_template.format(id=id)
        super().__init__(detail=self._exception_text_template)


class CategoryNotFoundBySlugException(BaseDomainException):
    _exception_text_template = 'Category with slug {slug} not found'

    def __init__(self, slug: str) -> None:
        self._exception_text_template = self._exception_text_template.format(slug=slug)
        super().__init__(detail=self._exception_text_template)


class LocationNotFoundByIdException(BaseDomainException):
    _exception_text_template = 'Location with id {id} not found'

    def __init__(self, id: int) -> None:
        self._exception_text_template = self._exception_text_template.format(id=id)
        super().__init__(detail=self._exception_text_template)


class UserNotFoundByIdException(BaseDomainException):
    _exception_text_template = 'User with id {id} not found'

    def __init__(self, id: int) -> None:
        self._exception_text_template = self._exception_text_template.format(id=id)
        super().__init__(detail=self._exception_text_template)


class CommentNotFoundByIdException(BaseDomainException):
    _exception_text_template = 'Comment with id {id} not found'

    def __init__(self, id: int) -> None:
        self._exception_text_template = self._exception_text_template.format(id=id)
        super().__init__(detail=self._exception_text_template)


class CategorySlugAlreadyExistsException(BaseDomainException):
    _exception_text_template = 'Category with slug {slug} already exists'

    def __init__(self, slug: str) -> None:
        self._exception_text_template = self._exception_text_template.format(slug=slug)
        super().__init__(detail=self._exception_text_template)


class LocationNameAlreadyExistsException(BaseDomainException):
    _exception_text_template = 'Location with name {name} already exists'

    def __init__(self, name: str) -> None:
        self._exception_text_template = self._exception_text_template.format(name=name)
        super().__init__(detail=self._exception_text_template)


class WrongPasswordException(BaseDomainException):
    _exception_text = 'Wrong password'

    def __init__(self) -> None:
        super().__init__(detail=self._exception_text)

class ForbiddenActionException(BaseDomainException):
    _exception_text = 'Not enough privileges to perform the action'

    def __init__(self) -> None:
        super().__init__(detail=self._exception_text)
