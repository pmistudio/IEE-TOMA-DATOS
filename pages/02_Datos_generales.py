
import streamlit as st

st.header("02 · Datos generales del edificio")

col1, col2 = st.columns(2)
with col1:
    uso_principal = st.selectbox("Uso principal", ["Residencial", "Residencial + Locales", "Terciario", "Otro"])
    anno_construccion = st.number_input("Año construcción (aprox.)", min_value=1800, max_value=2100, value=1975)
    num_plantas = st.number_input("Nº de plantas sobre rasante", min_value=1, max_value=50, value=4)
    num_sotanos = st.number_input("Nº de plantas bajo rasante", min_value=0, max_value=5, value=0)
with col2:
    tipologia = st.selectbox("Tipología", ["Entre medianeras", "Aislado", "Manzana cerrada", "Bloque abierto"])
    estructura = st.selectbox("Estructura principal", ["Hormigón", "Acero", "Madera", "Mixta", "Fábrica"])
    envolvente = st.multiselect("Envolvente", ["Fachada ladrillo", "Fachada SATE", "Fachada ventilada", "Cubierta plana", "Cubierta inclinada"])
    ascensor = st.selectbox("Ascensor", ["Sí", "No"])

st.subheader("Accesibilidad")
acc_itinerario = st.selectbox("Itinerario accesible a portal", ["Cumple", "No cumple", "Parcial"])
acc_portales = st.text_input("Portales y ámbitos (ancho libre, peldaños, rampas)")
acc_aseos_comunes = st.selectbox("Aseos accesibles en zonas comunes", ["No aplica", "Cumple", "No cumple"])

st.subheader("Conservación (visión general)")
cons_observ = st.text_area("Observaciones (global)")

st.session_state["generales"] = {
    "uso_principal": uso_principal,
    "anno_construccion": anno_construccion,
    "num_plantas": num_plantas,
    "num_sotanos": num_sotanos,
    "tipologia": tipologia,
    "estructura": estructura,
    "envolvente": envolvente,
    "ascensor": ascensor,
    "accesibilidad": {
        "itinerario": acc_itinerario,
        "portales": acc_portales,
        "aseos_comunes": acc_aseos_comunes
    },
    "conservacion_observ": cons_observ
}

st.success("Datos guardados en memoria de sesión.")
