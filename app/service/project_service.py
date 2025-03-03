from models.project import Project as ProjectModel
from models.project import Project


class ProjectService():

    def __init__(self, db) -> None:
        self.db = db

    def get_projects(self):
        return self.db.query(ProjectModel).all()

    def get_project(self, id: int):
        return self.db.query(ProjectModel).filter(ProjectModel.id == id).first()

    def get_projects_by_user(self, user_id: int):
        return self.db.query(ProjectModel).filter(ProjectModel.user_id == user_id).all()

    def create_project(self, project: Project, user_id: int):
        new_project = ProjectModel(**project.dict())
        self.db.add(new_project)
        self.db.commit()
        return new_project

    def update_project(self, id: int, data: Project):
        project = self.get_project(id)
        project.name = data.name
        project.description = data.description
        self.db.commit()
        return

    def delete_project(self, id: int):
        project = self.get_project(id)
        self.db.delete(project)
        self.db.commit()
        return
