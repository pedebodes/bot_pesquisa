from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///db_bot_superbuy.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# class Customers(Base):
#    __tablename__ = 'customers'
#    id = Column(Integer, primary_key=True)

#    name = Column(String)
#    address = Column(String)
#    email = Column(String)


class UrlBase(Base):
   __tablename__='url_base'
   
   id = Column(Integer, primary_key=True)
   dominio = Column(String)    
   url =Column(String) 


   
Base.metadata.create_all(engine)