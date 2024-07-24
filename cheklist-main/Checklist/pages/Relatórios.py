import streamlit as st
import pandas as pd
from teste import enviar_emaail,enviar_emaail2
from fpdf import FPDF
from io import BytesIO
from datetime import datetime
import pytz
from Estatísticas import estatistica
import requests



lista = []
lista_problema = []
image = st.image('https://www.logolynx.com/images/logolynx/fe/fe346f78d111e1d702b44186af59b568.jpeg')
lista_nomes = []
requiscao = requests.get('https://bancodedadosroteirooficial-default-rtdb.firebaseio.com/.json')
roteiro = requiscao.json()
dados = roteiro['Checklists']
for item in dados:
                            Checklist = dados[f'{item}']
                            for elemento in Checklist:
                                     espec = Checklist[f'{elemento}']
                                     Data = espec['Data']
                                     lista_ok  = espec['ok']
                                     for item in lista_ok:
                                       lista.append(item)
                                     lista_nao  = espec['Anormais'] 
                                     for item in lista_nao:
                                       lista_problema.append(item) 
                                     
st.write(f'{len(lista_ok) foram encontrados}')
