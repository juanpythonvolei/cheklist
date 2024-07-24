import streamlit as st
import pandas as pd
from teste import enviar_emaail,enviar_emaail2
from fpdf import FPDF
from io import BytesIO
from datetime import datetime
import pytz
from Estatísticas import estatistica
import requests

lista_item_repetido =[]
lista_normais = []
lista = []
lista_problema = []
image = st.image('https://www.logolynx.com/images/logolynx/fe/fe346f78d111e1d702b44186af59b568.jpeg')
lista_nomes = []
requiscao = requests.get('https://bancodedadosroteirooficial-default-rtdb.firebaseio.com/.json')
roteiro = requiscao.json()
dados = roteiro['Checklists']
for item in dados:
                            lista.append(item)          
                            Checklist = dados[f'{item}']
                            for elemento in Checklist:
                                     espec = Checklist[f'{elemento}']
                                     Data = espec['Data']
                                     lista_ok  = espec['ok']
                                     for item in lista_ok:
                                          if item  != '...':
                                            lista_normais.append(item)
                                     lista_anormal = espec['Anormais'] 
                                     for item in lista_anormal:
                                          if item  != '...':
                                            lista_problema.append(item) 

                                     
st.write(f'{len(lista)} Cheklists foram encontrados')
st.write(f'Total de Verificações Positivas: {len(lista_normais)}')
st.write(f'Total de Verificações Negativas: {len(lista_problema)}')
for item in lista_problema:
  quantidade = lista_problema.count(item)
  lista_item_repetido.append(f'O item {item} foi observado {quantidade} vezes')
lista_item_repetido = sorted(lista_item_repetido,reverse=True)
