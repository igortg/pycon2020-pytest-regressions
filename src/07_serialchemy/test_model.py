import pytest
import serialchemy.func as serialchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, User, Address


@pytest.fixture
def session():
    engine = create_engine('sqlite://')
    conn = engine.connect()
    Base.metadata.create_all(bind=conn)
    Session = sessionmaker(bind=conn)
    yield Session()
    conn.close()


@pytest.fixture(autouse=True)
def seed_db(session):
    user = User(name='Michael', nickname='Mike')
    user.address = Address(street="5th Avenue", city="New York")
    session.add(user)
    session.commit()

def test_user(data_regression, session):
    user = session.query(User).filter_by(name='Michael').first()
    serialized = serialchemy.dump(user, nest_foreign_keys=True)
    data_regression.check(serialized)
