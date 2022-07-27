from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def create_session():
    engine = create_engine('sqlite:///api-dev.db')
    db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

    Base = declarative_base()
    Base.query = db_session.query_property()

    return Base, engine, db_session