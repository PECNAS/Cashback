from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer

from .Base import Base

class Client(Base):
	__tablename__ = "user"
	
	id: Mapped[int] = mapped_column(primary_key=True)
	tg_id: Mapped[str] = mapped_column(String(30))
	username: Mapped[str] = mapped_column(String(255))
	category_id: Mapped[int] = mapped_column(Integer())
	min_cashback: Mapped[int] = mapped_column(Integer())

	def __repr__(self):
		return self.username