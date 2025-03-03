from config.database import Base
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

class ProcessedImage(Base):
    __tablename__ = "processed_images"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    data = Column(LargeBinary, nullable=False)
    inserted_at = Column(DateTime, default=datetime.utcnow())
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)

    # Cada imagen procesada pertenece a una imagen original
    original_image = relationship("Image", back_populates="processed_images")