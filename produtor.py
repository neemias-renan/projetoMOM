# produtor.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila')

def publicar_mensagem(mensagem):
    channel.basic_publish(exchange='', routing_key='fila', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')

connection.close()
