from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from app.database import engine 

Base = declarative_base()

class Detail(Base):
    __tablename__ = 'details'

    email = Column(String, primary_key=True)
    current_datetime = Column(DateTime)
    github_url = Column(String)

Base.metadata.create_all(bind=engine)
