import requests
import os

# Cargar variables de entorno
API_URL = os.getenv("API_URL")

def get_users():
    """Obtener la lista de usuarios"""
    response = requests.get(f"{API_URL}/users")
    if response.status_code == 200:
        return response.json()
    return []

def get_user_by_id(user_id):
    """Obtener un usuario por su ID"""
    response = requests.get(f"{API_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None
