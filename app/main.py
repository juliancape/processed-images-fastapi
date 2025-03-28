from fastapi import FastAPI
from config.database import engine, Base
from routes.user import user_router
from routes.project import project_router
from routes.image import image_router
from routes.processed_image import processed_image_router
from models import processed_image, project, user, image


# Inicializar la aplicación FastAPI
app = FastAPI(
    title="SaaS de Visión por Computadora",
    description="API para enviar imágenes y recibir las imágenes procesadas.",
    version="1.0.0"
)

# Incluir routers
app.include_router(user_router, prefix="/api", tags=["users"])
app.include_router(project_router, prefix="/api", tags=["projects"])
app.include_router(image_router, prefix="/api", tags=["images"])
app.include_router(processed_image_router, prefix="/api", tags=["processed_images"])

@app.on_event("startup")
def startup():
    print("Creando tablas si no existen...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente.")

# Ruta de inicio
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenido a la API SaaS de Visión por Computadora 🚀"}
