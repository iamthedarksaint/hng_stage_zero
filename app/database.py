from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config 


user = config("USER")
host = config("HOST")
port = config("PORT")
password = config("PASSWORD")
database = config("DATABASE")

db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(db_url, pool_size=1, max_overflow=1)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

