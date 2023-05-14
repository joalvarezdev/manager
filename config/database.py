from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.configuration import get_db_configuration

datasource: dict = get_db_configuration()

DB_URL = f"""postgresql://{datasource['username']}:{datasource['password']}@{datasource['host']}:{datasource['port']}/{datasource['db_name']}"""

engine = create_engine(DB_URL)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()


def get_database():
    database = session_local()
    try:
        yield database
    finally:
        database.close()
