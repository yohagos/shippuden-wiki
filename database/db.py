from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_DATABASE_URL = "postgresql://shippuden:shippuden@localhost/shippuden"

engine = create_engine(
    SQL_DATABASE_URL
)

with engine.connect() as connection:
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    for name in tables:
        if (name == "characters"):
            print(name)
    

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

