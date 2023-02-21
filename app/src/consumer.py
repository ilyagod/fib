#!/usr/bin/env python
import os

import mq
from fib import calc_fib


def callback(ch, method, properties, body):
    try:
        number = int(body.decode('utf8'))
    except Exception:
        return
    print('Result fib:', calc_fib(number))


channel = mq.get_channel()
channel.basic_consume(queue=os.getenv('RABBITMQ_QUEUE'), on_message_callback=callback)

print('[*] Waiting for numbers')
channel.start_consuming()
