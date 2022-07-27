# Use 'from main import create_session' to execute this file, otherwise it will give error 'ImportError'
#from main import create_session
from .main import create_session
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base, engine, db_session = create_session()

class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, index=True)
    description = Column(String(1000), nullable=False)

    def __repr__(self):
        return f"<(class Notes) '{self.title}' at {hex(id(self))}>"

    def get_data(self):
        return {'title': self.title, 'description': self.description}

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()        

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)