import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="TwinAI 3D",
    layout="wide"
)

st.title("TwinAI 3D")

image = Image.open("assets/hero.jpg")

st.image(image)

st.write("Meet Your Future Self")
