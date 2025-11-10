
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="IEE · Toma de Datos (CV)", page_icon="🏛️", layout="centered")

css_path = Path("styles.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

st.title("🏛️ IEE · Toma de Datos · Comunitat Valenciana")
st.write("Usa el menú **Pages** para navegar: Dashboard, Identificación, Generales, Lesiones, CEE y Exportación.")
