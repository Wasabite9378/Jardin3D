
import streamlit as st
import streamlit.components.v1 as components

st.title("Jardin 3D - Visualisation")

# Charger le contenu HTML
with open("Jardin3D_23-10-25.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Afficher le HTML dans Streamlit
