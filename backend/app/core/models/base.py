from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
