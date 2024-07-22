import qrcode
import streamlit as st
# URL que você deseja codificar no QR code

image = st.image('https://www.logolynx.com/images/logolynx/fe/fe346f78d111e1d702b44186af59b568.jpeg')

url = "https://cheklist-5zyysp6sntm2pdtcfnssg3.streamlit.app/?embed_options=dark_theme"

# Cria o QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Cria uma imagem do QR code
img_qrcode = qr.make_image(fill_color="black", back_color="white")


Codigo = st.image(f'{img_qrcode}')
