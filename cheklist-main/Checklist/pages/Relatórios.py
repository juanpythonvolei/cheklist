import streamlit as st
import pandas as pd
from teste import enviar_emaail,enviar_emaail2
from fpdf import FPDF
from io import BytesIO
from datetime import datetime
import pytz
from Estatísticas import estatistica
import requests
import google.generativeai as genai
from streamlit_option_menu import option_menu

lista_item_repetido =[]
lista_normais = []
lista = []
lista_problema = []
image = st.image('https://www.logolynx.com/images/logolynx/fe/fe346f78d111e1d702b44186af59b568.jpeg')
opcao_selecionada = st.selectbox("Selecione uma Opação",['Dados Gerais','Item com mais ocorrências','Ver Checklists'])
lista_nomes = []
requiscao = requests.get('https://bancodedadosroteirooficial-default-rtdb.firebaseio.com/.json')
roteiro = requiscao.json()
dados = roteiro['Checklists']
if opcao_selecionada == 'Dados Gerais':
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
  
  percentual = float((len(lista_normais)/(len(lista_normais)+len(lista_problema)))*100)
  Total_positivas = len(lista_normais)
  Total_negativas = len(lista_problema)
  Total = len(lista)
  st.write(f'{len(lista)} Cheklists foram encontrados')
  st.write(f'Total de Verificações Positivas: {len(lista_normais)}')
  st.write(f'Total de Verificações Negativas: {len(lista_problema)}')
  st.write(f'Percentual de Positividade Total: {percentual:.2f} %')
elif opcao_selecionada == 'Item com mais ocorrências':
  lista_item_repetido =[]
  lista_normais = []
  lista = []
  lista_problema = []
  texto_problemas = ''
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
  for item in lista_problema:
    texto_problemas += item
  GOOGLE_API_KEY = 'AIzaSyB2uaEtcP8T2_Fy6bhmXC3828qysZEqjNQ'
  genai.configure(api_key=GOOGLE_API_KEY)
  
  model = genai.GenerativeModel('gemini-1.5-flash')
  
  chat = model.start_chat(history=[])
  
  response = chat.send_message(f'Analisando os problemas relatados a seguir, me diga qual o problema, como óleo, rodas etc,que mais se repete dentre as queixas:\n\n{texto_problemas}\n')
  resposta = response.text
  st.write(f'{resposta}')
elif opcao_selecionada == 'Ver Checklists':
  requiscao = requests.get('https://bancodedadosroteirooficial-default-rtdb.firebaseio.com/.json')
  roteiro = requiscao.json()
  dados = roteiro['Checklists']
  for item in dados:
                                lista.append(item)          
  seletor  = option_menu("Usuários", ["Juan Zonho", "Jonatan Lima","Cesar Fusel","Luiz Felipe"], default_index=1)
  data = st.selectbox("Selecione uma data",lista)
  lista_item_repetido =[]
  lista_normais = []
  
  lista_problema = []
  texto_problemas = ''
  requiscao = requests.get('https://bancodedadosroteirooficial-default-rtdb.firebaseio.com/.json')
  roteiro = requiscao.json()
  dados = roteiro['Checklists']
  for item in dados:
                                lista.append(item)          
                                Checklist = dados[f'{item}']
                                for elemento in Checklist:
                                         espec = Checklist[f'{elemento}']
                                         usuario = espec['Usuário'] 
                                         Data = espec['Data'] 
                                         if usuario == seletor and Data == data: 
                                           
                                             lista_ok  = espec['ok']
                                             for item in lista_ok:
                                                  if item  != '...':
                                                    lista_normais.append(item)
                                             lista_anormal = espec['Anormais'] 
                                             for item in lista_anormal:
                                                  if item  != '...':
                                                    lista_problema.append(item) 
dict = {'Itens ok':lista_normais,'Itens Anoramis':lista_problema}
tabela = pd.pd.DataFrame(dict)
st.table(tabela)
