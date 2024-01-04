# consumidor.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila')

def callback(ch, method, properties, body):
    print(f'Mensagem recebida: {body}')

channel.basic_consume(queue='fila', on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens. Para sair, pressione CTRL+C')
channel.start_consuming()
