from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:test@localhost:5432/postgres"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a sessionmaker for the database session
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# database session
Base=declarative_base()

