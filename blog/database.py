from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# setting up the link to the database 
SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

# 
engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread":False})

# each time sessionsLocal is called it will create a session with the database. the name is sessionlocale to make a diffrence with in imported session from sqlalchemy
SessionLocal = sessionmaker(engine,autocommit=False, autoflush=False)

# this will return a class, from this later the database models are created
Base = declarative_base()


# is the function for the dependenty to make every time open a new connection and after close to connection to the database.
def get_db():
    db= SessionLocal()
    try:
        # yield makes it that code before and in yeild statements are only executed
        yield db
    finally:
        db.close()