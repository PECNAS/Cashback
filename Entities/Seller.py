from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

from .Base import Base

class Seller(Base):
	__tablename__ = "seller"
	
	id: Mapped[int] = mapped_column(primary_key=True)
	tg_id: Mapped[str] = mapped_column(String(30))
	username: Mapped[str] = mapped_column(String(255))
	shop_title: Mapped[str] = mapped_column(String(100))
	shop_url: Mapped[str] = mapped_column(String())
	items: Mapped[list["Item"]] = relationship(back_populates="seller")

	def __repr__(self):
		return self.shop_title