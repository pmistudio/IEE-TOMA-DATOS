
import streamlit as st
import pandas as pd
from utils.storage import save_uploaded_file

st.header("04 · CEE · Ventanas")

if "ventanas" not in st.session_state:
    st.session_state["ventanas"] = []

col1, col2 = st.columns(2)
with col1:
    estancia = st.text_input("Estancia/Ubicación", placeholder="Dormitorio 1, Salón, Escalera...")
    orient = st.selectbox("Orientación", ["N", "NE", "E", "SE", "S", "SO", "O", "NO"])
    hueco_ancho = st.number_input("Hueco ancho (m)", min_value=0.0, value=1.20, step=0.01)
    hueco_alto = st.number_input("Hueco alto (m)", min_value=0.0, value=1.20, step=0.01)
with col2:
    marco = st.selectbox("Tipo de marco", ["Aluminio sin RPT", "Aluminio con RPT", "PVC", "Madera", "Mixto"])
    vidrio = st.selectbox("Tipo de vidrio", ["Sencillo", "Doble 4/6/4", "Doble bajo emisivo", "Triple"])
    apert = st.selectbox("Tipo de apertura", ["Fijo", "Abatible", "Oscilobatiente", "Corredera", "Proyectante"])
    color = st.text_input("Color marco (aprox.)", placeholder="Blanco, Antracita, Moka...")

foto = st.file_uploader("Foto de la ventana (opcional)", type=["jpg","jpeg","png"])
ruta_foto = ""
if st.session_state.get("project_id") and foto:
    ruta_foto = save_uploaded_file(st.session_state["project_id"], foto, prefix="ventana")

desc = st.text_area("Descripción automática (puedes editar)", value="")

if st.button("Añadir ventana"):
    auto_desc = desc or f"{marco} · {vidrio} · {apert} · color {color}".strip()
    st.session_state["ventanas"].append({
        "estancia": estancia,
        "orientacion": orient,
        "ancho": hueco_ancho,
        "alto": hueco_alto,
        "marco": marco,
        "vidrio": vidrio,
        "apertura": apert,
        "color": color,
        "descripcion": auto_desc,
        "foto": ruta_foto
    })
    st.success("Ventana añadida.")

st.subheader("Listado de ventanas")
if st.session_state["ventanas"]:
    df = pd.DataFrame(st.session_state["ventanas"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("Aún no hay ventanas registradas.")
