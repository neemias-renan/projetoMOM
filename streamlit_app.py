# streamlit_app.py
import streamlit as st
import requests

# Função para enviar uma mensagem ao servidor
def enviar_mensagem(mensagem):
    # URL para enviar a mensagem ao servidor
    url = 'http://localhost:5000/enviar_mensagem'
    data = {'mensagem': mensagem}
    response = requests.post(url, json=data)
    return response.json()['mensagem']

# Função para obter mensagens do servidor
def obter_mensagens():
    url = 'http://localhost:5000/obter_mensagens'
    response = requests.get(url)

    if response.status_code == 200:
        mensagem_recuperada = response.json()['mensagem']
        return mensagem_recuperada
    else:
        return 'Nenhuma mensagem disponível no momento.'


#Interface do Streamlit
st.title('Sistema de Mensagens')
mensagem = st.text_input('Digite a mensagem:')
if st.button('Enviar'):
    resultado_envio = enviar_mensagem(mensagem)
st.title('Mensagens Submetidas')
mensagem_recuperada = obter_mensagens()
st.write(f'Mensagem Recebida: {mensagem_recuperada}')
