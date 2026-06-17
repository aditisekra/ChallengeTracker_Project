from sqlalchemy import Integer,String,Column
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from datetime import datetime,timezone

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    challenges=relationship("Challenges",back_populates="user")
    created_at = Column(
    DateTime,
    default=datetime.now(timezone.utc))

    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )

