
import streamlit as st
import pandas as pd
from utils.storage import save_json, save_md
from datetime import datetime

st.header("05 · Resumen, validación y exportación")

pid = st.session_state.get("project_id", "").strip()
if not pid:
    st.error("Primero define un ID de proyecto en la página 01.")
    st.stop()

ident = st.session_state.get("identificacion", {})
gener = st.session_state.get("generales", {})
les = st.session_state.get("lesiones_registradas", [])
ven = st.session_state.get("ventanas", [])

st.subheader("Validación rápida")
ok = True
req_fields = {"Propiedad / Comunidad": ident.get("promotor"), "Dirección": ident.get("direccion"),
              "Municipio": ident.get("municipio"), "Ref. catastral": ident.get("ref_catastral"),
              "Año construcción": gener.get("anno_construccion")}
for label, value in req_fields.items():
    if not value:
        st.warning(f"Campo requerido vacío: {label}")
        ok = False

st.subheader("Resumen")
st.write("Identificación:", ident)
st.write("Generales:", gener)
st.write("Lesiones:", pd.DataFrame(les) if les else "—")
st.write("Ventanas (CEE):", pd.DataFrame(ven) if ven else "—")

def mk_markdown(pid, ident, gener, les, ven):
    lines = []
    lines.append("# IEE · Toma de datos")
    lines.append(f"- Proyecto: {pid}")
    lines.append(f"- Dirección: {ident.get('direccion','')}")
    return "\n".join(lines)

if st.button("Exportar JSON + Markdown"):
    bundle = {"identificacion": ident, "generales": gener, "lesiones": les, "ventanas": ven, "exportado_en": datetime.now().isoformat()}
    json_path = save_json(pid, bundle, name="iee_datos.json")
    md_path = save_md(pid, mk_markdown(pid, ident, gener, les, ven), name="iee_resumen.md")
    st.success(f"Exportado: {json_path} · {md_path}")
