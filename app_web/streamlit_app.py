import streamlit as st
from pages import login, register, dashboard, upload_image

# Configuración de la página inicial
#st.set_page_config(page_title="Mi Proyecto", page_icon="🎨", initial_sidebar_state="collapsed")

# Estado inicial
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Antes de la autenticación: mostrar login o register
if not st.session_state.authenticated:
    # No se cambia la configuración de la página aquí, solo mostramos las pantallas correspondientes
    if st.session_state.page == "Login":
        login.display()
    else:
        register.display()

    st.stop()  # detiene el flujo si no está autenticado

# Después de la autenticación: mostrar sidebar con páginas protegidas
# Configuramos la barra lateral solo después de la autenticación
if st.session_state.authenticated:
    st.set_page_config(page_title="Dashboard", page_icon="📊", initial_sidebar_state="expanded")
    st.sidebar.title("Navegación")
    page = st.sidebar.selectbox("Selecciona una opción", ["Dashboard", "Upload Image", "Logout"])

    # Contenido dependiendo de la página seleccionada
    if page == "Dashboard":
        dashboard.display()
    elif page == "Upload Image":
        upload_image.display()
    else:  # Logout
        st.session_state.authenticated = False
        st.session_state.page = "Login"
        st.session_state.token = None
        st.rerun()
