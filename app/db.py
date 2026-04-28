from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import  AsyncSession, create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

load_dotenv()# load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL") # get URL data base from variables environment
engine = create_async_engine(DATABASE_URL, echo=True)
 # creating async engine SQLAlchemy with  URL data base from variables environment and echo enabled for logging SQL statements
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False) # creating async session maker SQLAlchemy with the created engine, using AsyncSession as the session class and setting expire_on_commit to False to prevent automatic expiration of objects after commit


SECRET_KEY = os.getenv("SECRET_KEY") # get secret key from variables environment


DEBUG = os.getenv("DEBUG", "False").lower() == "true" # get value of DEBUG from variables environment and convert it to boolean type


class Base(DeclarativeBase):  # create a base class for declarative models using SQLAlchemy's DeclarativeBase
    pass





async def get_db(): # create an asynchronous generator function to provide a database session
    async with async_session_maker() as session: # create an asynchronous context manager to manage the database session
        yield session # yield the session to be used in the application, allowing for proper cleanup after use