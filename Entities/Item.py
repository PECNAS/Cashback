from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, Integer, ForeignKey

from .Base import Base

class Item(Base):
	__tablename__ = "item"
	
	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(String(255))
	description: Mapped[str] = mapped_column(String())
	price: Mapped[int] = mapped_column(Integer())
	image: Mapped[str] = mapped_column(String())
	cashback: Mapped[int] = mapped_column(Integer())
	cashback_condition: Mapped[str] = mapped_column(String())

	seller: Mapped["Seller"] = relationship(back_populates="items", lazy="joined")
	seller_id: Mapped[int] = mapped_column(ForeignKey("seller.id"), nullable=False)

	category: Mapped["Category"] = relationship(back_populates="items", lazy="joined")
	category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)

	def __repr__(self):
		return self.title