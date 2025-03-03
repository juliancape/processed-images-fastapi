from config.database import Base
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    data = Column(LargeBinary, nullable=False)
    inserted_at = Column(DateTime, default=datetime.utcnow())
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    # Cada imagen pertenece a un proyecto
    project = relationship("Project", back_populates="images")
    # Una imagen original puede tener multiples imagenes procesadas
    processed_images = relationship("ProcessedImage", back_populates="original_image")