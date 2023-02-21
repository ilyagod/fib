import os

import pika


def get_channel():
    credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USER'), os.getenv('RABBITMQ_PASS'))
    parameters = pika.ConnectionParameters(os.getenv('RABBITMQ_HOST'), os.getenv('RABBITMQ_PORT'),
                                           os.getenv('RABBITMQ_VHOST'), credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue=os.getenv('RABBITMQ_QUEUE'))

    return channel