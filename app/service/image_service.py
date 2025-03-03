from models.image import Image as ImageModel
from models.image import Image


class ImageService():

    def __init__(self, db) -> None:
        self.db = db

    def get_images(self):
        return self.db.query(ImageModel).all()

    def get_image(self, id: int):
        return self.db.query(ImageModel).filter(ImageModel.id == id).first()

    def get_images_by_project(self, project_id: int):
        return self.db.query(ImageModel).filter(ImageModel.project_id == project_id).all()

    def create_image(self, image: Image):
        new_image = ImageModel(
            filename=image.filename,
            content_type=image.content_type,
            data=image.data,
            project_id=image.project_id
        )
        self.db.add(new_image)
        self.db.commit()
        return

    def update_image(self, id: int, data: Image):
        image = self.get_image(id)
        image.filename = data.filename
        image.content_type = data.content_type
        image.data = data.data
        self.db.commit()
        return

    def delete_image(self, id: int):
        image = self.get_image(id)
        self.db.delete(image)
        self.db.commit()
        return
