from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

from .Base import Base

class Category(Base):
	__tablename__ = "category"
	
	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(String(30))
	
	items: Mapped[list["Item"]] = relationship(back_populates="category")

	def __repr__(self):
		return self.title