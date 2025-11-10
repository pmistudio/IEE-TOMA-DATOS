
import streamlit as st
from utils.ui import card, quick_button, progress, pill

st.header("Inicio · Panel de inspección")

colA, _ = st.columns([1,1])
with colA:
    comp = len(st.session_state.get("lesiones_registradas", []))
    pend = 0
    avance = 72 if st.session_state.get("ventanas") else 35
    card(
        title=f"Completadas: {comp}  ·  Pendientes: {pend}",
        subtitle="¡Hola inspector! Continúa tu evaluación energética",
        icon="📈",
        bg="#6C63FF"
    )

st.subheader("Acciones rápidas")
c1,c2,c3,c4 = st.columns(4)
with c1:
    if quick_button("📷 Nueva Foto", "Capturar evidencia"):
        st.session_state["__nav_to__"] = "03 · Elementos y lesiones (selector visual por grupos)"
with c2:
    if quick_button("📏 Medición", "Tomar datos"):
        st.session_state["__nav_to__"] = "02 · Datos generales del edificio"
with c3:
    if quick_button("✅ Checklist", "Verificar ítems"):
        st.toast("Checklist básico pendiente de implementar")
with c4:
    if quick_button("📄 Reporte", "Generar PDF/MD"):
        st.session_state["__nav_to__"] = "05 · Resumen, validación y exportación"

st.divider()

st.subheader("Progreso de inspección")
progress("Envolvente Térmica", 85, color="#22c55e")
progress("Sistemas de Calefacción", 60, color="#3b82f6")
progress("Iluminación", 40, color="#f59e0b")

st.divider()

st.subheader("Categorías de evaluación")
with st.expander("🧱 Envolvente Térmica · Muros, ventanas, techos", expanded=False):
    pill("Muros"); st.write("—")
    pill("Ventanas"); st.write("—")
    pill("Cubiertas"); st.write("—")
with st.expander("🔥 Sistemas de Calefacción · Calderas, radiadores", expanded=False):
    pill("Calderas"); st.write("—")
    pill("Radiadores"); st.write("—")

st.divider()

st.subheader("Fotos recientes")
fotos = []
for l in st.session_state.get("lesiones_registradas", []):
    if l.get("foto"):
        fotos.append(l["foto"])
for v in st.session_state.get("ventanas", []):
    if v.get("foto"):
        fotos.append(v["foto"])

if fotos:
    cols = st.columns(min(4, len(fotos)))
    for i, f in enumerate(fotos[:8]):
        with cols[i % len(cols)]:
            st.image(f, use_column_width=True, caption=f.split("/")[-1][:14])
else:
    st.info("Aún no hay fotos. Añade desde **Lesiones** o **Ventanas**.")

st.divider()

st.subheader("Inspecciones guardadas")
c1, c2 = st.columns(2)
with c1:
    st.markdown("**Edificio Residencial A**  
Calle Mayor 12, Madrid")
    pill("Completo", bg="#dcfce7", fg="#14532d")
with c2:
    st.markdown("**Oficinas Centro**  
Av. Libertad 45B")
    pill("En Progreso", bg="#fff7ed", fg="#7c2d12")

st.caption("Navega por el menú lateral para completar cada sección.")
