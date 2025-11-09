
import streamlit as st
from datetime import datetime

st.header("📸 Captura de fotos")

photo = st.camera_input("Haz una foto (permite cámara desde móvil)")

if photo:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"IEE_captura_{ts}.jpg"
    st.image(photo, caption=fname, use_column_width=True)
    st.download_button("Descargar imagen", data=photo.getvalue(), file_name=fname, mime="image/jpeg")
