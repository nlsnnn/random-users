from typing import TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T")


class Pagination(BaseModel, Generic[T]):
    page: int
    size: int
    total: int
    items: list[T]
