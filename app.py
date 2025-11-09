
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="IEE · Toma de Datos", page_icon="📸", layout="centered")
st.title("📸 IEE · Toma de datos en obra")

st.write("Usa el menú lateral para capturar imágenes y rellenar la ficha del elemento.")
st.sidebar.success("Selecciona una sección del menú.")
