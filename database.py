from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from Entities.Client import Client
from Entities.Seller import Seller
from Entities.Item import Item

from Entities.Base import Base

engine = create_engine("sqlite:///cashback.db")
Base.metadata.create_all(engine)
