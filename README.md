# Sistema de Procesamiento de Imágenes con FastAPI

## 🧩 Problema que se busca resolver

En muchos entornos industriales, médicos o de vigilancia, es necesario procesar imágenes para extraer información crítica, generar alertas o simplemente almacenar datos relevantes para auditorías. Este proyecto ofrece una **API RESTful basada en FastAPI** que permite a los usuarios:

- Gestionar sus cuentas y proyectos.
- Subir imágenes originales a proyectos.
- Almacenar imágenes procesadas (por algún modelo externo de visión por computadora).
- Consultar, actualizar o eliminar sus datos en un sistema estructurado.

El objetivo es servir como **backend de un sistema SaaS** especializado en visión por computadora, donde la lógica de procesamiento se encuentra en otro servicio, y este backend actúa como repositorio y organizador de la información.

---

## 🧠 Lógica del backend

La aplicación está estructurada siguiendo buenas prácticas de arquitectura:

- **Rutas separadas por entidad**: usuarios, proyectos, imágenes y imágenes procesadas.
- **Servicios desacoplados (`Service`)** que manejan la lógica de negocio.
- **Modelos (`models`) y esquemas (`schemas`)** que siguen el patrón Pydantic y SQLAlchemy.
- **Middleware JWT** para proteger ciertas rutas como la creación de usuarios.
- **Conexión a base de datos** usando SQLAlchemy y sesiones limpias (`Session`).

---

## 🗂️ Estructura de datos (Modelos)

### 1. `User`

Representa un usuario del sistema.

- `id`: Identificador único.
- `name`: Nombre del usuario.
- `email`: Correo electrónico único.
- `hashed_password`: Contraseña encriptada.
- `inserted_at`: Fecha de registro.
- **Relación**: un usuario puede tener múltiples proyectos.

### 2. `Project`

Representa un proyecto de procesamiento de imágenes.

- `id`, `name`, `description`, `created_at`.
- `user_id`: Relación con el usuario que lo creó.
- **Relación**: un proyecto puede tener múltiples imágenes.

### 3. `Image`

Representa una imagen original subida por el usuario.

- `id`, `filename`, `content_type`, `data` (binario), `inserted_at`.
- `project_id`: Relación con el proyecto al que pertenece.
- **Relación**: una imagen puede tener varias imágenes procesadas.

### 4. `ProcessedImage`

Imagen derivada (procesada por un modelo de IA o filtro).

- `id`, `filename`, `content_type`, `data`, `inserted_at`.
- `image_id`: Relación con la imagen original.

---

## 🌐 Endpoints (Rutas)

### 🔐 Autenticación

- `POST /login`: Devuelve un token si el usuario es admin (modo de prueba).  
  **Request:** email y contraseña.

---

### 👤 Usuarios (`/users`)

- `GET /users`: Lista todos los usuarios.
- `GET /users/{id}`: Obtiene un usuario por ID.
- `POST /users`: Crea un usuario (requiere JWT).
- `PUT /users/{id}`: Actualiza un usuario.
- `DELETE /users/{id}`: Elimina un usuario.

---

### 📁 Proyectos (`/projects`)

- `GET /projects`: Lista todos los proyectos.
- `GET /projects/{id}`: Obtiene un proyecto por ID.
- `POST /projects`: Crea un nuevo proyecto asignado a un usuario.
- `PUT /projects/{id}`: Actualiza un proyecto existente.
- `DELETE /projects/{id}`: Elimina un proyecto.

---

### 🖼️ Imágenes (`/images`)

- `GET /images`: Lista todas las imágenes originales.
- `GET /images/{id}`: Obtiene una imagen por ID.
- `POST /images`: Sube una nueva imagen.
- `DELETE /images/{id}`: Elimina una imagen.

---

### 🧠 Imágenes procesadas (`/processed_images`)

- `GET /processed_images`: Lista todas las imágenes procesadas.
- `GET /processed_images/{id}`: Obtiene una imagen procesada.
- `POST /processed_images`: Sube una imagen procesada.
- `DELETE /processed_images/{id}`: Elimina una imagen procesada.

---

## 🔐 Seguridad

- Se utiliza un middleware `JWTBearer` para proteger rutas sensibles como la creación de usuarios.
- En el login de prueba se genera un token JWT con correo y contraseña si son `admin@gmail.com` y `admin`.

---

## 🚀 Tecnologías utilizadas

- **FastAPI**: Framework principal para construir la API.
- **SQLAlchemy**: ORM para interactuar con la base de datos.
- **Pydantic**: Validación y serialización de datos.
- **JWT**: Autenticación segura.
- **PostgreSQL / SQLite**: Puede usarse como base de datos relacional.
- **Uvicorn**: Servidor ASGI para desarrollo local.

---

## ✅ ¿Por qué esta estructura?

- **Escalabilidad**: Cada entidad está desacoplada y puede crecer sin romper el resto.
- **Modularidad**: Puedes conectar fácilmente una interfaz frontend o un microservicio de IA.
- **Facilidad de pruebas y mantenibilidad**.

---

## 📦 Cómo ejecutar

```bash
# Crear entorno virtual
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements.txt

# Correr el servidor
uvicorn main:app --reload
