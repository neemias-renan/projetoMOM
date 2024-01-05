# A biblioteca pika é utilizada para estabelecer uma conexão com um servidor RabbitMQ.

from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

# ▼ Estabelece a conexão com o servidor RabbitMQ na máquina local
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# ▼ Cria um canal de comunicação dentro da conexão para realizar operações, como declarar filas e publicar/consumir mensagens.
channel = connection.channel()

# Declara a fila chamada 'fila'
channel.queue_declare(queue='fila')

# Função de callback para processar mensagens recebidas da fila
def callback(ch, method, properties, body):
    print(f"Mensagem recebida: {body.decode('utf-8')}")

# Rota para enviar mensagem via método POST
@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem_route():
    try:
        mensagem = request.json['mensagem']
        
        # Publica a mensagem na fila
        channel.basic_publish(exchange='', routing_key='fila', body=mensagem)

        return jsonify({'mensagem': 'Enviada com sucesso!'})

    except Exception as e:
        return jsonify({'mensagem': f'Erro ao enviar mensagem: {e}'}), 500

# Rota para obter mensagens via método GET
@app.route('/obter_mensagens', methods=['GET'])
def obter_mensagens_route():
    try:
        # Obtém uma mensagem da fila
        method_frame, header_frame, body = channel.basic_get(queue='fila')

        if body:
            mensagem = body.decode('utf-8')
            print(f'Mensagem Recebida: {mensagem}')
            
            # Confirma o processamento da mensagem
            channel.basic_ack(method_frame.delivery_tag)
            
            return jsonify({'mensagem': mensagem}), 200
        else:
            return jsonify({'mensagem': 'Nenhuma mensagem disponível no momento.'}), 404

    except Exception as e:
        return jsonify({'mensagem': f'Erro ao obter mensagens: {e}'}), 500



if __name__ == '__main__':
    app.run(debug=True)
    
    # Configura a função de callback para processar mensagens recebidas da fila
    channel.basic_consume(queue='fila', on_message_callback=callback, auto_ack=True)
    
    # Inicia o processo de consumir mensagens da fila
    channel.start_consuming()
