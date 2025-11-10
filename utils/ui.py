
import streamlit as st

CARD = """
<div style="background:{bg}; border-radius:16px; padding:16px; color:white; box-shadow:0 2px 10px rgba(0,0,0,0.08);">
  <div style="font-size:0.95rem; opacity:0.9; margin-bottom:6px;">{subtitle}</div>
  <div style="display:flex; align-items:center; justify-content:space-between;">
    <div style="font-size:1.4rem; font-weight:700;">{title}</div>
    <div style="font-size:1.2rem;">{icon}</div>
  </div>
</div>
"""

def card(title, subtitle="", icon="📌", bg="#6C63FF"):
    st.markdown(CARD.format(title=title, subtitle=subtitle, icon=icon, bg=bg), unsafe_allow_html=True)

def quick_button(label, helptext="", key=None):
    return st.button(label, help=helptext, use_container_width=True)

def progress(label, pct, color="#22c55e"):
    pct = max(0, min(100, int(pct)))
    st.markdown(f"<div style='display:flex;justify-content:space-between'><b>{label}</b><span>{pct}%</span></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="height:8px;background:#e5e7eb;border-radius:999px;">
      <div style="height:8px;width:{pct}%;background:{color};border-radius:999px;"></div>
    </div>
    """, unsafe_allow_html=True)

def pill(text, bg="#f1f5f9", fg="#0f172a"):
    st.markdown(f"<span style='background:{bg};color:{fg};padding:4px 10px;border-radius:999px;font-size:0.8rem'>{text}</span>", unsafe_allow_html=True)
