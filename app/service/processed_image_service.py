from models.processed_image import ProcessedImage as ProcessedImageModel
from models.processed_image import ProcessedImage


class ProcessedImageService():

    def __init__(self, db) -> None:
        self.db = db

    def get_processed_images(self):
        return self.db.query(ProcessedImageModel).all()

    def get_processed_image(self, id: int):
        return self.db.query(ProcessedImageModel).filter(ProcessedImageModel.id == id).first()

    def get_processed_images_by_image(self, image_id: int):
        return self.db.query(ProcessedImageModel).filter(ProcessedImageModel.image_id == image_id).all()

    def create_processed_image(self, processed_image: ProcessedImage, image_id: int):
        new_processed_image = ProcessedImageModel(
            filename=processed_image.filename,
            content_type=processed_image.content_type,
            data=processed_image.data,
            image_id=image_id
        )
        self.db.add(new_processed_image)
        self.db.commit()
        return

    def update_processed_image(self, id: int, data: ProcessedImage):
        processed_image = self.get_processed_image(id)
        processed_image.filename = data.filename
        processed_image.content_type = data.content_type
        processed_image.data = data.data
        self.db.commit()
        return

    def delete_processed_image(self, id: int):
        processed_image = self.get_processed_image(id)
        self.db.delete(processed_image)
        self.db.commit()
        return
