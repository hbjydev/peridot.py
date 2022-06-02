from typing import Any, TypeVar, Generic

T = TypeVar('T')


class Paginator(Generic[T]):
    url: str
    total: int
    size: int
    page: int
    data: Any
    key: str

    def __init__(self, data: dict[str, Any], key: str):
        self.total = data['total']
        self.size = data['size']
        self.page = data['page']
        self.key = key
        self.data = data[self.key]
