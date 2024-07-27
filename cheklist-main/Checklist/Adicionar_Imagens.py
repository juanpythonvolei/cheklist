import streamlit as st
from PIL import Image
def adicionar_imagem(nome_texto,nome_link,lista):
    image = st.camera_input(label='Adicione uma foto',key=f'{nome_texto}')
    if image:
        with open(f'captured_image_{nome_link}.jpg', 'wb') as f:
            f.write(image.getvalue())
        link = f"./captured_image_{nome_link}.jpg"
        lista.append(link) 
    else:
        pass
def exibir_imagem(link,nome):
    st.warning(f'{nome}')
    image = Image.open(link)
    st.image(image, use_column_width=True)
