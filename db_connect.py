from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

config = {
	"use_sqlite_rather_than_postgres": False,
	"postgre_connection": "postgresql://postgres:<password>@localhost:5432/<dbname>"
}

if config["use_sqlite_rather_than_postgres"] :
    print("using sqlite")
    SQLALCHEMY_DATABASE_URL = "sqlite:///./mock.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else :
    print("using postgres")
    SQLALCHEMY_DATABASE_URL = config["postgre_connection"]
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Users(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	email = Column(String, unique=True, index=True)
	username = Column(String, unique=True, index=True)
	hashed_password = Column(String)
	is_active = Column(Boolean, default=False)
	is_admin = Column(Boolean, default=False)

	recent_task_id = Column(Integer, ForeignKey("tasks.id"))
	recent_task = relationship("Task", back_populates="recent_users")

class Tasks(Base):
	__tablename__ = "tasks"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	date_created = Column(String)
	is_deleted = Column(Boolean, default=False)

	recent_users = relationship("User", back_populates="recent_task")

Base.metadata.create_all(bind=engine)