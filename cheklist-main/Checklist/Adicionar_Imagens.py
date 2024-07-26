import streamlit as st
image = st.camera_input()
with open('captured_image.jpg', 'wb') as f:
    f.write(image.getvalue())
link = f"./captured_image.jpg"
