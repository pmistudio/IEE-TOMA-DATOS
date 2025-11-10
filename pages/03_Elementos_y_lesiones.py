
import streamlit as st
import pandas as pd
from utils.storage import load_catalog_yaml, save_uploaded_file
from pathlib import Path

st.header("03 · Elementos y lesiones (por grupos)")

catalog_path = Path("data/catalogo_lesiones.yaml")
catalog = load_catalog_yaml(str(catalog_path)) if catalog_path.exists() else {"Estructura": {"Cimentación": []}}

if "lesiones_registradas" not in st.session_state:
    st.session_state["lesiones_registradas"] = []

grupo = st.selectbox("Grupo", list(catalog.keys()))
subgrupo = st.selectbox("Subgrupo", list(catalog[grupo].keys()))
lesiones_disponibles = catalog[grupo][subgrupo]

lesion = st.text_input("Lesión (descripción breve)")
ubicacion = st.text_input("Ubicación/elemento", placeholder="Ej.: Fachada patio, portal A...")
nivel = st.selectbox("Nivel de daño estimado", ["Bajo", "Medio", "Alto"])
actuacion = st.selectbox("Actuación propuesta", ["Vigilancia", "Mantenimiento", "Reparación urgente", "Reparación programada"])
observ = st.text_area("Observaciones")

foto = st.file_uploader("Foto (opcional)", type=["jpg","jpeg","png"])
ruta_foto = ""
if st.session_state.get("project_id") and foto:
    ruta_foto = save_uploaded_file(st.session_state["project_id"], foto, prefix="lesion")

if st.button("Añadir a lista"):
    st.session_state["lesiones_registradas"].append({
        "grupo": grupo,
        "subgrupo": subgrupo,
        "lesion": lesion,
        "ubicacion": ubicacion,
        "nivel": nivel,
        "actuacion": actuacion,
        "observaciones": observ,
        "foto": ruta_foto
    })
    st.success("Lesión añadida.")

st.subheader("Listado de lesiones registradas")
if st.session_state["lesiones_registradas"]:
    df = pd.DataFrame(st.session_state["lesiones_registradas"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("Aún no hay lesiones registradas.")
