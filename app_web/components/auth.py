import requests
import streamlit as st
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()
API_URL = os.getenv("API_URL")

def login_user(email: str, password: str) -> bool:
    # Preparar el payload
    user_data = {"email": email, "hashed_password": password}

    # Hacer la solicitud POST a la API
    try:
        response = requests.post(f"{API_URL}/login", json=user_data)

        # Si la respuesta es exitosa (status_code 200), el login es correcto
        if response.status_code == 200:
            token = response.json()  # Token de autenticación
            st.session_state.token = token  # Guardar el token en session_state
            return True
        else:
            return False
    except Exception as e:
        st.error(f"Error al conectar con la API: {e}")
        return False

def register_user(name: str, email: str, password: str) -> bool:
    # Preparar el payload
    user_data = {"name": name, "email": email, "hashed_password": password}

    # Hacer la solicitud POST a la API para crear un nuevo usuario
    try:
        response = requests.post(f"{API_URL}/signup", json=user_data)

        # Si la respuesta es exitosa (status_code 201), el registro es correcto
        if response.status_code == 201:
            st.success("Registro exitoso. Ahora puedes iniciar sesión.")
            return True
        else:
            st.error(f"Error al registrar usuario: {response.json().get('message', 'Error desconocido')}")
            return False
    except Exception as e:
        st.error(f"Error al conectar con la API: {e}")
        return False
