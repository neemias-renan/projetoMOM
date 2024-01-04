# streamlit_app.py
import streamlit as st
import requests

st.title('Sistema de Mensagens')

mensagem = st.text_input('Digite a mensagem:')
if st.button('Enviar'):
    url = 'http://localhost:5000/enviar_mensagem'
    data = {'mensagem': mensagem}
    response = requests.post(url, json=data)
    st.success(response.json()['mensagem'])

# Lista de mensagens submetidas
st.title('Mensagens Submetidas')
if st.button('Atualizar Mensagens'):
    url = 'http://localhost:5000/obter_mensagens'
    response = requests.get(url)

    if response.status_code == 200:
        mensagem_recuperada = response.json()['mensagem']
        st.write(f'Mensagem Recebida: {mensagem_recuperada}')
    else:
        st.write('Nenhuma mensagem disponível no momento.')