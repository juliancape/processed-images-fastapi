import streamlit as st
from components.auth import login_user

def display():
    st.title("Iniciar Sesión")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        email = st.text_input("Correo Electrónico")
        password = st.text_input("Contraseña", type="password")

        if st.button("Iniciar Sesión"):
            # Llamada a la función login_user que hará la autenticación
            if login_user(email, password):
                st.session_state.authenticated = True
                st.rerun()  # reemplaza experimental_rerun
            else:
                st.error("Credenciales incorrectas")

        if st.button("¿No tienes una cuenta? Regístrate aquí"):
            st.session_state.page = "Register"
            st.rerun()  # recarga para mostrar register
