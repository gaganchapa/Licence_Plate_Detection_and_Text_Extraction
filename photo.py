import streamlit as st
picture = st.camera_input("First, take a picture...")

st.write(picture)