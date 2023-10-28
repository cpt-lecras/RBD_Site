from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:root@localhost/test')
Base = declarative_base()

class Loyalty(Base):
    __tablename__ = 'loyalty'

    id_loyalty = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    percent = Column(Integer)

class Country(Base):
    __tablename__ = 'country'

    id_country = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tax = Column(Integer)

class Client(Base):
    __tablename__ = 'client'

    id_client = Column(Integer, primary_key=True, autoincrement=True)
    nick = Column(String)
    balance = Column(Integer)
    orders = Column(Integer)

    id_country = Column(Integer, ForeignKey('country.id_country'))
    id_loyalty = Column(Integer, ForeignKey('loyalty.id_loyalty'))
    password=Column(String, nullable=False)


class Rate(Base):
    __tablename__ = 'rate'

    id_rate = Column(Integer, primary_key=True, autoincrement=True)
    ex_BIN = Column(Integer)
    ex_TRUST = Column(Integer)
    ex_BYBIT = Column(Integer)

class Coin(Base):
    __tablename__ = 'coin'

    id_coin = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)

    id_rate = Column(Integer, ForeignKey('rate.id_rate'))

class Bot_wallet(Base):
    __tablename__ = 'bot_wallet'

    id_wallet = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String)
    summ = Column(Integer)

class Ord(Base):
    __tablename__ = 'ord'

    id_wallet = Column(Integer, ForeignKey('wallet.id_wallet'), primary_key=True)
    id_client = Column(Integer, ForeignKey('client.id_client'), primary_key=True)
    id_coin = Column(Integer, ForeignKey('coin.id_coin'), primary_key=True)

    crypto_sum = Column(Integer)
    summ = Column(Integer)
    tax = Column(Integer)

"""
metadata = MetaData()
metadata.reflect(engine)
Base.metadata = metadata
Base.prepare()
"""






Session = sessionmaker(bind=engine)