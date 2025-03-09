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
			category_id=category.id)

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

def get_category_by_id(cat_id):
	try:
		with Session(engine) as session:
			sel = select(Category).where(
					Category.id.in_([cat_id])
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

def get_categories():
	with Session(engine) as session:
		sel = select(Category)
		categories = session.scalars(sel).all()

		return categories

def get_seller_id(tg_id):
	with Session(engine) as session:
		sel = select(Seller).where(
				Seller.tg_id.in_([tg_id])
			)
		seller = session.scalars(sel).one()

		return seller.id

def create_item(title, desc, price, image, cashback, cond, seller_id, cat_id, link):
	with Session(engine) as session:
		item = Item(
			title=title,
			description=desc,
			price=price,
			image=image,
			cashback=cashback,
			cashback_condition=cond,
			seller_id=seller_id,
			category_id=cat_id,
			link=link)
		session.add(item)
		session.commit()

def get_seller_items(tg_id):
	with Session(engine) as session:
		sel = select(Seller).where(
				Seller.tg_id.in_([tg_id])
			)
		seller = session.scalars(sel).one()

		sel = select(Item).where(
				Item.seller_id.in_([seller.id])
			)
		items = session.scalars(sel).all()

		return items

def get_item_by_id(item_id):
	try:
		with Session(engine) as session:
			sel = select(Item).where(
					Item.id.in_([item_id])
				)
			item = session.scalars(sel).one()

			return item

	except NoResultFound:
		return None

def delete_item(item_id):
	item = get_item_by_id(item_id)
	with Session(engine) as session:
		session.delete(item)
		session.commit()

def create_category(title):
	with Session(engine) as session:
		cat = Category(title=title)
		session.add(cat)
		session.commit()

def delete_category(cat_id):
	cat = get_category_by_id(cat_id)
	with Session(engine) as session:
		session.delete(cat)
		session.commit()

def get_items_in_category(cat_id):
	with Session(engine) as session:
		sel = select(Item).where(
				Item.category_id.in_([cat_id])
			)
		items = session.scalars(sel).all()

		return items

def get_users_with_cat(cat_id):
	with Session(engine) as session:
		sel = select(Client).where(
				Client.category_id.in_([cat_id])
			)
		users = session.scalars(sel).all()

		return users

def get_startup_info():
	with Session(engine) as session:
		sel1 = select(Client)
		sel2 = select(Seller)
		sel3 = select(Item)
		sel4 = select(Category)

		clients = session.scalars(sel1).all()
		sellers = session.scalars(sel2).all()
		items = session.scalars(sel3).all()
		cats = session.scalars(sel4).all()

		return [
		len(clients),
		len(sellers),
		len(cats),
		len(items)
		]

if __name__ == "__main__":
	get_startup_info()