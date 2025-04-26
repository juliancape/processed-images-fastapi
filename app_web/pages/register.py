import streamlit as st
from components.auth import register_user

def display():
    st.title("Registrar Usuario")

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        name = st.text_input("Nombre completo")
        email = st.text_input("Email")
        password = st.text_input("Contraseña", type="password")

        if st.button("Registrar"):
            if register_user(name, email, password):
                st.session_state.authenticated = True
                st.rerun()   # al registrar, forzamos rerun a authenticated
            else:
                st.error("Error al registrar")

        if st.button("¿Ya tienes cuenta? Inicia sesión aquí"):
            st.session_state.page = "Login"
            st.rerun()   # recarga para mostrar login
