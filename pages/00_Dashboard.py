
import streamlit as st

st.header("Inicio · Panel de inspección")

st.subheader("Resumen")
comp = len(st.session_state.get("lesiones_registradas", []))
st.metric("Lesiones registradas", comp, help="Añadidas en la página de Lesiones")

st.subheader("Acciones rápidas")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/03_Elementos_y_lesiones.py", label="📷 Nueva foto")
with col2:
    st.page_link("pages/02_Datos_generales.py", label="📏 Medición")
with col3:
    st.page_link("pages/05_Resumen_y_exportacion.py", label="📄 Reporte")
with col4:
    st.page_link("pages/04_CEE_Ventanas.py", label="🪟 Ventanas CEE")

st.subheader("Progreso de inspección")
st.write("Envolvente Térmica")
st.progress(0.85)
st.write("Sistemas de Calefacción")
st.progress(0.60)
st.write("Iluminación")
st.progress(0.40)

st.caption("Consejo: define un ID de proyecto en Identificación antes de empezar.")
