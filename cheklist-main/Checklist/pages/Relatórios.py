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
from Adicionar_Imagens import exibir_imagem
css_style = """
            .my-square {
                background-color:#0275b1;
                border-radius: 10px;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
            }
        """
        
        # Aplicando o estilo e inserindo os quadrados
st.markdown(f"<style>{css_style}</style>", unsafe_allow_html=True)
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
  st.markdown(f'<div class="my-square">{Total} Cheklists foram encontrados</div>', unsafe_allow_html=True)
  st.divider()          
  st.markdown(f'<div class="my-square">Total de Verificações Positivas: {Total_positivas}</div>', unsafe_allow_html=True)
  st.divider()          
  st.markdown(f'<div class="my-square">Total de Verificações Negativas: {Total_negativas}</div>', unsafe_allow_html=True)
  st.divider()          
  st.markdown(f'<div class="my-square">Percentual de Positividade Total: {percentual:.2f} %</div>', unsafe_allow_html=True)

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
               
  
  data = st.selectbox("Selecione uma data",lista)
  seletor  = option_menu("Usuários", ["Juan Zonho", "Jonatan Lima","Cesar Fusel","Luiz Felipe"], default_index=1)          
  lista_item_repetido =[]
  lista_normais = []
  lista_imagens = []
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
                                                      lista_normais.append(item)
                                               lista_anormal = espec['Anormais'] 
                                               for item in lista_anormal:
                                                      lista_problema.append(item) 
                                               try           :
                                                           lista1 = espec['Imagens']
                                                           for item in lista1:
                                                                       lista_imagens.append(item)
                                               except:
                                                           pass
          
  dict = {'Itens ok':lista_normais,'Itens Anormais':lista_problema}
  tabela = pd.DataFrame(dict)
  st.table(tabela) 
  caracter = './captured_image_'          
  if len(lista_imagens) > 0:
              botao = st.button('Ver Imagens do Checklist')
              if botao:
                          for item in lista_imagens:
                                      
                                      nome = item.replace(caracter,'')
                                      exibir_imagem(item,nome)
              
