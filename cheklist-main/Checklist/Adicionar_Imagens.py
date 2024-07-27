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
    try:
        if nome == '...':
            pass
        else:
            st.warning(f'Imagem do item {nome} abaixo')
            image = Image.open(link)
            st.image(image, use_column_width=True)
            st.divider()
    except:
        pass
