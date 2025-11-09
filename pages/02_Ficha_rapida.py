
import streamlit as st
import json
from datetime import datetime

st.header("📝 Ficha rápida de elemento")

with st.form("ficha"):
    tipo = st.selectbox("Tipo de elemento", ["Ventana","Puerta","Fachada","Cubierta","Instalación"])
    orient = st.selectbox("Orientación", ["N","NE","E","SE","S","SO","O","NO"])
    notas = st.text_area("Notas adicionales")
    submitted = st.form_submit_button("Generar ficha")

if submitted:
    data = {
        "tipo": tipo,
        "orientacion": orient,
        "notas": notas,
        "timestamp": datetime.now().isoformat()
    }
    st.success("Ficha generada")
    st.code(json.dumps(data, ensure_ascii=False, indent=2), language="json")
