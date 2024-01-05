**Instruções para Iniciar o Sistema**

Este sistema utiliza o RabbitMQ como um sistema de mensagens assíncrono. Antes de iniciar, certifique-se de ter o RabbitMQ e o Erlang instalados em sua máquina.

### Instalação do RabbitMQ e Erlang

1. **Erlang**: O RabbitMQ requer o Erlang para funcionar. Faça o download e instale o Erlang a partir do seguinte link: [Erlang Downloads](https://www.erlang.org/downloads)

2. **RabbitMQ**: Após a instalação do Erlang, faça o download e instale o RabbitMQ a partir do seguinte link: [RabbitMQ Downloads](https://www.rabbitmq.com/download.html)

### Configuração do Ambiente Virtual e Dependências

3. **Ambiente Virtual (venv)**: Crie um ambiente virtual para isolar as dependências do projeto. No terminal, navegue até o diretório do projeto e execute:

    ```bash
    python3 -m venv venv
    ```

4. **Ativação do Ambiente Virtual**: Ative o ambiente virtual de acordo com o sistema operacional:

    - No Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    - No Linux/Mac:

    ```bash
    source venv/bin/activate
    ```

5. **Instalação de Dependências**: Instale as dependências do projeto usando o `pip`. No diretório do projeto, execute:

    ```bash
    pip install -r requirements.txt
    ```

### Inicialização do Sistema

6. **Execução do API Gateway**: Abra um console e navegue até o diretório do projeto. Execute o seguinte comando para iniciar o API Gateway:

    ```bash
    python api_gateway.py
    ```

    Isso iniciará o servidor Flask e configurará a conexão com o RabbitMQ.

7. **Execução do Streamlit App**: Abra um segundo console e navegue até o diretório do projeto. Execute o seguinte comando para iniciar o aplicativo Streamlit:

    ```bash
    streamlit run streamlit_app.py
    ```

    Isso iniciará o aplicativo Streamlit para interação com o sistema.

O sistema está agora pronto para ser utilizado. Certifique-se de ter o RabbitMQ em execução para permitir a comunicação assíncrona entre os componentes do sistema. Consulte a [documentação do RabbitMQ](https://www.rabbitmq.com/documentation.html) para mais informações sobre sua configuração e uso.
