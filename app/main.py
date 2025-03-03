from fastapi import FastAPI
from config.database import engine, Base
from routes.user import user_router
from routes.project import project_router
from routes.image import image_router
from routes.processed_image import processed_image_router

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

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

# Ruta de inicio
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenido a la API SaaS de Visión por Computadora 🚀"}
