from config.database import Base
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    inserted_at = Column(DateTime, default=datetime.utcnow())

    # Un usuario puede tener muchos proyectos
    projects = relationship("Project", back_populates="owner")