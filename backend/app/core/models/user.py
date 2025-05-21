from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import Base


class User(Base):
    name: Mapped[str]
    last_name: Mapped[str]
    gender: Mapped[str]
    phone_number: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    address: Mapped[str]
    photo: Mapped[str]
