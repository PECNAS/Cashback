from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer
from sqlalchemy import ForeignKey

from .Base import Base

class Request(Base):
	__tablename__ = "request"
	
	id: Mapped[int] = mapped_column(primary_key=True)
	date: Mapped[str] = mapped_column(String())
	status: Mapped[str] = mapped_column(String())
	
	client_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
	item_id: Mapped[int] = mapped_column(ForeignKey("item.id"), nullable=False)

	def __repr__(self):
		return self.id