from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DEV_DATABASE_URL = os.getenv("DEV_DATABASE_URL")


engine = create_engine(
    DATABASE_URL,
    pool_size=10,          
    max_overflow=5,       
    pool_timeout=30,       
    pool_recycle=1800,     
    pool_pre_ping=True     
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
