import streamlit as st
import pandas as pd
from teste import enviar_emaail,enviar_emaail2
from fpdf import FPDF
from io import BytesIO
from datetime import datetime
import pytz
from Estatísticas import estatistica
import requests




image = st.image('https://www.logolynx.com/images/logolynx/fe/fe346f78d111e1d702b44186af59b568.jpeg')
lista_nomes = []
requiscao = requests.get('https://bancodedadosroteirooficial-default-rtdb.firebaseio.com/.json')
roteiro = requiscao.json()
dados = roteiro['Checklists']
for item in dados:
                            Checklist = dados[f'{item}']
                            for elemento in Checklist:
                                     espec = Checklist[f'{elemento}']
                                     itens_ok= espec['Items ok']
                                     itens_Anormais= espec['Items Anormais'] 
st.write(espec)
