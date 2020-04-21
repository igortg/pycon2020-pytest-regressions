from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session

Base = declarative_base()
Session = None

def init_db():
    engine = create_engine('sqlite://')
    conn = engine.connect()
    Base.metadata.create_all(bind=conn)
    global Session
    session_maker = sessionmaker(bind=conn)
    Session = scoped_session(session_maker)


def db_session():
    if not Session:
        raise RuntimeError("Call init_db")
    return Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))
    address_id = Column(Integer, ForeignKey('addresses.id'))
    address = relationship("Address")


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
