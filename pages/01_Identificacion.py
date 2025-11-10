
import streamlit as st
from datetime import date

st.header("01 · Identificación y localización")

project_id = st.text_input("ID de proyecto", help="Ej.: IEE_Picasso26_2025")
st.session_state.setdefault("project_id", project_id or st.session_state.get("project_id", ""))

col1, col2 = st.columns(2)
with col1:
    promotor = st.text_input("Propiedad / Comunidad", placeholder="Comunidad de Propietarios ...")
    direccion = st.text_input("Dirección", placeholder="C/ ..., nº ..., municipio")
    municipio = st.text_input("Municipio", placeholder="Alicante / Alacant")
    ref_catastral = st.text_input("Referencia catastral", placeholder="XXXXXXXXYHXXXXZ")
with col2:
    cp = st.text_input("CP", placeholder="030xx")
    provincia = st.text_input("Provincia", placeholder="Alicante")
    coordenadas = st.text_input("Coordenadas (lat,lon)", placeholder="38.3452,-0.4815")
    fecha_visita = st.date_input("Fecha de visita", value=date.today())

st.session_state["identificacion"] = {
    "project_id": st.session_state.get("project_id", ""),
    "promotor": promotor,
    "direccion": direccion,
    "municipio": municipio,
    "cp": cp,
    "provincia": provincia,
    "ref_catastral": ref_catastral,
    "coordenadas": coordenadas,
    "fecha_visita": str(fecha_visita),
}

st.success("Datos guardados en memoria de sesión.")
