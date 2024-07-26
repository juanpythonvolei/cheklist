import streamlit as st

def adicionar_imagem(nome_texto,nome_link,lista):
    image = st.camera_input(label='Adicione uma foto',key=f'{nome_texto}')
    with open(f'captured_image_{nome_link}.jpg', 'wb') as f:
        f.write(image.getvalue())
    link = f"./captured_image_{nome_link}.jpg"
    lista.append(link)
