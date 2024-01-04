# api_gateway.py
from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    mensagem = request.json['mensagem']

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila')
    channel.basic_publish(exchange='', routing_key='fila', body=mensagem)

    connection.close()

    return jsonify({'mensagem': 'Enviada com sucesso!'})



def obter_mensagens():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='fila')

        method_frame, header_frame, body = channel.basic_get(queue='fila')

        if body:
            mensagem = body.decode('utf-8')
            print(f'Mensagem Recebida: {mensagem}')
            
            # Confirme explicitamente que a mensagem foi processada
            channel.basic_ack(method_frame.delivery_tag)  

            connection.close()
            return mensagem
        else:
            connection.close()
            return None

    except Exception as e:
        print(f"Erro ao obter mensagens: {e}")
        return None

@app.route('/obter_mensagens', methods=['GET'])
def obter_mensagens_route():
    mensagem_recuperada = obter_mensagens()

    if mensagem_recuperada:
        return jsonify({'mensagem': mensagem_recuperada}), 200
    else:
        return jsonify({'mensagem': 'Nenhuma mensagem disponível no momento.'}), 404



if __name__ == '__main__':
    app.run(debug=True)
