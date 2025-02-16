from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from Entities.Client import Client
from Entities.Seller import Seller
from Entities.Item import Item
from Entities.Category import Category

from Entities.Base import Base

engine = create_engine("sqlite:///cashback.db")
Base.metadata.create_all(engine)

def check_user(tg_id):
	with Session(engine) as session:
		try:
			sel = select(Client).where(
					Client.tg_id.in_([tg_id])
				)
			client = session.scalars(sel).one()

			return {
				"role": "client",
				"object": client
			}

		except NoResultFound:
			try:
				sel = select(Seller).where(
						Seller.tg_id.in_([tg_id])
					)
				seller = session.scalars(sel).one()

				return {
					"role": "seller",
					"object": seller
				}
			except NoResultFound:
				return None

def create_client(tg_id, username, category):
	'''
	добавляет запись покупателя в базе данных
	'''
	if username == None: username = "not specified"
	
	with Session(engine) as session:
		client = Client(
			tg_id=tg_id,
			username=username,
			category=category.id)

		session.add(client)
		session.commit()

		print(client)

def get_category_by_title(title):
	try:
		with Session(engine) as session:
			sel = select(Category).where(
					Category.title.in_([title])
				)
			category = session.scalars(sel).one()

			return category

	except NoResultFound:
		return None

def create_seller(tg_id, username, shop_title, shop_url):
	if username == None: username = "not specified"
	
	with Session(engine) as session:
		seller = Seller(
			tg_id=tg_id,
			username=username,
			shop_title=shop_title,
			shop_url=shop_url)

		session.add(seller)
		session.commit()

		print(seller)

if __name__ == "__main__":
	print(get_category_by_title("Для домggа"))